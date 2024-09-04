import pandas as pd
from faker import Faker
import random

# Initialize Faker instance
data_generator = Faker()

# Generate dummy data for each table
def generate_libraries(num):
    data = []
    for i in range(num):
        data.append({
            'library_id': i + 1,
            'name': data_generator.company(),
            'location': data_generator.city()
        })
    return pd.DataFrame(data)

def generate_books(num):
    data = []
    for i in range(num):
        data.append({
            'book_id': i + 1,
            'title': data_generator.catch_phrase(),
            'author': data_generator.name(),
            'isbn': data_generator.isbn13(separator='-')
        })
    return pd.DataFrame(data)

def generate_categories(num):
    categories = ['Self-Improvement', 'Biography', 'Fantasy', 'Romance', 'Science Fiction', 'History', 'Thriller']
    data = [{'category_id': i + 1, 'name': cat} for i, cat in enumerate(categories[:num])]
    return pd.DataFrame(data)

def generate_book_categories(books, categories):
    data = []
    for book_id in books['book_id']:
        category_id = random.choice(categories['category_id'])
        data.append({
            'book_id': book_id,
            'category_id': category_id
        })
    return pd.DataFrame(data)

def generate_users(num):
    data = []
    for i in range(num):
        data.append({
            'user_id': i + 1,
            'username': data_generator.user_name(),
            'email': data_generator.email(),
            'password': data_generator.password(),
            'created_at': data_generator.date_this_decade()
        })
    return pd.DataFrame(data)

def generate_loans(users, books, libraries):
    data = []
    for _ in range(len(users) * 2):  # Assuming 2 books per user
        user_id = random.choice(users['user_id'])
        book_id = random.choice(books['book_id'])
        library_id = random.choice(libraries['library_id'])
        loan_date = data_generator.date_this_year()
        due_date = data_generator.date_between(start_date=loan_date, end_date='+15d')
        data.append({
            'loan_id': len(data) + 1,
            'user_id': user_id,
            'book_id': book_id,
            'library_id': library_id,
            'loan_date': loan_date,
            'due_date': due_date,
            'return_date': data_generator.date_between(start_date=loan_date, end_date=due_date) if random.random() > 0.5 else None
        })
    return pd.DataFrame(data)

def generate_holds(users, books, libraries):
    data = []
    for _ in range(len(users) * 2):  # Assuming 2 holds per user
        user_id = random.choice(users['user_id'])
        book_id = random.choice(books['book_id'])
        library_id = random.choice(libraries['library_id'])
        hold_date = data_generator.date_this_year()
        expiry_date = data_generator.date_between(start_date=hold_date, end_date='+7d')
        data.append({
            'hold_id': len(data) + 1,
            'user_id': user_id,
            'book_id': book_id,
            'library_id': library_id,
            'hold_date': hold_date,
            'expiry_date': expiry_date
        })
    return pd.DataFrame(data)

def generate_inventory(libraries, books):
    data = []
    for library_id in libraries['library_id']:
        for book_id in books['book_id']:
            data.append({
                'inventory_id': len(data) + 1,
                'library_id': library_id,
                'book_id': book_id,
                'quantity': random.randint(0, 10)  # Randomly setting book quantities
            })
    return pd.DataFrame(data)

# Generate and save datasets
libraries = generate_libraries(5)
books = generate_books(20)
categories = generate_categories(7)
book_categories = generate_book_categories(books, categories)
users = generate_users(10)
loans = generate_loans(users, books, libraries)
holds = generate_holds(users, books, libraries)
inventory = generate_inventory(libraries, books)

# Save datasets to CSV files
libraries.to_csv('libraries.csv', index=False)
books.to_csv('books.csv', index=False)
categories.to_csv('categories.csv', index=False)
book_categories.to_csv('book_categories.csv', index=False)
users.to_csv('users.csv', index=False)
loans.to_csv('loans.csv', index=False)
holds.to_csv('holds.csv', index=False)
inventory.to_csv('inventory.csv', index=False)

print("Dummy datasets have been generated and saved as CSV files.")
