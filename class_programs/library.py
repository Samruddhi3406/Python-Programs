class library:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        print("Book Title:",self.title)
        print("Book Author:",self.author)
        print("Book Price:",self.price)

l1=library("Pyhton Basics","John",500)

l1.display()