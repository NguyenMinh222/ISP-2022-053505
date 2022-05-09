from serializers.fabric_serialize import *
from console.argsparser import ArgParser

dump_in, load_from = ArgParser.get_arguments()


def get_creator(filename: str) -> CreateSerializer | None:
    filetype = filename.lower().split('.')[-1]
    creators = {
        'json': CreateJson,
        'yaml': CreateYaml,
        'toml': CreateToml
    }
    return creators.get(filetype, None)


def dump(obj, filename: str) -> any:
    creator = get_creator(filename)
    if creator is None:
        return None
    ser = creator.create()
    ser.dump(obj, filename)
    obj = ser.load(filename)
    print("Object dumped successfully")
    return obj


def load(filename: str) -> any:
    creator = get_creator(filename)
    if creator is None:
        return None
    ser = creator.create()
    item = ser.load(filename)
    print("Object loaded successfully")
    return item


def convert():
    global obj
    if load_from is not None:
        obj = load(''.join(load_from))

    if dump_in is not None:
        dump(obj, ''.join(dump_in))