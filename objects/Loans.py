class Loans(object):
    """
    This class is used to keep record of loans in the library
    """
    loans_list = []

    def __init__(self, cust_id, book_id, loan_date, return_date):
        self.__cust_id = cust_id
        self.__book_id = book_id
        self.__loan_date = loan_date
        self.__return_date = return_date

    # This magic method returns the string representation of the object
    def __str__(self):
        return f'{self.__cust_id}, {self.__book_id}, {self.__loan_date}, {self.__return_date}'

    @classmethod
    def set_loans_list(cls, tmp_loans_list):
        cls.loans_list = tmp_loans_list

    # This method return the attributes of an object of this class
    def getObjAtt(self):
        return self.__cust_id, self.__book_id, self.__loan_date, self.__return_date

    # The following methods just getting single attributes value
    def getCustId(self):
        return self.__cust_id

    def getBookId(self):
        return self.__book_id

    def getReturnDate(self):
        return self.__return_date
