# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
# Benefit: Add additional logic when read, write or delete attributes
# Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property  #getter method to read
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter #setter method to write
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle = Rectangle(3, 4)

rectangle.width = 2

# del rectangle.height to delete

print(rectangle.width) # 2.0cm
print(rectangle._height) # 4   internal value