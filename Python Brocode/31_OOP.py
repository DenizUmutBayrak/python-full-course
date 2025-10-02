#object = A bundle of related attributes (variables) and methods (function)
#Ex = phone, cup, book
#You need  a class to create many objects

#class = (blueprint) used to design the structure and layout of an object

class Car:

    num_of_cars = 0 #class variable = shared among all instance of a class
               #defined outside  the constructor
               #Allow you to share data among all objects created from class

    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        Car.num_of_cars += 1

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)

print(car1.model) #Mustang
print(car2  .year) #2025
print(car1.num_of_cars) #4