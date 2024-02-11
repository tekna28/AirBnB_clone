#!/usr/bin/python3
"""Defines FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Class that stores and retrieves data."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method that returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Method that sets in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Method that serializes __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Method that deserializes the JSON file __file_path to __objects."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
