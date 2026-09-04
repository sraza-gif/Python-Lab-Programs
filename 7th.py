# Library Management System using inheritance and polymorphism

class LibraryItem:
    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title
        self.issued = False

    def issue(self):
        if not self.issued:
            self.issued = True
            print(self.title, "has been issued.")
        else:
            print(self.title, "is already issued.")

    def return_item(self):
        if self.issued:
            self.issued = False
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not issued.")

    def display(self):
        print("ID:", self.item_id)
        print("Title:", self.title)


class Book(LibraryItem):
    def display(self):
        print("Type: Book")
        super().display()


class Magazine(LibraryItem):
    def display(self):
        print("Type: Magazine")
        super().display()


class Journal(LibraryItem):
    def display(self):
        print("Type: Journal")
        super().display()


# Creating objects
book = Book(101, "Python Programming")
magazine = Magazine(102, "Technology Today")
journal = Journal(103, "Computer Science Journal")

items = [book, magazine, journal]

for item in items:
    item.display()
    item.issue()
    item.return_item()
    print()