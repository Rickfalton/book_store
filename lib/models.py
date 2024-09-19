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
    user = relationship("User", back_populates="carts")
    carts = relationship("Cart", back_populates="user")
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

class Order(Base):
    __tablename__ = 'orders'
    
    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    order_date = Column(DateTime, default=datetime.utcnow)
    total_amount = Column(Float, nullable=False)
    user = relationship("User", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")

    @classmethod
    def complete_purchase(cls, user):
        session = Session()
        cart_items = session.query(Cart).filter_by(user_id=user.user_id).all()
        total_amount = 0
        
        for item in cart_items:
            book = session.query(Book).filter_by(book_id=item.book_id).first()
            if book and book.stock_quantity >= item.quantity:
                total_amount += book.price * item.quantity
                book.stock_quantity -= item.quantity  # Update stock
            else:
                print(f"Not enough stock for '{book.title}'")
        
        if total_amount > 0:
            order = cls(user_id=user.user_id, total_amount=total_amount)
            session.add(order)
            session.commit()
            print(f"Purchase completed! Total amount: ${total_amount:.2f}")
        else:
            print("No valid items in cart.")
        
        # Clear cart after purchase
        session.query(Cart).filter_by(user_id=user.user_id).delete()
        session.commit()
        session.close()

class OrderItem(Base):
    __tablename__ = 'order_items'
    
    order_item_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'))
    book_id = Column(Integer, ForeignKey('books.book_id'))
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    order_id = Column(Integer, ForeignKey('orders.order_id'))
    order = relationship("Order", back_populates="order_items")


engine = create_engine('sqlite:///lib/vbs_shop.db')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()