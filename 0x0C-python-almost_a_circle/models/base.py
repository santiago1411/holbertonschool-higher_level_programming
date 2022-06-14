#!/usr/bin/python3
"""base
"""
import json


class Base:
    """Base of the other shapes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string to file"""

        filename = cls.__name__ + ".json"
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
        """

        str_list = []
        if json_string is None or json_string == "":
            return str_list
        str_list = json.loads(json_string)
        return str_list

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attrs already set
        """

        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        if cls.__name__ == "Square":
            temp = cls(1)
        # update temp with obj func update()
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        """

        res = []
        with open(cls.__name__ + ".json", mode="w") as read_file:
            file2 = read_file.read()
        # Converting str to list
        text = cls.from_json_string(file2)
        for item in text:
            # Formatting dicts into str format
            if type(item) == dict:
                res.append(cls.create(**item))
            else:
                res.append(item)
        return res
