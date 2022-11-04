import pickle

from handlers.BooksHandler import deal_user_choice
from objects.Books import Books
from objects.Customers import Customers
from objects.Loans import Loans


print('\nWelcome to the library app:')
# Reading the files to lists as pickles
with open('database/Books.pkl', 'rb') as f_books, open('database/Customers.pkl', 'rb') as f_customers, open(
        'database/Loans.pkl', 'rb') as f_loans:
    Books.set_books_list(pickle.load(f_books))
    Customers.set_customers_list(pickle.load(f_customers))
    Loans.set_loans_list(pickle.load(f_loans))


if __name__ == '__main__':
    deal_user_choice()


# Writing to the files as pickles
with open('database/Books.pkl', 'wb') as f_books, open('database/Customers.pkl', 'wb') as f_customers, open(
        'database/Loans.pkl', 'wb') as f_loans:
    pickle.dump(Books.books_list, f_books)
    pickle.dump(Customers.customers_list, f_customers)
    pickle.dump(Loans.loans_list, f_loans)

