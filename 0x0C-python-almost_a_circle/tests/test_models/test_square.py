#!/usr/bin/python3
"""module for square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String of class"""

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
        """Update method for Square"""

        if args:
            for i, element in enumerate(args):
                if i == 0:
                    self.id = element
                elif i == 1:
                    self.size = element
                elif i == 2:
                    self.x = element
                elif i == 3:
                    self.y = element
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary"""
        dic = {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
        return dic
