
from typing import List,Optional
from models import *
from dao import *
import json



class Supplier:
    supplier_id: int
    name: str
    address: str
    contact: str
    email: str
    # product: List['Product']



class Product:
    product_id: int
    name: str
    description: str
    price: float
    # supplier:List[Supplier]


class Stock:
    stock_id: int
    product_id: int
    quantity: int
    location: str
    threshold: int



class SupplierOrder:
    order_id: int
    supplier: Supplier
    product: Product
    stock: Stock
    quantity: int
    order_date: str
    total_price=float

    
    def calculate_total_price(self) -> float:
        return self.quantity * self.product.price


class Consumer:
    consumer_id: int
    name: str
    address: str
    contact: str
    email: str


class ConsumerOrder:
    order_id: int
    consumer: Consumer
    product: Product
    quantity: int
    order_date: str



class ConsumerTransaction:
    transaction_id: int
    consumer: Consumer
    order: ConsumerOrder
    amount: float
    transaction_date: str

    
    def consumer_id(self) -> int:
        return self.consumer.consumer_id

    
    def order_id(self) -> int:
        return self.order.order_id


class SupplierTransaction:
    transaction_id: int
    supplier: Supplier
    order: SupplierOrder
    transaction_date: str
    amount: float



class Query:
    
    def get_supplier_by_id(supplier_id: int) -> Supplier:
        return SupplierDAO.get_supplier_by_id(supplier_id)

    
    def get_all_suppliers() -> List[Supplier]:
        return SupplierDAO.get_all_suppliers()

    
    def get_product_by_id(product_id: int) -> Product:
        productDao = ProductDAO.get_product_by_id(product_id)
        Product = {}
        Product["product_id"]=productDao.product_id
        Product["name"]=productDao.name
        Product["price"] = productDao.price
        Product["description"] = productDao.description
        return Product

    
    def get_all_products() -> List[Product]:
        return ProductDAO.get_all_products()

    
    def get_stock_by_id(stock_id: int) -> Stock:
        return StockDAO.get_stock_by_id(stock_id)

    
    def get_all_stocks() -> List[Stock]:
        return StockDAO.get_all_stocks()
    
#------------------------------supplier order--------------------------------------------------------------------------------------------------------------------
    
    def get_supplier_order_by_id(order_id: int) -> SupplierOrder:
        return SupplierOrderDAO.get_supplier_order_by_id(order_id)

    
    def get_all_supplier_orders() -> List[SupplierOrder]:
        return SupplierOrderDAO.get_all_supplier_orders()
    
    
    def get_orders_by_supplier_id(self, supplier_id: int) -> List[SupplierOrder]:
        return SupplierOrderDAO.get_orders_by_supplier_id(supplier_id)
   
    
    def get_suppliers_by_order_id(order_id: int) -> List[Supplier]:
        return SupplierOrderDAO.get_suppliers_by_order_id(order_id)
# ---------------------------------------consumer---------------------------------------------------------------
    
    def get_consumer_by_id(consumer_id: int) -> Consumer:
        return ConsumerDAO.get_consumer_by_id(consumer_id)

    
    def get_all_consumers() -> List[Consumer]:
        return ConsumerDAO.get_all_consumers()
# -----------------------------------consumerOrder------------------------------------------------
    
    def get_consumer_order_by_id(order_id: int) -> ConsumerOrder:
        return ConsumerOrderDAO.get_consumer_order_by_id(order_id)

    
    def get_all_consumer_orders() -> List[ConsumerOrder]:
        return ConsumerOrderDAO.get_all_consumer_orders()
