class Customers(object):
    """
    This class is used to keep record of customers
    """
    customers_list = []

    def __init__(self, customer_id, name, city, age, borrowed_books):
        self.__customer_id = customer_id
        self.__name = name
        self.__city = city
        self.__age = age
        self.__borrowed_books = borrowed_books

    # This magic method returns the string representation of the object
    def __str__(self):
        return f'{self.__customer_id}, {self.__name}, {self.__city} , {self.__age}, {self.__borrowed_books}'

    @classmethod
    def set_customers_list(cls, tmp_customers_list):
        cls.customers_list = tmp_customers_list

    # This method return the attributes of an object of this class
    def getObjAtt(self):
        return self.__customer_id, self.__name, self.__city, self.__age, self.__borrowed_books

    # This method is to rais or reduce borrowed books from customer
    def setBorrowedBooks(self, val):
        self.__borrowed_books += val

    # This methods is to get customer attributes
    def getCustomerId(self):
        return self.__customer_id

    def getCustomerName(self):
        return self.__name

    def getCustomerCity(self):
        return self.__city

    def getCustomerAge(self):
        return self.__age

    def getCustomerBorrowedBooks(self):
        return self.__borrowed_books