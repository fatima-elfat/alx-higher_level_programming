#!/usr/bin/python3
"""
the module of class Base.
"""


import json
import csv
import turtle


class Base():
    """
    defines class Base
    Attributes:
        __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Assigns id if given otherwise assigns the incremented
        value to the public instance attribute id.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries

        Return: a JSON representation.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Arguments:
            cls : self Class.
            list_objs : a list of instances who inherits of Base.

        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                l_dct = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(l_dct))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Return: JSON representation json_string:
        """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Arguments:
            cls : self Class.
            dictionary : a double pointer to a dictionary.
        Return: the attributes.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                r = cls(1, 1)
            else:
                r = cls(1)
            r.update(**dictionary)
            return r

    @classmethod
    def load_from_file(cls):
        """
        Reads from json,  returns a list of instances,
        the type of these instances depends on cls.

        Arguments:
            cls : self Class.
        Return : alist of instances.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                l_dct = cls.from_json_string(f.read())
            return [cls.create(**a) for a in l_dct]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes in CSV.
        Arguments:
            cls : self Class.
            list_objs : alist of Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Reads from csv and deserializes in CSV.

        Arguments:
            cls : self Class.
        Return: a list of instances.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                reader = csv.DictReader(f, fieldnames=fields)
                l_dct = [dict([key, int(val)] for key, val in a.items())
                         for a in reader]
                return [cls.create(**b) for b in l_dct]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares.
        Arguments
            list_rectangles : the list of Rectangle .
            list_squares : the list of Square.
        this task is to be reviewed by peers.
        """
        drawing = turtle.Turtle()
        drawing.screen.bgcolor("#000000")
        drawing.pensize(3)
        drawing.shape("turtle")
        drawing.color("#eeeeee")
        for r in list_rectangles:
            drawing.showturtle()
            drawing.up()
            drawing.goto(r.x, r.y)
            drawing.down()
            for i in range(2):
                drawing.forward(r.width)
                drawing.left(90)
                drawing.forward(r.height)
                drawing.left(90)
            drawing.hideturtle()
        drawing.color("#ffffff")
        for sq in list_squares:
            drawing.showturtle()
            drawing.up()
            drawing.goto(sq.x, sq.y)
            drawing.down()
            for i in range(2):
                drawing.forward(sq.width)
                drawing.left(90)
                drawing.forward(sq.height)
                drawing.left(90)
            drawing.hideturtle()
        turtle.exitonclick()
