import inspect
import sys
import types
from inspect import getmodule


def serialize(obj):
    """The isinstance() function returns True if the object being checked is
     an instance of the specified class(s) or its subclass (direct, indirect, or virtual)."""
    if isinstance(obj, (str, int, float, bool, types.NoneType)):
        return obj

    if isinstance(obj, dict):
        return {"dict": obj}

    if isinstance(obj, (list, tuple)):
        li = []
        for elements in obj:
            li.append(serialize(elements))
        return {"list": li}

    if isinstance(obj, bytes):
        return {"bytes": obj.hex()}

    if isinstance(obj, types.CodeType):
        attr = []
        elements = {}
        for member in inspect.getmembers(obj):
            if member[0].startswith('co'):
                attr.append(member)

        for attribute in attr:
            elements[serialize(attribute[0])] = serialize(attribute[1])
        return {"code": elements}

    if isinstance(obj, types.FunctionType):
        return {"func": serialize(obj.__code__)}

    if isinstance(obj, type):
        attribs_dict = dict(obj.__dict__)
        for key in attribs_dict.keys():
            attribs_dict[key] = serialize(attribs_dict[key])
        attribs_dict['__annotations__'] = None
        return {"type": {"name": obj.__name__, "attribs": attribs_dict}}

    if (getmodule(type(obj)).__name__ == 'importlib._bootstrap' or
            getmodule(type(obj)).__name__ in sys.builtin_module_names):
        return None

    else:
        obj_dict = serialize(obj.__dict__)
        obj_type = serialize(type(obj))
        return{"object": {"obj_dict": obj_dict, "obj_type": obj_type}}


def deserialize(obj: dict[str, any]) -> any:
    if not isinstance(obj, dict):
        return obj

    for key, value in obj.items():

        if isinstance(value, (str, int, float, bool)):
            return value

        if key == "dict":
            return value

        if key == "list":
            return [deserialize(element) for element in value.values()]

        if key == "tuple":
            if value is None:
                return()
            return tuple(deserialize(element) for element in value.values())

        if key == "bytes":
            return bytes.fromhex(value)

        if key == "code":
            return types.CodeType(
                deserialize(value["co_argcount"]),
                deserialize(value["co_posonlyargcount"]),
                deserialize(value["co_kwonlyargcount"]),
                deserialize(value["co_nlocals"]),
                deserialize(value["co_stacksize"]),
                deserialize(value["co_flags"]),
                deserialize(value["co_code"]),
                tuple(deserialize(value["co_consts"])),
                tuple(deserialize(value["co_names"])),
                tuple(deserialize(value["co_varnames"])),
                deserialize(value["co_filename"]),
                deserialize(value["co_name"]),
                deserialize(value["co_firstlineno"]),
                deserialize(value["co_lnotab"]),
                tuple(deserialize(value["co_freevars"])),
                tuple(deserialize(value["co_cellvars"]))
            )

        if key == "func":
            import __main__
            globals().update(__main__.__dict__)
            def func(): pass
            func.__code__ = deserialize(value)
            return func

        if key == "type":
            import __main__
            globals().update(__main__.__dict__)
            obj_type = getattr(__main__, value['name'], None)
            serialized = serialize(obj_type)

            if (serialized is None
                    or isinstance(serialized, dict)
                    and serialized['type'] != value):
                attribs = value['attribs']
                for i in attribs.keys():
                    attribs[i] = deserialize(attribs[i])

                obj_type = type(
                    value['name'],
                    (object,),
                    attribs
                )

            return obj_type

        if key == "object":
            obj_dict = deserialize(value["obj_dict"])
            obj_type = deserialize(value["obj_type"])

            try:
                obj = object.__new__(obj_type)
                obj.__dict__ = obj_dict
                for (obj_key, obj_value) in obj_dict.items():
                    setattr(obj, obj_key, obj_value)
            except TypeError:
                obj = None
            return obj

    return None
