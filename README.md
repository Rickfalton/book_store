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
## Technologies Used
Python: Programming language for application logic.
SQLAlchemy: ORM for database interactions.
SQLite: Lightweight database for data storage.
Faker: Library for generating fake data for seeding the database.