from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    orders = relationship("Order", back_populates="user")
    cart_items = relationship("Cart", back_populates="user")

    def add_to_cart(self, book, quantity):
        session = Session()
        cart_item = Cart(user_id=self.user_id, book_id=book.book_id, quantity=quantity)
        session.add(cart_item)
        session.commit()
        session.close()
        print(f"Added {quantity} of '{book.title}' to your cart.")

class Book(Base):
    __tablename__ = 'books'
    
    book_id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0)
    orders = relationship("OrderItem", back_populates="book")

    @classmethod
    def view_books(cls):
        session = Session()
        books = session.query(cls).all()
        session.close()
        return books



engine = create_engine('sqlite:///app/pharmacy.db')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()