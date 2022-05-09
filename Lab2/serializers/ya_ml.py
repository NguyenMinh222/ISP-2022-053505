import yaml
from serializers import pack_unpack
from serializers.s_methods import Serializer


class Yaml(Serializer):
    def dumps(self, obj):
        return yaml.dump(pack_unpack.serialize(obj))

    def loads(self, path):
        return pack_unpack.deserialize(yaml.safe_load(path))
