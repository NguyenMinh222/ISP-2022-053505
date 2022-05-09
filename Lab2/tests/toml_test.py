import os

from serializers import to_ml as toml
from tests import ser_entities


def test_dump_load_object():
    serial = toml.Toml()
    file = open("example.json", "w")
    serial.dump(ser_entities.boozer_object, file.name)
    obj = serial.load(file.name)
    file.close()
    os.remove(os.path.abspath(file.name))
    assert obj.name == 'Ivan'


def test_dump_loads():
    serial = toml.Toml()
    obj = serial.loads(serial.dumps(ser_entities.boozer_object))
    assert str(type(obj)) == str(type(ser_entities.boozer_object))


def test_dump_load2():
    serial = toml.Toml()
    file = open("example.json", "w")
    serial.dump(ser_entities.mul, file.name)
    func = serial.load(file.name)
    file.close()
    os.remove(os.path.abspath(file.name))
    assert 2 * 3 == func(2, 3)
