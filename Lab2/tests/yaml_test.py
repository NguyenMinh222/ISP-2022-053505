import math
import os

from serializers import ya_ml as yaml
from tests import ser_entities


def test_dumps_loads():
    serializze = yaml.Yaml()
    ser = serializze.dumps(ser_entities.f)
    func = serializze.loads(ser)
    assert math.sin(42 * 123 * 0) == func(0)


def test_dump_load():
    serializze = yaml.Yaml()
    file = open("example.yaml", "w")
    serializze.dump(ser_entities.f, file.name)
    func = serializze.load(file.name)
    file.close()
    os.remove(os.path.abspath(file.name))
    assert math.sin(42 * 123 * 1) == func(1)


def test_dump_load2():
    serializze = yaml.Yaml()
    file = open("example.yaml", "w")
    serializze.dump(ser_entities.mul, file.name)
    func = serializze.load(file.name)
    file.close()
    os.remove(os.path.abspath(file.name))
    assert 2 * 3 == func(2, 3)
