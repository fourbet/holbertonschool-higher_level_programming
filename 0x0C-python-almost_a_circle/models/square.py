#!/usr/bin/python3
""" Project: Python - Almost a Circle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ The class Square inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor of the class Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Print method """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """ getter of size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter of size """
        super(Square, type(self)).width.fset(self, value)
        super(Square, type(self)).height.fset(self, value)
        
    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        lists= ("id","size", "x", "y")
        i = 0
        for arg in args:
            if (i > 3):
                break
            if arg is None and i == 0:
                super().__init__()
            else:
                setattr(self, lists[i], arg)
            i += 1
        if kwargs is not None and i == 0:
            for k, v in kwargs.items():
                if k == "id" and v is None:
                    super().__init__()
                else:
                    setattr(self, k, v)

    def to_dictionary(self):
        """ Returns the dictionary representation of a square """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}        
