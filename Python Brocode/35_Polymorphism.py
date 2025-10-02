#Polymorphism = Greek word that means to "have many form or faces"
#Poly = Many
#Morphe = Form

#Two ways to achieve  polymorphism
#1.Inheritance = An object could be treated of the same type as a parent class
#2.Duck typing = Object must have necessary attributes/methods

class Shape:
    pass

class Circle(Shape):
    pass

class Triangle(Shape):
    pass

class Square(Shape):
    pass

circle = Circle()  #both square and circle