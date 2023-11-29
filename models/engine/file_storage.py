#!/usr/bin/python3
""" File Storage Module """

import json
from models.base_model import BaseModel
from models.state import State
# ... import other classes

class FileStorage:
    """ This class manages file storage for your AirBnB clone """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """ Returns a dictionary of models currently in storage.
            If cls is provided, it returns only objects of that class.
        """
        if cls:
            cls_dict = {}
            for key, obj in FileStorage.__objects.items():
                if isinstance(obj, cls):
                    cls_dict[key] = obj
            return cls_dict
        return FileStorage.__objects

    def new(self, obj):
        """ Adds new object to storage dictionary """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ Saves storage dictionary to file """
        with open(FileStorage.__file_path, 'w') as f:
            temp = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(temp, f)

    def reload(self):
        """ Loads storage dictionary from file """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for obj_id, obj_dict in temp.items():
                    cls_name = obj_dict['__class__']
                    cls = globals()[cls_name]
                    self.__objects[obj_id] = cls(**obj_dict)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Deletes obj from __objects if its inside """
        if obj:
            obj_key = f"{type(obj).__name__}.{obj.id}"
            if obj_key in self.__objects:
                del self.__objects[obj_key]
