class Serializer:

    def dump(self, obj: any, filename: str):
        """Serializing Python object into file"""
        """Create a new file if the specified file is not found"""
        file = open(filename, 'w')
        file.write(self.dumps(obj))

    def dumps(self, obj: any) -> str:
        """Serializing Python object to string"""

    def load(self, filename: str):
        """Deserializing Python object from file"""
        file = open(filename, 'r')
        return self.loads(file.read())

    def loads(self, string: str) -> any:
        """Deserializing Python object from string"""
