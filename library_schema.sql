CREATE TABLE Library (
    library_id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    location VARCHAR NOT NULL
);

CREATE TABLE Book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL,
    isbn VARCHAR UNIQUE NOT NULL
);

CREATE TABLE Category (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL UNIQUE
);

CREATE TABLE Book_Category (
    book_id INT,
    category_id INT,
    PRIMARY KEY (book_id, category_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

CREATE TABLE Users (  -- Renamed from User to Users
    user_id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL UNIQUE,
    email VARCHAR NOT NULL UNIQUE,
    password VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Loan (
    loan_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    library_id INT NOT NULL,
    loan_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),  -- Updated foreign key reference
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (library_id) REFERENCES Library(library_id)
);

CREATE TABLE Hold (
    hold_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    library_id INT NOT NULL,
    hold_date DATE NOT NULL,
    expiry_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),  -- Updated foreign key reference
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (library_id) REFERENCES Library(library_id)
);
