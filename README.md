### Virtual Book Store
## Overview
The Virtual Book Store project is a command-line application that allows users to browse, purchase, and manage books efficiently. It leverages SQLAlchemy as an ORM for data management and utilizes SQLite as the database backend. This project aims to automate product data management for a retail field team, reducing inconsistencies and improving efficiency.

## Features
User Management: Users can register, log in, and manage their accounts.
Book Catalog: Users can view available books, including title, author, price, and stock quantity.
Shopping Cart: Users can add books to their cart and manage quantities.
Order Processing: Users can complete purchases, automatically updating stock levels.
Data Seeding: Use the Faker library to populate the database with sample book data.
Sales Reporting: Generate reports of completed sales.

## Running the Application

1. Ensure Python 3.x is installed on your machine.

2. Set Up the Virtual Environment: This project uses pipenv for managing dependencies:
   bash
   $ pipenv install
   $ pipenv shell
   

3. Run database migrations with Alembic:
   bash
   $ alembic upgrade head
   

4. Run the test cases for validation:
   bash
   $ pytest
   

5. To run the application, execute the main script:
   bash
   $ python3 app/main.py

## Usage Instructions
## CLI Commands


## Register a new user 

$ python3 app/main.py register <username> <password>
Description: Registers a new user with the specified username and password.

## Log in:

$ python3 app/main.py login <username> <password>
Description: Authenticates a user and starts a session.

## View available books:


$ python3 app/main.py list_books
Description: Displays a list of available books with details such as title, author, price, and stock.

## Add a book to the cart:

$ python3 app/main.py add_to_cart <book_id> <quantity>
Description: Adds a specified quantity of the book to the shopping cart.

## Checkout:

$ python3 app/main.py checkout
Description: Completes the purchase and updates the stock levels.

## Generate sales report:


$ python3 app/main.py generate_report
Description: Generates a report of completed sales.

## Technologies Used
Python: Programming language for application logic.
SQLAlchemy: ORM for database interactions.
SQLite: Lightweight database for data storage.
Faker: Library for generating fake data for seeding the database.

## Access the Project
You can access the project on GitHub: Virtual Book Store Repository