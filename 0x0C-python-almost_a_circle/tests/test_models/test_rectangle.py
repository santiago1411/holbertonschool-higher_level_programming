#!/usr/bin/python3

"""
Module for Rectangle class.
"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method, initialize a Rectangle"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""

        return self.__width

    @property
    def height(self):
        """Getter for height"""

        return self.__height

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @property
    def y(self):
        """Getter for y"""

        return self.__y

    @width.setter
    def width(self, value):
        """Setter for width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter for x"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter for y."""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a rectangle"""

        return self.__width * self.__height

    def display(self):
        """Print in stdo the Rectangle"""

        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Return string representation of class."""

        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update the class rectangle"""

        if args:
            for i, element in enumerate(args):
                if i == 0:
                    self.id = element
                elif i == 1:
                    self.__width = element
                elif i == 2:
                    self.__height = element
                elif i == 3:
                    self.__x = element
                elif i == 4:
                    self.__y = element
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary"""
        dic = {'id': self.id, 'width': self.width,
               'height': self.height, 'x': self.x, 'y': self.y}
        return dic
