#!/usr/bin/python3
"""Class Student"""


class Student:
    """
    Def instance atrributes of class student
    Instances publics of attributes first_name, last_name, age
    self espicify  methods and atributes
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (type(attrs) is None):
            return(attrs.__dict__)
