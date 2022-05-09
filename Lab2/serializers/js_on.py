from serializers import pack_unpack
from serializers.s_methods import Serializer


class Json(Serializer):
    def to_str(self, obj):
        """Create a string according to Json"""
        if isinstance(obj, dict):
            strings = list()
            for key, value in obj.items():
                strings.append(f'{self.to_str(key)}:{self.to_str(value)},')
            return f"{{{''.join(strings)[:-1]}}}"
        elif isinstance(obj, str):
            """Create a character conversion table for the str.obj method"""
            s = obj.translate(str.maketrans({
                "\"": r"\"",
                "\\": r"\\",
            }))
            return f"\"{s}\""
        elif obj is None:
            return 'null'
        else:
            return str(obj)

    def dumps(self, obj):
        """Serializes object, class or function into Json"""
        return self.to_str(pack_unpack.serialize(obj))

    def loads (self, path):
        """Deserializes object, class or function from Json"""
        null = None
        return pack_unpack.deserialize(eval(path))
