import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Book

# Database setup
DATABASE_URL = 'sqlite:///lib/vbs_shop.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def seed_books(num_books=50):
    fake = Faker()
    session = Session()

    for _ in range(num_books):
        book = Book(
            title=fake.sentence(nb_words=random.randint(2, 5)).rstrip('.'),  # Create a random title
            author=fake.name(),  # Create a random author name
            price=round(random.uniform(5.0, 100.0), 2),  #  Get Random price between $5.00 and $100.00
            stock_quantity=random.randint(0, 50)  # get Random stock quantity between 0 and 50
        )
        session.add(book)

    session.commit()
    session.close()
    print(f"Successfully seeded {num_books} books.")

if __name__ == "__main__":
    Base.metadata.create_all(engine)  #  all tables are created
    seed_books(50)  
