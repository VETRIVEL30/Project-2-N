from database import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship, backref
from datetime import datetime



class Supplier(Base):
    __tablename__ = 'supplier'

    supplier_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    address = Column(String, nullable=False)
    contact = Column(String, nullable=False)
    email = Column(String, nullable=False)

    products = relationship('Product', secondary='product_supplier', backref='suppliers')

class Product(Base):
    __tablename__ = 'product'

    product_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String)
    price = Column(Numeric(10, 2), nullable=False)

product_supplier = Table(
    'product_supplier', Base.metadata,
    Column('product_id', Integer, ForeignKey('product.product_id'), primary_key=True),
    Column('supplier_id', Integer, ForeignKey('supplier.supplier_id'), primary_key=True)
)


class Stock(Base):
    __tablename__ = 'stock'

    stock_id = Column(Integer, primary_key=True, nullable=False)
    product_id = Column(Integer, ForeignKey('product.product_id', ondelete='CASCADE'), nullable=False)
    quantity = Column(Integer, nullable=False)
    location = Column(String, nullable=False)
    threshold = Column(Integer, nullable=False)
    product = relationship("Product", backref="stocks")


class SupplierOrder(Base):
    __tablename__ = 'supplier_order'

    order_id = Column(Integer, primary_key=True, nullable=False)
    supplier_id = Column(Integer, ForeignKey('supplier.supplier_id', ondelete='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.product_id', ondelete='CASCADE'), nullable=False)
    stock_id = Column(Integer, ForeignKey('stock.stock_id', ondelete='CASCADE'), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Numeric(10, 2), nullable=False)
    order_date = Column(DateTime, nullable=False)
    
    supplier = relationship("Supplier", backref=backref("supplier_orders", cascade="all, delete-orphan"))
    product = relationship("Product", backref=backref("supplier_orders", cascade="all, delete-orphan"))
    stock = relationship("Stock", backref=backref("supplier_orders", cascade="all, delete-orphan"))

    def calculate_total_price(self):
        if self.product:
            self.total_price = self.quantity * self.product.price




class SupplierTransaction(Base):
    __tablename__ = 'supplier_transaction'

    transaction_id = Column(Integer, primary_key=True, nullable=False)
    supplier_id = Column(Integer, ForeignKey('supplier.supplier_id', ondelete='CASCADE'), nullable=False)
    order_id = Column(Integer, ForeignKey('supplier_order.order_id', ondelete='CASCADE'), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    transaction_date = Column(DateTime, nullable=False)

    supplier = relationship("Supplier", backref=backref("transactions", cascade="all, delete-orphan"))
    order = relationship("SupplierOrder", backref=backref("transactions", cascade="all, delete-orphan"))


class Consumer(Base):
    __tablename__ = 'consumer'

    consumer_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    address = Column(String, nullable=False)
    contact = Column(String, nullable=False)
    email = Column(String, nullable=False)

class ConsumerOrder(Base):
    __tablename__ = 'consumer_order'

    order_id = Column(Integer, primary_key=True, nullable=False)
    consumer_id = Column(Integer, ForeignKey('consumer.consumer_id', ondelete='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.product_id', ondelete='CASCADE'), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Numeric(10, 2), nullable=False)
    order_date = Column(DateTime, nullable=False)

    consumer = relationship("Consumer", backref="consumer_orders")
    product = relationship("Product", backref="consumer_orders")

    
    def calculate_total_price(self):
        if self.product:
            self.total_price = self.quantity * self.product.price

class ConsumerTransaction(Base):
    __tablename__ = 'consumer_transaction'

    transaction_id = Column(Integer, primary_key=True, nullable=False)
    consumer_id = Column(Integer, ForeignKey('consumer.consumer_id', ondelete='CASCADE'), nullable=False)
    order_id = Column(Integer, ForeignKey('consumer_order.order_id', ondelete='CASCADE'), nullable=False)
    stock_id = Column(Integer, ForeignKey('stock.stock_id', ondelete='CASCADE'), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    transaction_date = Column(DateTime, nullable=False)
    
    consumer = relationship("Consumer", backref=backref("transactions", cascade="all, delete-orphan"))
    order = relationship("ConsumerOrder", backref=backref("transactions", cascade="all, delete-orphan"))
    stock = relationship("Stock", backref=backref("transactions", cascade="all, delete-orphan"))

    def set_amount_from_order(self):
        if self.order:
            self.amount = self.order.total_price