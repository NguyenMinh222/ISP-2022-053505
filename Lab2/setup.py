from setuptools import setup


setup(name="Serializer",
      version='1.0.0',
      description='JSON, Yaml and Toml serializers',
      author='NguyenMinh222',
      requires=['pytest', 'PyYAML', 'toml'],
      packages=['serializers, console, tests'],
      )