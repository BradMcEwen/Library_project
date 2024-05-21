class Author:
    def __init__(self, author_name, biography):
        self.author_name = author_name
        self.biography = biography

    def get_author(self):
        return self.author_name
    
    def author_biography(self):
        return self.biography
    
    def __str__(self):
        return f"Author: {self.author_name}, Biography: {self.biography}"
    
    def __repr__(self):
        return str(self)