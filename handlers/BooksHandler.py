from handlers.CustomersHandler import insert_customer, display_all_customers, find_customer, check_and_remove_customer
from handlers.LoansHandler import loan_book, return_book, display_all_loans, display_late_loans
from objects.Books import Books
from objects.Loans import Loans
import re
from random import randint
from datetime import date
from tabulate import tabulate

"""
This Module define main and books functions
"""

regex_book_template = re.compile("^[a-zA-Z0-9-\s\.]+$")
regex_name_template = re.compile("^[A-Za-z\.]+(\s[A-Za-z-\.]+)+$")


# Print library menu and get the user choice
def print_library_menu():
    user_choice = input('''============= Library menu =============
            1.Add a new customer
            2.Add a new book
            3.Loan a book
            4.Return a book
            5.Display all books
            6.Display all customers
            7.Display all loans
            8.Display late loans
            9.Find book by name
            10.Find customer by name
            11.Remove book
            12.Remove customer
            13.Exit
        Please enter your choice: 
            ''')
    return user_choice


def deal_user_choice():
    user_choice = ''
    # library menu
    while user_choice != '13':
        user_choice = print_library_menu()
        if user_choice == '1':   # Add a new customer
            insert_customer()
        elif user_choice == '2':    # Add a new book
            insert_book()
        elif user_choice == '3':    # Loan a book
            loan_book()
        elif user_choice == '4':    # Return a book
            return_book()
        elif user_choice == '5':     # Display all books
            display_all_books()
        elif user_choice == '6':    # Display all customers
            display_all_customers()
        elif user_choice == '7':     # Display all loans
            display_all_loans()
        elif user_choice == '8':     # Display late loans
            display_late_loans()
        elif user_choice == '9':    # Find book by name
            find_book()
        elif user_choice == '10':   # Find customer by name
            find_customer()
        elif user_choice == '11':   # Remove book
            remove_book()
        elif user_choice == '12':    # Remove customer
            check_and_remove_customer()
        elif user_choice == '13':    # Remove customer
            break
        else:
            print(f'"{user_choice}" is not an option please choose again\n')
    return


def insert_book():
    # Request and validate before object creation
    new_book_id = req_and_val_book_id()
    if new_book_id is None:
        return
    new_book_name = req_and_val_book_name()
    if new_book_name is None:
        return
    new_book_author = req_and_val_book_author()
    if new_book_author is None:
        return
    new_book_year_published = req_and_val_year_published()
    if new_book_year_published is None:
        return
    new_book_type = req_and_val_book_type()
    if new_book_type is None:
        return
    new_book_amount = req_and_val_book_amount()
    if new_book_amount is None:
        return

    #  inputs validation passed, creating book object
    new_book = Books(new_book_id, new_book_name, new_book_author, new_book_year_published, new_book_type,
                     int(new_book_amount))
    Books.books_list.append(new_book)
    print(f'Book name: "{new_book_name}" was added to the library'+'\n')
    return


def req_and_val_book_id():
    new_book_id = request_book_id()
    if new_book_id is None:
        return
    book_id_available = check_book_id_available(new_book_id)
    if book_id_available is None:
        return
    return new_book_id


def request_book_id():
    while True:
        new_book_id = input("Insert book ID (Y to auto generate): ")
        if new_book_id == '0':
            print('***Insertion was canceled')
            print('Return to library menu\n')
            return
        if new_book_id == 'Y':
            new_book_id = auto_generate_random_book_id()
            print(f'**Auto generate book ID: {new_book_id}')
        if new_book_id.isnumeric() and len(new_book_id) == 7:
            return new_book_id
        print(f'''Book ID: "{new_book_id}" is not a valid ID, please use numeric characters only. 
        Book ID must contain 7 digits
        Y - to auto generate a random number 
        0 to cancel and return to library menu''')


def auto_generate_random_book_id():
    book_id_avail = None
    while not book_id_avail:
        tmp_book_id = randint(10**6, (10**7)-1)  # random number between 1000000-9999999
        book_id_avail = check_book_id_available(tmp_book_id, 'Y')
    return str(tmp_book_id)


def check_book_id_available(new_book_id, auto_gen='N'):
    for book in Books.books_list:
        if new_book_id == book.getBookId():
            if auto_gen == 'N':
                print(f'This book (ID) "{new_book_id}" already exists in the library!\n')
            return
    return True


def req_and_val_book_name():
    new_book_name = request_book_name()
    if new_book_name is None:
        return
    book_name_availability = check_book_name_availability(new_book_name)
    if book_name_availability is None:
        return
    return new_book_name


def request_book_name():
    while True:
        new_book_name = input("Insert book name: ")
        if new_book_name == '0':
            print('***Insertion was canceled')
            print('Return to library menu\n')
            return
        if regex_book_template.search(new_book_name):
            return new_book_name
        print(f'''Book Name: "{new_book_name}" is not a valid name, please use alphabetic, numeric, space, hyphen or dot characters only
        0 to cancel and return to library menu''')


