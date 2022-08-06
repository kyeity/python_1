class Book:
    genre: str = None
    title = None
    author = None

    def __init__(self, title: str,  genre: str, author: str):
        self.title = title
        self.genre = genre
        self.author = author

    def __repr__(self):
        return f'{self.title}, {self.genre}, {self.author}'


class Reader:
    full_name = None
    reader_ticket_number = None
    birthday = None
    number = None
    reader_books = []

    def __init__(self, full_name: str, reader_ticket_number: int, birthday: str, number: int):
        self.full_name = full_name
        self.reader_ticket_number = reader_ticket_number
        self.birthday = birthday
        self.number = number
        self.reader_books = []

    def __repr__(self):
        return f'{self.full_name}, {self.reader_ticket_number}, {self.birthday}, {self.number}'

    # def take_book(self, reader, book: Book):
    #     self.reader_books.append(reader, book.title)


class Library:
    address = None
    phone_number = None
    books = []
    readers = []

    def __init__(self):
        self.books = []
        self.readers = []

    def __str__(self) -> str:
        return str(self.books) + str(self.readers)

    def add_book(self, book: Book):
        self.books.append(book.title)

    def remove_book(self, book: Book):
        self.books.remove(book.title)

    def add_readers(self, reader: Reader):
        self.readers.append(reader.full_name)

    def remove_readers(self, reader: Reader):
        self.readers.remove(reader.full_name)

    def take_book(self, reader: Reader, book: Book):
        Reader.reader_books.append([reader.full_name, book.title])
        self.books.remove(book.title)
        y = []
        for i in Reader.reader_books:
            book_list = tuple(i)
            if reader.full_name in i:
                list_book = book_list[1]
                y.append(list_book)
        return f'{reader.full_name} взяв книги: {y}'

    def return_book(self, reader: Reader, book: Book):
        self.books.append(book.title)
        # Reader.reader_books.remove([reader.full_name, book.title])
        y = []
        for i in Reader.reader_books:
            book_list = tuple(i)
            if reader.full_name in i:
                list_book = book_list[1]
                y.append(list_book)
        Reader.reader_books.remove([reader.full_name, book.title])
        return f'{reader.full_name} повернув книги: {y}'


if __name__ == '__main__':
    book1 = Book('Оно', 'Ужасы', 'Кинг')
    book2 = Book('Оно2', 'Ужасы', 'Кинг')
    book3 = Book('Оно3', 'Ужасы', 'Кинг')
    book4 = Book('Шерлок Холмс', 'Детектив', 'Дойль')
    book5 = Book('Айвенго', 'Роман', 'Вальтер Скотт')
    book6 = Book('Пролетая над гнездом кукушки', 'Драмма', 'Кизи')
    book7 = Book('Оно4', 'Ужасы', 'Кинг')

    reader1 = Reader('Мирослав', 1, '26.08.97', 12345)
    reader2 = Reader('Саша', 2, '26.08.97', 56789)
    reader3 = Reader('Вова', 3, '26.08.97', 13579)
    reader4 = Reader('Игорь', 4, '26.08.97', 24680)
    library = Library()
    readers_books = Reader.reader_books

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
    library.add_book(book6)
    library.add_book(book7)

    library.add_readers(reader1)
    library.add_readers(reader2)
    library.add_readers(reader3)
    library.add_readers(reader4)

    print(library)

    # library.remove_book(book1)

    print(library)
    print('----')
    print(library.take_book(reader1, book1))

    print(Reader.reader_books)
    print(library)


    print(library.take_book(reader1, book6))
    print(Reader.reader_books)
    print(library)
    print()
    print(library.take_book(reader2, book5))
    print(library.take_book(reader2, book4))
    print(Reader.reader_books)
    print(library)
    print(library.return_book(reader1, book6))
    print(library.return_book(reader1, book1))
    print(library)
    print(Reader.reader_books)
