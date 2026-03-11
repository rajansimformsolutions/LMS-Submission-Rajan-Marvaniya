class library:
    def __init__(self, books):
        self.books = books

    def display_books(self):
        if len(self.books) == 0:
            print("no books avaible in library.")
        else:
            print("books avaible in the library:")
            for book in self.books:
                print("-", book)

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print("you borrowed:", book_name)
        else:
            print("Sorry, this book is not available.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print("you returned:", book_name)

book_list = ["Python Basics", "Data Structures", "Machine Learning", "AI Fundamentals"]
library = library(book_list)

while True:
        print("\n------ Library Menu ------")
        print("1. Display Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        choice = int(input("enter your choice:"))

        if choice == 1:
            library.display_books()

        elif choice == 2:
            book = input("Enter the book name to borrow: ")
            library.borrow_book(book)
    
        elif choice == 3:
            book = input("enter the book name to borrow:")
            library.borrow_book(book)

        elif choice == 4:
            print("exiting the book name to return:")
            break
         
        else:
            print("invalid choise. try again.")