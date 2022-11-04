from objects.Customers import Customers
from objects.Loans import Loans
import re
from tabulate import tabulate

"""
This Module define customers functions
"""

regex_city_template = re.compile("^[a-zA-Z-\s\.]+$")
regex_name_template = re.compile("^[A-Za-z\.]+(\s[A-Za-z-\.]+)+$")


def insert_customer():
    # Request and validate before object creation
    new_customer_id = req_and_val_customer_id()
    if new_customer_id is None:
        return
    new_customer_name = req_and_val_customer_name()
    if new_customer_name is None:
        return
    new_customer_city = req_and_val_customer_city()
    if new_customer_city is None:
        return
    new_customer_age = req_and_val_customer_age()
    if new_customer_age is None:
        return

    # Customer validation passed, creating customer object
    new_customer = Customers(new_customer_id, new_customer_name, new_customer_city, new_customer_age, 0)
    Customers.customers_list.append(new_customer)
    print(f'Customer name: "{new_customer_name}" was added to the library\n')
    return


def req_and_val_customer_id():
    new_customer_id = request_customer_id()
    if new_customer_id is None:
        return
    customer_id_available = validate_customer_id_available(new_customer_id)
    if customer_id_available is None:
        return
    return new_customer_id


def request_customer_id():
    while True:
        new_customer_id = input("Insert customer ID: ")
        if new_customer_id == '0':
            print('***Insertion was canceled')
            print('Return to library menu\n')
            return
        if new_customer_id.isnumeric() and len(new_customer_id) == 9:
            return new_customer_id
        print(f'''Customer ID: "{new_customer_id}" is not a valid ID, please use numeric characters only. 
        Customer ID must contain 9 digits 
        0 to cancel and return to library menu''')


def validate_customer_id_available(new_customer_id):
    for customer in Customers.customers_list:
        if new_customer_id == customer.getCustomerId():
            print('This customer (ID) already exists in the library!\n')
            return
    return True


def req_and_val_customer_name():
    while True:
        new_customer_name = input("Insert customer name (first and last name): ")
        if new_customer_name == '0':
            print('***Insertion was canceled')
            print('Return to library menu\n')
            return
        if regex_name_template.search(new_customer_name):
            break
        print(f'''Customer Name: "{new_customer_name}" is not a valid name, please use alphabetic, space, hyphen or dot characters only
        0 to cancel and return to library menu''')
    return new_customer_name


def req_and_val_customer_city():
    while True:
        new_customer_city = input("Insert customer city: ")
        if new_customer_city == '0':
            print('***Insertion was canceled')
            print('Return to library menu\n')
            return
        if regex_city_template.search(new_customer_city):
            break
        print(f'''Customer city: "{new_customer_city}" is not a valid name, please use alphabetic, space, hyphen or dot characters only
        0 to cancel and return to library menu''')
    return new_customer_city


def req_and_val_customer_age():
    while True:
        new_customer_age = input("Insert customer age >=6: ")
        if new_customer_age == '-1':
            print('***Insertion was canceled')
            print('Return to library menu\n')
            return
        if not new_customer_age.isnumeric():
            print(f'''Customer age: "{new_customer_age}" is not a valid age, please use numeric characters only (between 6-120)
            -1 to cancel and return to library menu''')
            continue
        if int(new_customer_age) > 120:
            print(f'''Customer age: "{new_customer_age}" doesnt make sense, the age must be less than 120
            -1 to cancel and return to library menu''')
            continue
        if int(new_customer_age) < 6:
            print(
                f'''Customer age: "{new_customer_age}" is too young, per library guidelines the minimum age is 6 years old, please come back in {6 - int(new_customer_age)} years
            -1 to cancel and return to library menu''')
            continue
        break
    return new_customer_age


def display_all_customers():
    if len(Customers.customers_list) == 0:
        print('No customers in the library list\n')
        return
    all_customers = []
    for i in range(len(Customers.customers_list)):
        ind = (i + 1,)
        all_customers.append(ind + Customers.customers_list[i].getObjAtt())
    print('The list of the customers are: ')
    print(tabulate(all_customers, headers=['Index', 'ID', 'Name', 'City', 'Age', 'Borrowed books']))
    print()


# Find customer by name - can be several customers
def find_customer():
    desired_customer_name = input('Please insert customer name that you want to find: ')
    customers_name_found = []
    for customer in Customers.customers_list:
        if desired_customer_name.lower() == customer.getCustomerName().lower():
            customers_name_found.append(customer)
    if len(customers_name_found) == 0:
        print(f'No customer found named: "{desired_customer_name}"\n')
        return
    customer_name_str_list = []
    for i in range(len(customers_name_found)):
        ind = (i + 1,)
        customer_name_str_list.append(ind + customers_name_found[i].getObjAtt())
    print(f'{len(customers_name_found)} customers found with that name: ')
    print(tabulate(customer_name_str_list, headers=['Index', 'ID', 'Name', 'City', 'Age', 'Borrowed Books']))
    print()


def check_and_remove_customer():
    chosen_customer_id, borrowed_books = check_no_loans_on_customer()
    if borrowed_books == 0:
        remove_customer_from_list(chosen_customer_id)
    return


def check_no_loans_on_customer():
    chosen_customer_id = input('Please insert customer ID to remove: ')
    loans_on_customer = []
    for loan in Loans.loans_list:
        if chosen_customer_id == loan.getCustId():
            loans_on_customer.append(loan)
    if len(loans_on_customer):
        loans_on_customer_str_list = []
        for i in range(len(loans_on_customer)):
            ind = (i + 1,)
            loans_on_customer_str_list.append(ind + loans_on_customer[i].getObjAtt())
        print(f'The costumer cannot be removed, because he have {len(loans_on_customer)} book/s to return:')
        print(tabulate(loans_on_customer_str_list, headers=['Index','Customer ID', 'Book ID', 'Loan Date', 'Return Date']))
        print()
    return chosen_customer_id, len(loans_on_customer)


def remove_customer_from_list(chosen_customer_id):
    for i in range(len(Customers.customers_list)):
        if chosen_customer_id == Customers.customers_list[i].getCustomerId():
            Customers.customers_list.pop(i)
            print(f'Customer ID: "{chosen_customer_id}" has been removed\n')
            return
    print(f'Customer ID: "{chosen_customer_id}" not found in the library\n')
    return

