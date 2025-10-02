# Magic Methods = Dunder Methods( double underscore ) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects
#                 We control the behaviours

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}  " #Normally we see the address but now not

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author # if the books have same title and author
#                                                                          return True

    def __lt__(self, other): #less than    gt = greater than
        return self.num_pages < other.num_pages

    def __add__(self, other): return self.num_pages + other.num_pages

    def __contains__(self, keyword): return keyword in self.title

    def __getitem__(self, key):
        if key == "title":
            return self.title

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 223)
book3 = Book("The Lion, The Witch and the Wardrobe", "C.S Lewis", 172)

print(book1) #Hobbit by J.R.R Tolkien
print(book1 == book2) #False
print(book2 < book3)
print(book2 + book3) #95
print("Lion" in book3) #True
print(book1.title)