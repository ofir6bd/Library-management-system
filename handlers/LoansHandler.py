from objects.Customers import Customers
from objects.Books import Books
from objects.Loans import Loans
from datetime import date, timedelta
from tabulate import tabulate

"""
This Module defines the loans functions
"""


def loan_book():
    # Request and validate before object creation
    desired_customer = check_cust_exists()
    if desired_customer is None:
        return
    book_type_found, desired_book = book_availability()
    if book_type_found is None or desired_book is None:
        return
    late_loans_on_cust = check_late_loans(desired_customer.getCustomerId())
    if late_loans_on_cust is None:
        return

    # Validation passed, creating a loan object and updating book amount and borrowed books on customer
    Books.setAmount(desired_book, -1)
    Customers.setBorrowedBooks(desired_customer, 1)
    days_to_return = get_return_date(book_type_found)
    new_loan = Loans(desired_customer.getCustomerId(), desired_book.getBookId(), date.today(),
                     date.today() + timedelta(days=days_to_return))
    Loans.loans_list.append(new_loan)
    print(
        f'Loan details: Customer ID: "{desired_customer.getCustomerId()}", Book ID: "{desired_book.getBookId()}" were added to the library loans list\n')
    return


def check_cust_exists():
    desired_customer_id = input('Please enter the customer ID:')
    for customer in Customers.customers_list:
        if desired_customer_id == customer.getCustomerId():
            return customer
    print(f'Customer ID: "{desired_customer_id}" was not found in library lists\n')
    return


# To check if the book exists and the amount
def book_availability():
    desired_book_id = input('Please enter the book ID:')
    for book in Books.books_list:
        if desired_book_id == book.getBookId():
            if book.getBookAmount() == 0:
                print(f'The book ID: "{desired_book_id}" exists in the library lists, but the amount is 0, so no book available at the moment\n')
                return None, None
            else:
                return book.getBookType(), book
    print(f'Book name:"{desired_book_id}" was not found in library lists\n')
    return None, None


# Converting book type to days to return
def get_return_date(book_type):
    dic = {'1': '10', '2': '5', '3': '2'}
    return int(dic[book_type])


def check_late_loans(desired_customer):
    late_Loans_list = []
    for loan in Loans.loans_list:
        if desired_customer == loan.getCustId():
            if loan.getReturnDate() < date.today():
                late_Loans_list.append(loan)
    if len(late_Loans_list) == 0:
        return True
    else:
        print(f'The customer cannot loan another book since he have {len(late_Loans_list)} book overdue!!!')
        print('       Customer ID,Book name,Loan Date,Return Date')
        for i in range(1, len(late_Loans_list) + 1):
            print(f'    {i}. {late_Loans_list[i - 1]}')
        print()
        return None


def return_book():
    return_customer_id = input('Please enter the customer ID:')
    return_book_id = input('Please enter the book ID to return:')
    # To check if loan exists per customer ID and book ID
    for i in range(len(Loans.loans_list)):
        if return_customer_id == Loans.loans_list[i].getCustId() and return_book_id == Loans.loans_list[i].getBookId():
            Loans.loans_list.pop(i)
            print(
                f'Loans details: Customer ID: "{return_customer_id}", Book ID: "{return_book_id}", were removed from the library loans list\n')
            # Raising book amount by 1 and reducing borrowed books on customer by 1
            for book in Books.books_list:
                if return_book_id == book.getBookId():
                    Books.setAmount(book, 1)
            for customer in Customers.customers_list:
                if return_customer_id == customer.getCustomerId():
                    Customers.setBorrowedBooks(customer, -1)
            return
    print(
        f'This Loan: Customer ID "{return_customer_id}" and Book ID "{return_book_id}" were not found in library loans list\n')
    return


def display_all_loans():
    if len(Loans.loans_list) == 0:
        print('No loans in the library at the moment\n')
        return
    all_loans = []
    for i in range(len(Loans.loans_list)):
        ind = (i + 1,)
        all_loans.append(ind + Loans.loans_list[i].getObjAtt())
    print('The list of the loans are: ')
    print(tabulate(all_loans, headers=['Index', 'Customer ID', 'Book ID', 'Loan Date', 'Return Date']))
    print()


def display_late_loans():
    late_Loans_list = []
    for loan in Loans.loans_list:
        if loan.getReturnDate() < date.today():
            late_Loans_list.append(loan)
    if len(late_Loans_list) == 0:
        print('no late loans found at the moment\n')
    else:
        late_loans_str_list = []
        for i in range(len(late_Loans_list)):
            ind = (i + 1,)
            late_loans_str_list.append(ind + late_Loans_list[i].getObjAtt())
        print('The list of the late loans are: ')
        print(tabulate(late_loans_str_list, headers=['Index', 'Customer ID', 'Book ID', 'Loan Date', 'Return Date']))
        print()