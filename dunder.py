class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}, Pages: {self.pages}"

    def __repr__(self):
        return f"Book: {self.title}, Pages: {self.pages}"

    def __len__(self):
        return self.pages

# Using the class
b1 = Book("Python Basics", 300)

print(b1)            # Calls __str__ → Book: Python Basics, Pages: 300
print(len(b1))       # Calls __len__ → 300
