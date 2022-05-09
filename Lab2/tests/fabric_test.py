from serializers import js_on as json, ya_ml as yaml, to_ml as toml
from serializers.fabric_serialize import *


def get_serializer(creator: CreateSerializer()):
    return creator.create()


def test_json_creator():
    serializze = get_serializer(CreateJson())
    print(type(serializze))
    assert isinstance(serializze, json.Json)


def test_yaml_creator():
    serializze = get_serializer(CreateYaml())
    print(type(serializze))
    assert isinstance(serializze, yaml.Yaml)


def test_toml_creator():
    serializze = get_serializer(CreateToml())
    print(type(serializze))
    assert isinstance(serializze, toml.Toml)
