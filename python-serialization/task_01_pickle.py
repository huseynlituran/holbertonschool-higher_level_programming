#!/usr/bin/python3
"""
This module contains a custom class for serialization using pickle.
"""
import pickle


class CustomObject:
    """
    A custom class that can be serialized and deserialized using pickle.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes the CustomObject instance.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the object's attributes to stdout in a specific format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance of the object using pickle.
        Returns None if an exception occurs.
        """
        try:
            # 'wb' = Write Binary (Binar Yazmaq)
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an instance of CustomObject from a file using pickle.
        Returns None if an exception occurs.
        """
        try:
            # 'rb' = Read Binary (Binar Oxumaq)
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            return None
