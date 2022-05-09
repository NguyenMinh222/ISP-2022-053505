from serializers import s_methods
from serializers import js_on
from serializers import to_ml
from serializers import ya_ml


class CreateSerializer:
    def create(self) -> s_methods.Serializer:
        """Method that creates different types of serializers"""


class CreateJson(CreateSerializer):
    def create(self) -> s_methods.Serializer:
        return js_on.Json()


class CreateYaml(CreateSerializer):
    def create(self) -> s_methods.Serializer:
        return ya_ml.Yaml()


class CreateToml(CreateSerializer):
    def create(self) -> s_methods.Serializer:
        return to_ml.Toml()
