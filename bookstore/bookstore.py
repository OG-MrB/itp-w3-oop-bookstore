class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.allbooks = []
        
    def get_books(self):
        return self.allbooks
        
    def add_book(self,book):
        self.allbooks.append(book)
        
    def search_books(self, title=None, author=None):
        book_list = []
        if title:
            for book in self.allbooks:
                if title.lower() in book.title.lower():
                    book_list.append(book)
            return book_list
        if author:
            for book in self.allbooks:
                if author ==  book.author:
                    book_list.append(book)
            return book_list

class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
        
    def get_books(self):
        return self.books
# poe = Author('Edgar Allan Poe', 'US')
# store.search_books(title='raven', author=poe


class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.books.append(self)
    
        
