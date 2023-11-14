#!/usr/bin/python3
"""class Base module"""
import json


class Base:
    """class for base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize instance attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string reprentation of object"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns list of the JSON string representation"""
        if not json_string:
            return '[]'
        if not isinstance(json_string, str):
            raise TypeError('json_string must be a string')
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string to file"""
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                serialized = [inst.to_dictionary() for inst in list_objs]
                jsonfile.write(cls.to_json_string(serialized))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            obj = cls(2, 1)
        else:
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = cls.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
