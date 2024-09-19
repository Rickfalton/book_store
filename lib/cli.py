import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Book, Order, OrderItem

# Database setup
DATABASE_URL = 'sqlite:///lib/vbs_shop.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def register_user(username, email):
    session = Session()
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        print("Username already exists. Please choose a different username.")
        session.close()
        return None
    
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    session.close()
    print(f"User '{username}' registered successfully.")
    return user

def view_users():
    session = Session()
    users = session.query(User).all()
    session.close()
    for user in users:
        print(f"User ID: {user.user_id}, Username: {user.username}, Email: {user.email}")

def view_books():
    session = Session()
    books = Book.view_books()
    session.close()
    if not books:
        print("No books available.")
        return
    for book in books:
        print(f"Book ID: {book.book_id}, Title: '{book.title}', Author: {book.author}, Price: ${book.price}, Stock: {book.stock_quantity}")

def add_book(title, author, price, stock_quantity):
    session = Session()
    book = Book(title=title, author=author, price=price, stock_quantity=stock_quantity)
    session.add(book)
    session.commit()
    session.close()
    print(f"Book '{title}' added successfully.")

def add_to_cart(user, book_id, quantity):
    session = Session()
    book = session.query(Book).filter_by(book_id=book_id).first()
    if not book:
        print("Book not found.")
        session.close()
        return
    
    if book.stock_quantity < quantity:
        print(f"Insufficient stock for '{book.title}'. Available: {book.stock_quantity}.")
    else:
        user.add_to_cart(book, quantity)
    session.close()

def complete_purchase(user):
    Order.complete_purchase(user)

def main():
    print("Welcome to the Virtual Bookstore CLI!")
    
    while True:
        print("\nMenu:")
        print("1. Register User")
        print("2. View Users")
        print("3. View Books")
        print("4. Add Book")
        print("5. Add to Cart")
        print("6. Complete Purchase")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            username = input("Enter username: ")
            email = input("Enter email: ")
            register_user(username, email)
        elif choice == '2':
            view_users()
        elif choice == '3':
            view_books()
        elif choice == '4':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            price = float(input("Enter book price: "))
            stock_quantity = int(input("Enter stock quantity: "))
            add_book(title, author, price, stock_quantity)
        elif choice == '5':
            username = input("Enter your username: ")
            session = Session()
            user = session.query(User).filter_by(username=username).first()
            session.close()
            if user:
                book_id = int(input("Enter book ID to add to cart: "))
                quantity = int(input("Enter quantity: "))
                add_to_cart(user, book_id, quantity)
            else:
                print("User not found. Please register first.")
        elif choice == '6':
            username = input("Enter your username: ")
            session = Session()
            user = session.query(User).filter_by(username=username).first()
            session.close()
            if user:
                complete_purchase(user)
            else:
                print("User not found. Please register first.")
        elif choice == '7':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Base.metadata.create_all(engine)  # Ensure all tables are created
    main()
