# 14. [IGA] Understanding Magic Dunder Methods
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
       return self.title + "By " + self.author

bok= Book("Lord of the rings ", "Tolkin ")
print(bok)
