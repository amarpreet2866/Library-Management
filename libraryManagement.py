# Library Management System by Amarpreet Singh
class Library():
    def __init__(self, list, name):
        self.listOfBooks = list
        self.libraryName = name
        self.lendBook = {}

    def bookDisplay(self):
        print(f"We have the following books in our library: {self.libraryName}")
        for i,book in enumerate(self.listOfBooks):
            print(i+1, book.title())

    def bookLend(self):
        book = input("Enter the name of book: ")
        taker = input("Enter the name of borrower: ")
        book = book.title()
        taker = taker.title()
        if book not in self.lendBook.keys():
            self.lendBook.update({book:taker})
            print(f"You can take the {book} book now.")
        else:
            print(f"The book has taken by {self.lendBook[book]}")
    
    def bookDonate(self):
        donation = input("Enter the name of book you want to Add: ")
        donation = donation.title()
        self.listOfBooks.append(donation)
        print(f"{donation} book is added.")

    def bookReturn(self):
        book = input("Enter the name of book you want to return: ")
        returner = input("Enter the name of Borrower: ")
        book = book.title()
        returner = returner.title()
        if book not in self.lendBook.keys() or returner not in self.lendBook.values():
            print("Either the name of book or the name of returner is wrong. Check it and try again.")
        else:
            self.lendBook.pop(book)
            print(f"The {book} book is returned.")
    pass

if __name__ == "__main__":
    name = input("Enter your name: ")
    libName = input("Enter the name of library: ")
    bookList = input("Enter the name of books. Split them by a comma',': ")
    bookList = bookList.title()
    bookList = bookList.split(",")
    name = Library(bookList , libName.title())    
    print("Welcome to our Library")
    c = "y"
    while c == "y":
        try:
            print("Select to continue\n1.Display all books\n2.Lend a book\n3.Add a book\n4.Return a book")
            opt = int(input("Enter your selection: "))
            if opt == 1:
                name.bookDisplay()
            elif opt == 2:
                name.bookLend()
            elif opt == 3:
                name.bookDonate()
            elif opt == 4:
                name.bookReturn()
            else:
                print("You have entered a wrong input. Please enter the valid input.")
            c = input("Do you want to continue?\nPress y for yes and n for no\nSelect: ")    
        except:
            print("You have entered wrong input.Please enter the valid input.")