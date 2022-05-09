import os
import math
from serializers import js_on as json
from tests import ser_entities


def test_dumps_loads_function():
    serial = json.Json()
    ser = serial.dumps(ser_entities.f)
    func = serial.loads(ser)
    assert isinstance(func(0), float)


def test_dump_load_function():
    serial = json.Json()
    file = open("example.json", "w")
    serial.dump(ser_entities.f, file.name)
    func = serial.load(file.name)
    file.close()
    os.remove(os.path.abspath(file.name))
    assert math.sin(42 * 123 * 1) == func(1)


def test_dump_load_function2():
    serial = json.Json()
    file = open("example.json", "w")
    serial.dump(ser_entities.mul, file.name)
    func = serial.load(file.name)
    file.close()
    os.remove(os.path.abspath(file.name))
    assert 2 * 3 == func(2, 3)


def test_dump_load_object():
    serial = json.Json()
    obj = serial.loads(serial.dumps(ser_entities.boozer_object))
    assert str(type(obj)) == str(type(ser_entities.boozer_object))