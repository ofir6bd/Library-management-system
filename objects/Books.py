class Books(object):
    """
    This class is used to keep record of books library
    """
    book_types_opt = ['1', '2', '3']
    books_list = []

    def __init__(self, book_id, name, author, year_published, book_type, amount):
        self.__book_id = book_id
        self.__name = name
        self.__author = author
        self.__year_published = year_published
        self.__book_type = book_type
        self.__amount = amount

    # This magic method returns the string representation of the object
    def __str__(self):
        return f'{self.__book_id}, {self.__name}, {self.__author}, {self.__year_published}, {self.__book_type}, {self.__amount}'

    @classmethod
    def set_books_list(cls, tmp_books_list):
        cls.books_list = tmp_books_list

    # This method return the attributes of an object of this class
    def getObjAtt(self):
        return self.__book_id, self.__name, self.__author, self.__year_published, self.__book_type, self.__amount

    # This methode raise and reduce the amount of a book in +-1 when loan or return a book
    def setAmount(self, val):
        self.__amount += val

    # The following methods getting single attributes value
    def getBookAmount(self):
        return self.__amount

    def getBookId(self):
        return self.__book_id

    def getBookType(self):
        return self.__book_type

    def getBookName(self):
        return self.__name