def check_book_name_availability(new_book_name):
    for book in Books.books_list:
        if new_book_name.lower() == book.getBookName().lower():
            print(f'This book name "{new_book_name}" already exists in the library!\n')
            return
    return True


def req_and_val_book_author():
    while True:
        new_book_author = input("Insert book Author (first and last name): ")
        if new_book_author == '0':
            print('***Insertion was canceled')
            print('Return to library menu\n')
            return
        if regex_name_template.search(new_book_author):
            return new_book_author
        print(f'''Author name: "{new_book_author}" is not a valid name, please use alphabetic, space or dot characters only
        0 to cancel and return to library menu''')


def req_and_val_year_published():
    while True:
        new_book_year_published = input("Insert year published: ")
        if new_book_year_published == '-1':
            print('***Insertion was canceled')
            print('Return to library menu\n')
            return
        if new_book_year_published.isnumeric():
            if int(new_book_year_published) > date.today().year:
                print(f'''Year published: "{new_book_year_published}" doesnt make sense, must be before 2023
                -1 to cancel and return to library menu''')
                continue
            elif int(new_book_year_published) < 1450:  # The first book ever created
                print(
                    f'''Year published: "{new_book_year_published}" is too early, must be be after 1450
                -1 to cancel and return to library menu''')
                continue
            else:
                return new_book_year_published
        print(f'''Year published: "{new_book_year_published}" is not a valid age, please use numeric characters only (between 1450-2022)
        -1 to cancel and return to library menu''')


def req_and_val_book_type():
    while True:
        new_book_type = input("Insert book type (1/2/3): ")
        if new_book_type in Books.book_types_opt:
            return new_book_type
        if new_book_type == '-1':
            print('***Insertion was canceled')
            print('Return to library menu\n')
            return
        print(f'''Book type: "{new_book_type}" is not a valid, it must be 1, 2 or 3 
        -1 to cancel and return to library menu''')


def req_and_val_book_amount():
    while True:
        new_book_amount = input("Insert book amount >=1: ")
        if new_book_amount == '-1':
            print('***Insertion was canceled')
            print('Return to library menu\n')
            return
        if new_book_amount.isnumeric() and new_book_amount != '0':
            return new_book_amount
        print(f'''Book amount: "{new_book_amount}" is not a valid, please use positive numeric number and greater than 0
        -1 to cancel and return to library menu''')


def display_all_books():
    if len(Books.books_list) == 0:
        print('No books in the library list\n')
        return
    all_books = []
    for i in range(len(Books.books_list)):
        ind = (i+1,)
        all_books.append(ind + Books.books_list[i].getObjAtt())
    print('The list of the books are: ')
    print(tabulate(all_books, headers=['Index', 'ID', 'Name', 'Author', 'Year published', 'Type', 'Amount']))
    print()


# Find book by name
def find_book():
    desired_book = input('Please insert book name that you want to find: ')
    for item in Books.books_list:
        book_id, book_name, book_author, book_year_published, book_type, amount = Books.getObjAtt(item)
        if desired_book.lower() == book_name.lower():
            print(f'''The book information: 
            ID: {book_id} 
            Name: {book_name}
            Author: {book_author}
            Year published: {book_year_published}
            Type: {book_type}
            Amount: {amount}\n''')
            return
    print(f'No book found named: "{desired_book}"\n')


# Remove book by name, and check no active loan
def remove_book():
    chosen_book_name = input('Please insert book name to remove: ')
    chosen_book_id = ''
    for i in range(len(Books.books_list)):
        if chosen_book_name.lower() == Books.books_list[i].getBookName().lower():
            chosen_book_id = Books.books_list[i].getBookId()
            break
    if chosen_book_id == '':
        print(f'Book name: "{chosen_book_name}" not found in the library\n')
        return
    else:
        book_borrowed = check_no_loans_on_book(chosen_book_id, chosen_book_name)
    if book_borrowed is None:
        print(f'Book name: "{Books.books_list[i].getBookName()}" has been removed\n')
        Books.books_list.pop(i)
    return


# Check no active loan before removing a book
def check_no_loans_on_book(chosen_book_id, chosen_book_name):
    borrowed_lst = []
    for loan in Loans.loans_list:
        if chosen_book_id == loan.getBookId():
            borrowed_lst.append(loan)
    if borrowed_lst:
        borrowed_str_lst = []
        for i in range(len(borrowed_lst)):
            ind = (i + 1,)
            borrowed_str_lst.append(ind + borrowed_lst[i].getObjAtt())
        print(f'Book name: "{chosen_book_name}" cannot be removed, since it borrowed at the moment')
        print(tabulate(borrowed_str_lst, headers=['Index', 'Customer ID', 'Book ID', 'Loan Date', 'Return Date']))
        print()
        return True


