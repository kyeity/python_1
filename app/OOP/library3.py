class Book:

    genre: str = None
    title: str = None
    author: str = None

    def __init__(self, genre: str, title: str, author: str):
        self.genre = genre
        self.title = title
        self.author = author

    def __str__(self):
        return f'Genre: {self.genre}, title: {self.title}, author: {self.author}'

    def __eq__(self, other):
        return self.genre == other.genre and self.title == other.title and self.author == other.author

class Reader:
    books: list[Book] = []
    name = None
    id = None
    date_of_birth = None
    phone = None

    def __init__(self, name: str, id: str, date_of_birth: str, phone: str):
        self.name = name
        self.id = id
        self.date_of_birth = date_of_birth
        self.phone = phone

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f'Name: {self.name}, ID_{self.id}'

class Library():
    library_number: list= []
    library_books: list[Book] = []
    readers_books: list[Book] = []
    library_readers: list[Reader] = []
    library_amount: int = 0
    adress: str = None
    phone: str = None

    def __init__(self, adress: str, phone: str, books: list[Book], readers: list[Reader]):
        self.adress = adress
        self.phone = phone
        self.books = books
        self.readers = readers
        self.library_books.extend(books)
        self.library_readers.extend(readers)

    def takeBook(self, book: Book, reader: Reader):
        if book in self.library_books and reader in self.library_readers:
            self.readers_books.extend(book)
            self.library_books.remove(book)
            reader.books.extend(book)
            return f'{reader.name} took book {book.title}'
        else:
            return f'There is no book {book.title} in Library'


    def returnBook(self, book: Book, reader: Reader):
        reader.books.remove(book)
        self.library_books.extend(book)
        return f'{reader.name} returned book {book.title}'

    def showthebooks(self, book: Book):
        return f'{self.library_books(book)}'

#if __name__ == '__main__':
    #Library()

firstlistofbooks = Book('comedy', 'Lol', 'Author_of_comedy')
secondlistofbooks = Book('drama', 'cry', 'Author_of_drama')
thirdlistofbooks = Book('science', 'NASA', 'Author_of_science')

firstreader = Reader('Ivan', '001', '20.11.1980', '+380981231231')
secondreader = Reader('Ryan', '002', '21.12.1981', '+380981231221')
thirdreader = Reader('James', '007', '22.10.1982', '+380981231241')
#Library.takeBook()

#show = Library.takeBook('comedy', 'Lol', 'Author_of_comedy')



print('-------------------')

#print(Library.takeBook('Lol','lol'))

print('-------------------')

