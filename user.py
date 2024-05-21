
class User:
    
    def __init__(self, name, library_id):
        self.name = name
        self.__library_id = library_id
        self.borrowed_books = [] 


    def name(self):
        return self.name
    
    def get_library_id(self):
        return self.__library_id  
    
    def add_borrowed_books(self, book):
        self.borrowed_books.append(book)
    
    def __str__(self):
        return "User: "+str(self.name)+", Library ID: "+str(self.__library_id)
    
    def __repr__(self):
        return str(self)