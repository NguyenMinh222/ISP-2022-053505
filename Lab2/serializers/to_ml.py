import toml
from serializers import pack_unpack
from serializers.s_methods import Serializer


class Toml(Serializer):
    def dumps(self, obj):
        return toml.dumps(pack_unpack.serialize(obj))

    def loads(self, path):
        return pack_unpack.deserialize(toml.loads(path))
