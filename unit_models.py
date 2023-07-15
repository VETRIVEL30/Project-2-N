from datetime import datetime
from decimal import Decimal
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_test import Product, Supplier, Customer, Stock, Sorder, Corder, Stransaction, Ctransaction
from database2 import Base

# Create a PostgreSQL database for testing
engine = create_engine("postgresql://postgres:Password0#@database1.cuetvdodk2bh.us-east-1.rds.amazonaws.com:5432/test")
Session = sessionmaker(bind=engine)

# Create the tables in the database
Base.metadata.create_all(engine)

class TestModels(unittest.TestCase):
    def setUp(self):
        # Create a new session for each test
        self.session = Session()

    def tearDown(self):
        # Rollback the session after each test
        self.session.rollback()
        self.session.close()

    def test_product(self):
        # Create a Product object
        product = Product(Pname='Test Product', Description='Test Description', Price=10.99)

        # Add the product to the session
        self.session.add(product)
        self.session.commit()

        # Retrieve the product from the database
        retrieved_product = self.session.query(Product).filter_by(Pid=product.Pid).first()

        # Assert that the retrieved product matches the original product
        self.assertEqual(retrieved_product.Pname, 'Test Product')
        self.assertEqual(retrieved_product.Description, 'Test Description')
        self.assertEqual(retrieved_product.Price, Decimal('10.99'))
        self.assertNotEqual(retrieved_product.Pname, 'Product')

    def test_supplier(self):
        # Create a Supplier object
        supplier = Supplier(Sname='Test Supplier', Scontact=12345689, Sadd='Test Address')

        # Add the supplier to the session
        self.session.add(supplier)
        self.session.commit()

        # Retrieve the supplier from the database
        retrieved_supplier = self.session.query(Supplier).filter_by(Sid=supplier.Sid).first()

        # Assert that the retrieved supplier matches the original supplier
        self.assertEqual(retrieved_supplier.Sname, 'Test Supplier')
        self.assertEqual(retrieved_supplier.Scontact, 12345689)
        self.assertEqual(retrieved_supplier.Sadd, 'Test Address')
    
    def test_customer(self):
        # Create a Customer object
        customer = Customer(Cname='Test Customer', Ccontact=98765432, Cadd='Test Address')

        # Add the customer to the session
        self.session.add(customer)
        self.session.commit()

        # Retrieve the customer from the database
        retrieved_customer = self.session.query(Customer).filter_by(Cid=customer.Cid).first()

        # Assert that the retrieved customer matches the original customer
        self.assertEqual(retrieved_customer.Cname, 'Test Customer')
        self.assertEqual(retrieved_customer.Ccontact, 98765432)
        self.assertEqual(retrieved_customer.Cadd, 'Test Address')    

    def test_stock(self):
        # Create a Product object
        product = Product(Pname='Test Product', Description='Test Description', Price=10.99)
        self.session.add(product)
        self.session.commit()

        # Create a Stock object
        stock = Stock(Pid=product.Pid, Qnt=100)

        # Add the stock to the session
        self.session.add(stock)
        self.session.commit()

        # Retrieve the stock from the database
        retrieved_stock = self.session.query(Stock).filter_by(Sid=stock.Sid).first()

        # Assert that the retrieved stock matches the original stock
        self.assertEqual(retrieved_stock.Pid, product.Pid)
        self.assertEqual(retrieved_stock.Qnt, 100)

    def test_sorder(self):
        # Create a Product object
        product = Product(Pname='Test Product', Description='Test Description', Price=10.99)
        self.session.add(product)
        self.session.commit()

        # Create a Supplier object
        supplier = Supplier(Sname='Test Supplier', Scontact=1234567890, Sadd='Test Address')
        self.session.add(supplier)
        self.session.commit()

        # Create an Sorder object
        sorder = Sorder(Pid=product.Pid, Sid=supplier.Sid, Pqnt=50)

        # Add the Sorder to the session
        self.session.add(sorder)
        self.session.commit()

        # Retrieve the Sorder from the database
        retrieved_sorder = self.session.query(Sorder).filter_by(Oid=sorder.Oid).first()

        # Assert that the retrieved Sorder matches the original Sorder
        self.assertEqual(retrieved_sorder.Pid, product.Pid)
        self.assertEqual(retrieved_sorder.Sid, supplier.Sid)
        self.assertEqual(retrieved_sorder.Pqnt, 50)

    def test_corder(self):
        # Create a Product object
        product = Product(Pname='Test Product', Description='Test Description', Price=10.99)
        self.session.add(product)
        self.session.commit()

        # Create a Customer object
        customer = Customer(Cname='Test Customer', Ccontact=98765432, Cadd='Test Address')
        self.session.add(customer)
        self.session.commit()

        # Create a Corder object
        corder = Corder(Pid=product.Pid, Cid=customer.Cid, Pqnt=20)

        # Add the Corder to the session
        self.session.add(corder)
        self.session.commit()

        # Retrieve the Corder from the database
        retrieved_corder = self.session.query(Corder).filter_by(Oid=corder.Oid).first()

        # Assert that the retrieved Corder matches the original Corder
        self.assertEqual(retrieved_corder.Pid, product.Pid)
        self.assertEqual(retrieved_corder.Cid, customer.Cid)
        self.assertEqual(retrieved_corder.Pqnt, 20)

    def test_stransaction(self):
        # Create a Sorder object
        sorder = Sorder(Pid=1, Sid=1, Pqnt=10)
        self.session.add(sorder)
        self.session.commit()

        # Create an Stransaction object
        stransaction = Stransaction(Oid=sorder.Oid, TDate=datetime.now(), Tprice=100)

        # Add the Stransaction to the session
        self.session.add(stransaction)
        self.session.commit()

        # Retrieve the Stransaction from the database
        retrieved_stransaction = self.session.query(Stransaction).filter_by(Tid=stransaction.Tid).first()

        # Assert that the retrieved Stransaction matches the original Stransaction
        self.assertEqual(retrieved_stransaction.Oid, sorder.Oid)
        self.assertEqual(retrieved_stransaction.TDate, stransaction.TDate)
        self.assertEqual(retrieved_stransaction.Tprice, 100)
    
    def test_ctransaction(self):
        # Create a Corder object
        corder = Corder(Pid=1, Cid=1, Pqnt=5)
        self.session.add(corder)
        self.session.commit()

        # Create a Ctransaction object
        ctransaction = Ctransaction(Oid=corder.Oid, TDate=datetime.now(), Tprice=50)

        # Add the Ctransaction to the session
        self.session.add(ctransaction)
        self.session.commit()

        # Retrieve the Ctransaction from the database
        retrieved_ctransaction = self.session.query(Ctransaction).filter_by(Tid=ctransaction.Tid).first()

        # Assert that the retrieved Ctransaction matches the original Ctransaction
        self.assertEqual(retrieved_ctransaction.Oid, corder.Oid)
        self.assertEqual(retrieved_ctransaction.TDate, ctransaction.TDate)
        self.assertEqual(retrieved_ctransaction.Tprice, 50)
        
if __name__ == '__main__':
    unittest.main()