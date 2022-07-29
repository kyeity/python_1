class Book:

    genre = None
    title = None
    author = None

    def __init__(self, genre: str, title: str, author: str):
        self.genre = genre
        self.title = title
        self.author = author

    def __str__(self):
        return f'{self.genre}, {self.title}, {self.author}'

class Reader:
    name = None
    id = None
    date_of_birth = None
    phone = None

    def __init__(self, name: str, id: str, date_of_birth: str, phone: str):
        self.name = name
        self.id = id
        self.date_of_birth = date_of_birth
        self.phone = phone

    def __str__(self):
        return f'{self.name}, ID_{self.id}, {self.date_of_birth}, {self.phone}'

class Library (Book, Reader):
    adress = None

    def __init__(self, genre: str, title: str, author: str, name: str, id: str, date_of_birth: str, phone: str, adress: str):
        self.genre = genre
        self.title = title
        self.author = author
        self.name = name
        self.id = id
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.adress = adress
        self.books = genre + title + author

    def __str__(self):
        return f'{self.genre}, {self.title}, {self.author}, {self.name}, {self.id}, {self.date_of_birth}, {self.phone}, {self.adress}'

    def takeBook(self):
        pass

    def returnBook(self):
        pass

Book.title = ['basic', 'python', 'C#', 'C++']
#Book.title.append('x-=-')
books = Book.title
books.append('+ one_more_book')
books = ', '.join(books)
#bktl = ', '.join(['basic', 'python', 'C#', 'C++'])
#lib = Library('readername', 'readerid', ['basic', 'python', 'C#', 'C++'], 'bookauthor', 'bookgenre', 'adress', 'readerdate_of_birth', 'readerphone')

lib = Library('name', 'ID', books, 'author', 'genre', 'adress', 'derdate_of_birth', 'phone')
#Book.title.append('123')


print('{}, {}'.format(Book('genre', 'title', 'author'), Reader('name', 'id', 'birth', 'phone')))
print('-------------------')
print(lib)
print('-------------------')