# -----------------------------supplierTransaction------------------------------------------------------------------
    
    def get_supplier_transaction_by_id(transaction_id: int) -> SupplierTransaction:
        return SupplierTransactionDAO.get_supplier_transaction_by_id(transaction_id)

    
    def get_all_supplier_transactions() -> List[SupplierTransaction]:
        return SupplierTransactionDAO.get_all_supplier_transactions()
    
    
    def get_transactions_by_supplier_id(supplier_id: int) -> List[SupplierTransaction]:
        return SupplierTransactionDAO.get_transactions_by_supplier_id(supplier_id)

    
    def get_supplier_by_transaction_id(transaction_id: int) -> Optional[Supplier]:
        return SupplierTransactionDAO.get_supplier_by_transaction_id(transaction_id)

    
    def get_order_by_transaction_id(transaction_id: int) -> Optional[SupplierOrder]:
        return SupplierTransactionDAO.get_order_by_transaction_id(transaction_id)

    
    def get_transaction_by_order_id(order_id: int) -> Optional[SupplierTransaction]:
        return SupplierTransactionDAO.get_transaction_by_order_id(order_id)
# ---------------------------------------consumerTransaction-------------------------------------------------------------------------------
    
    def get_orders_by_consumer_id(consumer_id: int) -> List[ConsumerOrder]:
        # Retrieve orders by consumer ID
        return ConsumerOrderDAO.get_orders_by_consumer_id(consumer_id)

    
    def get_consumers_by_order_id(order_id: int) -> List[Consumer]:
        # Retrieve consumers by order ID
        return ConsumerOrderDAO.get_consumers_by_order_id(order_id)
    
    def get_consumer_transaction_by_id(transaction_id: int) -> ConsumerTransaction:
        return ConsumerTransactionDAO.get_consumer_transaction_by_id(transaction_id)

    
    def get_all_consumer_transactions() -> List[ConsumerTransaction]:
        return ConsumerTransactionDAO.get_all_consumer_transactions()

    
    def get_transactions_by_consumer_id(consumer_id: int) -> List[ConsumerTransaction]:
        # Retrieve transactions by consumer ID
        transactions = ConsumerTransactionDAO.get_transactions_by_consumer_id(consumer_id)
        return transactions

    
    def get_consumer_by_transaction_id(transaction_id: int) -> Optional[Consumer]:
        # Retrieve consumer by transaction ID
        consumer = ConsumerTransactionDAO.get_consumer_by_transaction_id(transaction_id)
        return consumer

    
    def get_order_by_transaction_id(transaction_id: int) -> Optional[ConsumerOrder]:
        # Retrieve order by transaction ID
        order = ConsumerTransactionDAO.get_order_by_transaction_id(transaction_id)
        return order

    
    def get_transaction_by_order_id(order_id: int) -> Optional[ConsumerTransaction]:
        # Retrieve transaction by order ID
        transaction = ConsumerTransactionDAO.get_transaction_by_order_id(order_id)
        return transaction


