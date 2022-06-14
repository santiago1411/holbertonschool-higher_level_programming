#!/usr/bin/python3
"""square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns formatted information display
        """

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size"""

        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the values of the Rectangle instance"""

        if len(args) == 0:
            for llave in kwargs:
                setattr(self, llave, kwargs[llave])
        else:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

    def to_dictionary(self):
        """return format of a dictionary"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
