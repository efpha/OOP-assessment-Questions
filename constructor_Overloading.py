# constructor_Overloading
class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width is not None else length  # Assume square if width is not provided

    def area(self):
        return self.length * self.width

square = Rectangle(5)
rectangle = Rectangle(5, 10)
print(square.area())     
print(rectangle.area())  
