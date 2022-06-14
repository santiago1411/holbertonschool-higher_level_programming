#!/usr/bin/python3
"""rectangle
"""


from models.base import Base


class Rectangle(Base):
    """Inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""

        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""

        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """Print in stdo the Rectangle"""

        for i in range(self.y):
            print()
        for i in range(self.__height):
            print(" " * self.x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Method that returns the rectangle string representation"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates the values of the Rectangle instance"""

        if len(args) == 0:
            for llave in kwargs:
                setattr(self, llave, kwargs[llave])
        else:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]

    def to_dictionary(self):
        """Returns dict representation
        """
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.width}
