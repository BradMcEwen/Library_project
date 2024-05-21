from genre import Genre

class Book(Genre):

    def __init__(self, isbn, title, author, publication_date, genre_name, genre_category):
        super().__init__(genre_name, genre_category)
        self.__isbn = isbn 
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.availability_status = True 
    
    def get_title(self):
        return self.title
    
    def get_author_name(self):  
        return self.author()  
    
    def get_isbn(self):
        return self.__isbn
    
    def get_publication_date(self):
        return self.publication_date

    def is_available(self):
        return self.availability_status
    
    def set_is_available(self, availability):
        self.availability_status = availability
    
    def checkout_book(self): 
        if self.is_available():
            self.availability_status = False
            return True
        return False
    
    def return_book(self): 
        self.availability_status = True 
    
    def __str__(self):
        return f"ISBN: {self.get_isbn()}\nTitle: {self.get_title()}\nAuthor: {self.get_author_name()}\nPublication Date: {self.get_publication_date()}\nGenre Name: {self.genre_name}\nGenre Category: {self.genre_category}"

    def __repr__(self):
        return str(self)

