from sqlalchemy import Column, Integer, String,DECIMAL,DateTime,func,ForeignKey,BigInteger
from sqlalchemy.orm import relationship, backref
from database2 import Base

class Product(Base):
    _tablename_= "Products"

    Pid = Column(Integer, primary_key=True)
    Pname = Column(String)
    Description = Column(String)
    Price= Column(DECIMAL)
    stockRel = relationship("Stock", backref="product",foreign_keys='Stock.Pid', cascade="all, delete")
    sorderRel = relationship("Sorder", backref="product",foreign_keys='Sorder.Pid', cascade="all, delete")
    corderRel = relationship("Corder", backref="product",foreign_keys='Corder.Pid', cascade="all, delete")
    
    def repr(self):
        return f"<Product(Pid={self.Pid}, Pname='{self.Pname}', Description='{self.Description}',Price='{self.Price}')>"
    
class Supplier(Base):
    _tablename_= "Suppliers"

    Sid = Column(Integer, primary_key=True)
    Sname = Column(String)
    Scontact= Column(Integer)
    Sadd= Column(String)

    def repr(self):
        return f"<Supplier(Sid={self.Sid}, Sname='{self.Sname}', Scontact='{self.Scontact}',Sadd='{self.Sadd}')>"

class Customer(Base):
    _tablename_= "Customers"

    Cid = Column(Integer, primary_key=True)
    Cname = Column(String)
    Ccontact= Column(Integer)
    Cadd= Column(String)

    def repr(self):
        return f"<Customer(Cid={self.Cid}, Cname='{self.Cname}', Ccontact='{self.Ccontact}',Cadd='{self.Cadd}')>"


class Stock(Base):
    _tablename_= "Stocks"

    Sid = Column(Integer, primary_key=True)
    Pid = Column(Integer, ForeignKey('Products.Pid',ondelete='CASCADE',onupdate='CASCADE'))
    Qnt = Column(Integer)
    
     

    def repr(self):
        return f"<Stock(Stid={self.Stid}, Pid='{self.Pid}', Qnt='{self.Qnt}')>"
    
class Sorder(Base):
    _tablename_= "Sorders" 

    Oid = Column(Integer, primary_key=True)
    Pid = Column(Integer, ForeignKey('Products.Pid',ondelete='CASCADE',onupdate='CASCADE'))
    Sid = Column(Integer, ForeignKey('Suppliers.Sid',ondelete='CASCADE',onupdate='CASCADE'))
    Pqnt = Column(Integer)
    

    def repr(self):
        return f"<Sorder(Oid={self.Oid}, Pid='{self.Pid}', Sid='{self.Sid}',Pqnt='{self.Pqnt}')>"

class Corder(Base):
    _tablename_= "Corders" 

    Oid = Column(Integer, primary_key=True)
    Pid = Column(Integer, ForeignKey('Products.Pid',ondelete='CASCADE',onupdate='CASCADE'))
    Cid = Column(Integer, ForeignKey('Customers.Cid',ondelete='CASCADE',onupdate='CASCADE'))
    Pqnt = Column(Integer)
    

    def repr(self):
        return f"<Corder(Oid={self.Oid}, Pid='{self.Pid}', Cid='{self.Cid}',Pqnt='{self.Pqnt}')>"


class Stransaction(Base):
    _tablename_= "Stransactions"

    Tid = Column(Integer, primary_key=True)
    Oid = Column(Integer, ForeignKey('Sorders.Oid',ondelete='CASCADE',onupdate='CASCADE'))
    TDate=Column(DateTime)
    Tprice=Column(Integer)
    #product = relationship('Product', back_populates='Transaction')
  
    def repr(self):
        return f"<Stransaction(Tid={self.Tid}, Oid='{self.Oid}',TDate='{self.TDate}',Tprice='{self.Tprice})>"
    

class Ctransaction(Base):
    _tablename_= "Ctransactions"

    Tid = Column(Integer, primary_key=True)
    Oid = Column(Integer, ForeignKey('Corders.Oid',ondelete='CASCADE',onupdate='CASCADE'))
    TDate=Column(DateTime)
    Tprice=Column(Integer)
    #product = relationship('Product', back_populates='Transaction')
  
    def repr(self):
        return f"<Ctransaction(Tid={self.Tid}, Oid='{self.Oid}',TDate='{self.TDate}',Tprice='{self.Tprice})>"