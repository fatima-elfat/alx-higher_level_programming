#!/usr/bin/python3
"""
the modules of class Square, inherits from Rectangle.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines class  Square.

    Attributes:
        size
    Inherited Attributes:
        id
        __weight
        __height
        __x
        __y
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Calls super will use the logic of the __init__
        of the Rectangle class. The width and height must
        be assigned to the value of size.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        Getter function for size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter function for size.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Overrides the __str__ method and prints
        [Square] (<id>) <x>/<y> - <size>.
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__,
            self.id,
            self.__x,
            self.__y,
            self.size
            )

    def update(self, *args, **kwargs):
        """
        Assigns and updates the Rectangle.

        Arguments:
            *args : the attribute values.
            **kwargs : the key/value of attributes.
        """
        if args and len(args) != 0:
            i = 0
            for a in args:
                if i == 0:
                    if a is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
                i += 1
        elif kwargs and len(kwargs) != 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Prints the dictionary representation of a Square.
        """
        dct = {}
        dct["id"] = self.id
        dct["size"] = self.size
        dct["x"] = self.x
        dct["y"] = self.y
        return dct
