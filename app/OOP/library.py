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

    def __init__(self, readername: str, readerid: str, booktitle: str, bookauthor: str,bookgenre: str, adress: str, readerdate_of_birth: str, readerphone: str):
        self.bk = Book(bookgenre, bookauthor, booktitle)
        self.rd = Reader(readername, readerid, readerdate_of_birth, readerphone)
        self.adress = adress

    def __str__(self):
        return f'{self.rd}, {self.bk}, {self.adress}'

    def takeBook(self):
        pass

    def returnBook(self):
        pass


Book.title = ['basic', 'python', 'C#', 'C++']
bktl = Book.title
bktl = ', '.join(['basic', 'python', 'C#', 'C++'])
#lib = Library('readername', 'readerid', ['basic', 'python', 'C#', 'C++'], 'bookauthor', 'bookgenre', 'adress', 'readerdate_of_birth', 'readerphone')

lib = Library('readername', 'readerid', bktl,'bookauthor', 'bookgenre', 'adress', 'readerdate_of_birth', 'readerphone')
#Book.title.append('123')


print('{}, {}'.format(Book('genre', 'title', 'author'), Reader('name', 'id', 'birth', 'phone')))
print('-------------------')
print(lib)
print('-------------------')

