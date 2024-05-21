from book import Book
from user import User
from genre import Genre
from author import Author
import re


class Library:

    def __init__(self):
        self.books = {} 
        self.loaned_books = {}
        self.users = {}
        self.authors = {}
        self.genres = [] 

    def add_book(self): 
        isbn = input("Enter the last 4 digits of the isbn: ")
        valid_isbn = re.match(r"\d{4}", isbn) 
        if valid_isbn:
            print("Valid ISBN")
            title = input("Enter book title: ").upper()
            author_first_name = input("Enter book author first name: ").title()
            author_last_name = input("Enter book author last name: ").title()
            author_name = author_first_name + " " + author_last_name
            biography = input("Enter a short bio about the author: ").lower()
            publication_date = input('Enter the publication date in this form "YEAR-MM-DD" : ')
            valid_pub_date = re.match(r"\d{4}-\d{2}-\d{2}", publication_date) 
            if valid_pub_date:
                print("Valid publication date")
                genre_name = input("Enter the genre you would like to add: ").title()
                genre_category = input("Enter a genre category (for example: Drama, Poetry, Fiction, )").title()
                print()
            else:
                print("Invalid publication date")
                self.add_book()
        else:
            print("Invalid ISBN")
            self.add_book()
        author = Author(author_name, biography)
        self.authors[author_name] = biography
        genre = Genre(genre_name, genre_category)
        self.genres.append(genre)
        book = Book(isbn, title, author, publication_date, genre_name)
        self.books[isbn] = book
        print(f"Book added successfully: \n{book}")

    def checkout_book(self): 
        user = input("Do you have a library ID? Enter yes or no? ").lower()
        if user == "no":
            print("No problem, lets get you setup with one so you can check books out!")
            self.add_user()
        elif user == "yes":
            print("Welcome back!")
            isbn = input('Enter the 4 digit isbn of the book you would like to check out: ')
            verified_isbn = re.match(r"\d{4}", isbn) 
            if verified_isbn:
                print("Valid ISBN")
                library_id = input("Enter your 6 digit library ID: ")
                if library_id.isdigit():
                    user_id = int(library_id)
                    if isbn in self.books:
                        book = self.books[isbn]
                        print()
                        print(f"Book found: {book}") 
                        if book.is_available():
                            print("Book is available for checkout") 
                            print()
                            if user: 
                                book.set_is_available(False)
                                self.loaned_books[isbn] = user_id
                                user = self.users.get(user_id)
                                if user:
                                    user.add_borrowed_books(book)
                                    print(f"Book '{book.title}' checked out to {user.name}")
                                    print()
                            else:
                                print("That user couldn't be found") 
                        else:
                            print("That book is unavailable")
                    else:
                        print("No book found by that ISBN")
                else:
                    print("Please enter valid ID")
            else:
                print("Invalid ISBN")
        else:
            print("Invalid input")

    def return_book(self):
        isbn = input("Enter the ISBN of the book to return: ")
        valid_isbn = re.match(r"\d{4}", isbn) 
        if valid_isbn:
            print("Valid ISBN")
            if isbn in self.books and isbn in self.loaned_books:
                title = self.books[isbn].get_title() 
                self.books[isbn].return_book()
                del self.loaned_books[isbn]
                print(f"Book '{title}' was returned")
                print()
            else:
                print("No book found by that information")
        else:
            print("Invalid ISBN")

    def search_for_book(self): 
        isbn = input('Enter the 4 digit isbn of the book you would like: ')
        verified_isbn = re.match(r"\d{4}", isbn) 
        if verified_isbn:
            print("Valid ISBN")
            book = self.books.get(isbn)
            if book:
                print()
                print("Here is the book that matches the ISBN you entered:")
                print(book)
                print()
            else:
                print("We dont have a book with that isbn.")   
                self.search_for_book()
        else:
            print("Invalid Input")
            self.search_for_book()

    def display_books(self):
        print("Here is a list of all the books in the library:")
        for isbn, book in self.books.items():
            print(book)


    def add_user(self):
        user = input("What is your name?").title()
        if user not in self.users:
            library_id = input("Please enter a 6 digit code to create a library ID: ")
            valid_id = re.match(r"\d{6}")
            if valid_id:
                print("Valid Input")
                user = User(user, library_id)
                self.users[library_id] = user
                print(f"{user.name} was added into system with ID of {valid_id}")
                print()
            else:
                print("Invalid Input")
        else:
            print("There is already a user under that name!")
            self.add_user()

    def view_user(self): 
        library_id = input("Enter the 6 digit library ID of the user you would like to view details on: ")
        user = self.users.get(int(library_id))
        if user:
            print("Here are the user's details: ")
            print(user)
            print()
        else:
            print("The library id you entered does not match any of the user's.")
            self.view_user()
    
    def display_users(self): 
        print("Here are the details of all users: ")
        for user in self.users.values():
            print(user)

    def borrowed_books(self): 
        library_id = input("Enter the 6 digit library id of the user you would like to view borrowed books for: ")
        library_id = int(library_id)
        user = self.users.get(library_id)
        if user:
            print(f"Here is a list of borrowed books by {user.name}: ")
            for book in user.borrowed_books:
                print(book.title)
        else:
            print("The library id you entered does not match any of the users.")
            self.borrowed_books()

    def add_author(self):
        author = input("Enter book author's full name: ").title()
        biography = input("Enter a short bio about the author: ").lower()
        author = Author(author, biography)
        self.authors[author] = biography
        print()
        print(f"{author} was added")

    def view_author(self):
        author = input("Enter the full name of the author you'd like to view: ").title()
        for key, value in self.authors.items():
            if key == author:
                print()
                print(f'Author: {author}, Biography: {value}')
                break
            else:
                print("Input does not match authors on file")
                self.view_author()

    def display_authors(self):
        print("Here is the list of all authors on file: ")
        for author in self.authors:
            print(author)

    def add_genre(self):
        genre_name = input("Enter the name of the genre you would like to add: ").title()
        genre_category = input("Enter a genre category (for example: Drama, Poetry, Fiction, )").title()
        genre = Genre(genre_name, genre_category)
        self.genres.append(genre)
        print()
        print(f"{genre_name} was added to the genre list in the {genre_category} category!")

    def view_genre(self):
        print("Here is a list of genre's with the assigned category names: ")
        for genre in self.genres:
            print(f"Genre: {genre.genre_name} |  Category: {genre.genre_category}")
            
    def display_genres(self): 
        print("Here is the list of genres: ")
        for genre in self.genres:
            print(genre.genre_name)