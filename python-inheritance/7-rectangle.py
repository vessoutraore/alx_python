#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry
class BaseGeometryMetaClass(type):
    """
    A metaclass for BAse geometry
    """
    def __dir__(cls)->None:
        """
        A function define to remove the __init_subclass__ from dir
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
class Rectangle(BaseGeometry, metaclass=BaseGeometryMetaClass):
    """
    Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).
    """
    def __init__(self, width, height):
        """
        initialaizatio function for base geometry
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
    
    def __str__(self):
        """
        THIS mETHOD CONVERT THE OBJECT TO A READABLE STRING
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        This method return the result of width * height
        """
        return self.__width*self.__height