class Mutation:
    
    def create_supplier(name: str, address: str, contact: str, email: str) -> Supplier:
        return SupplierDAO.create_supplier(name, address, contact, email)
    
    def update_supplier(supplier_id: int, name: str = None, address: str = None, contact: str = None, email: str = None) -> Supplier:
        return SupplierDAO.update_supplier(supplier_id, name, address, contact, email)

    
    def delete_supplier(supplier_id: int) -> Supplier:
        return SupplierDAO.delete_supplier(supplier_id)

    
    def create_product(name: str, description: str, price: float) -> Product:
        return ProductDAO.create_product(name, description, price)

    
    def update_product(product_id: int, name: str = None, description: str = None, price: float = None) -> Product:
        return ProductDAO.update_product(product_id, name, description, price)

    
    def delete_product(product_id: int) -> Product:
        return ProductDAO.delete_product(product_id)

    
    def create_stock(product_id: int, quantity: int, location: str, threshold: int) -> Stock:
        return StockDAO.create_stock(product_id, quantity, location, threshold)

    
    def update_stock(stock_id: int, quantity: int = None, location: str = None, threshold: int = None) -> Stock:
        return StockDAO.update_stock(stock_id, quantity, location, threshold)

    
    def delete_stock(stock_id: int) -> Stock:
        return StockDAO.delete_stock(stock_id)
    
    
    def create_supplier_order(self, supplier_id: int, product_id: int, stock_id: int, quantity: int, order_date: str) -> SupplierOrder:
        return SupplierOrderDAO.create_supplier_order(supplier_id, product_id, stock_id, quantity, order_date)
    
    def update_supplier_order(order_id: int, quantity: int = None, order_date: str = None) -> SupplierOrder:
        return SupplierOrderDAO.update_supplier_order(order_id, quantity, order_date)

    
    def delete_supplier_order(order_id: int) -> SupplierOrder:
        return SupplierOrderDAO.delete_supplier_order(order_id)

    
    def create_consumer(name: str, address: str, contact: str, email: str) -> Consumer:
        return ConsumerDAO.create_consumer(name, address, contact, email)

    
    def update_consumer(consumer_id: int, name: str = None, address: str = None, contact: str = None, email: str=None) -> Consumer:
        return ConsumerDAO.update_consumer(consumer_id, name, address, contact, email)

    
    def delete_consumer(consumer_id: int) -> Consumer:
        return ConsumerDAO.delete_consumer(consumer_id)

    
    def create_consumer_order(consumer_id: int, product_id: int, quantity: int, order_date: str) -> ConsumerOrder:
        return ConsumerOrderDAO.create_consumer_order(consumer_id, product_id, quantity, order_date)

    
    def update_consumer_order(order_id: int, quantity: int = None, order_date: str = None) -> ConsumerOrder:
        return ConsumerOrderDAO.update_consumer_order(order_id, quantity, order_date)

    
    def delete_consumer_order(order_id: int) -> ConsumerOrder:
        return ConsumerOrderDAO.delete_consumer_order(order_id)

    
    def create_supplier_transaction(supplier_id: int, order_id: int, transaction_date: str) -> SupplierTransaction:
        supplier = SupplierDAO.get_supplier_by_id(supplier_id)
        order = SupplierOrderDAO.get_supplier_order_by_id(order_id)
        if supplier and order:
            transaction = SupplierTransactionDAO.create_supplier_transaction(supplier_id, order_id, transaction_date)
            return transaction
        else:
            raise ValueError("Invalid supplier ID or order ID")
    
    def update_supplier_transaction(transaction_id: int, transaction_date: str = None) -> SupplierTransaction:
        transaction = SupplierTransactionDAO.update_supplier_transaction(transaction_id, transaction_date)
        if not transaction:
            raise ValueError("Invalid transaction ID")
        return transaction

    
    def delete_supplier_transaction(transaction_id: int) -> SupplierTransaction:
        transaction = SupplierTransactionDAO.delete_supplier_transaction(transaction_id)
        if not transaction:
            raise ValueError("Invalid transaction ID")
        return transaction
#--------------------------------consumerTransaction----------------------------------------------------------------------------------------------------------- 
    
    def create_consumer_transaction(consumer_id: int, order_id: int, transaction_date: str) -> ConsumerTransaction:
        consumer = ConsumerDAO.get_consumer_by_id(consumer_id)
        order = ConsumerOrderDAO.get_consumer_order_by_id(order_id)
        if consumer and order:
            transaction = ConsumerTransactionDAO.create_consumer_transaction(consumer_id, order_id, transaction_date)
            return transaction
        else:
            raise ValueError("Invalid consumer ID or order ID")

    
    def update_consumer_transaction(transaction_id: int, transaction_date: str = None) -> ConsumerTransaction:
        transaction = ConsumerTransactionDAO.update_consumer_transaction(transaction_id, transaction_date)
        if not transaction:
            raise ValueError("Invalid transaction ID")
        return transaction

    
    def delete_consumer_transaction(transaction_id: int) -> ConsumerTransaction:
        transaction = ConsumerTransactionDAO.delete_consumer_transaction(transaction_id)
        if not transaction:
            raise ValueError("Invalid transaction ID")
        return transaction
