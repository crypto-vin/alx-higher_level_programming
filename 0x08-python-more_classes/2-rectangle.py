#!/usr/bin/python3
"""rectangle class

"""
class Rectangle:
    """creates rectangle object"""
    def __init__(self, width=0, height=0):
        """initializes rectangle class

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets width of a rectangle

        """
        return self.__width

    @property
    def height(self):
        """gets height of a rectangle

        """
        return self.__height

    @width.setter
    def width(self, value):
        """sets width of the rectangle

        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """sets height of the rectangle

        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns area of the rectangle

        """
        return self.height * self.width

    def perimeter(self):
        """ returns perimeter of the rectangle

        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * 2) + (self.width * 2)

if __name__ == "__main__":
    Rectangle()

