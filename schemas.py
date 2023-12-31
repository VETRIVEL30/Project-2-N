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
    def get_supplier_by_id(self, supplier_id: int) -> Supplier:
        SupplierDao = SupplierDAO.get_supplier_by_id(supplier_id)
        Supplier = {}
        Supplier["supplier_id"] = SupplierDao.supplier_id
        Supplier["name"] = SupplierDao.name
        Supplier["address"] = SupplierDao.address
        Supplier["contact"] = SupplierDao.contact
        Supplier["email"] = SupplierDao.email
        return Supplier


    def get_all_suppliers(self) -> List[Supplier]:
        suppliers = SupplierDAO.get_all_suppliers()
        Suppliers = []
        for supplier in suppliers:
            Supplier = {}
            Supplier["supplier_id"] = supplier.supplier_id
            Supplier["name"] = supplier.name
            Supplier["address"] = supplier.address
            Supplier["contact"] = supplier.contact
            Supplier["email"] = supplier.email
            Suppliers.append(Supplier)
        return Suppliers


    def get_product_by_id(self, product_id: int) -> Product:
        productDao = ProductDAO.get_product_by_id(product_id)
        Product = {}
        Product["product_id"]=productDao.product_id
        Product["name"]=productDao.name
        Product["price"] = productDao.price
        Product["description"] = productDao.description
        return Product


    def get_all_products(self) -> List[Product]:
        products = ProductDAO.get_all_products()
        Products = []
        for product in products:
            Product = {}
            Product["product_id"]=product.product_id
            Product["name"]=product.name
            Product["price"] = product.price
            Product["description"] = product.description
            Products.append(Product)
        return Products


    def get_stock_by_id(self, stock_id: int) -> Stock:
        StockDao = StockDAO.get_stock_by_id(stock_id)
        Stock = {}
        Stock["stock_id"] = StockDao.stock_id
        Stock["product_id"] = StockDao.product_id
        Stock["quantity"] = StockDao.quantity
        Stock["location"] = StockDao.location
        Stock["threshold"] = StockDao.threshold
        return Stock


    def get_all_stocks(self) -> List[Stock]:
        stocks = StockDAO.get_all_stocks()
        Stocks = []
        for stock in stocks:
            Stock = {}
            Stock["stock_id"] = stock.stock_id
            Stock["product_id"] = stock.product_id
            Stock["quantity"] = stock.quantity
            Stock["location"] = stock.location
            Stock["threshold"] = stock.threshold
            Stocks.append(Stock)
        return Stocks
    
#------------------------------supplier order--------------------------------------------------------------------------------------------------------------------
        
    def get_supplier_order_by_id(self, order_id: int) -> SupplierOrder:
        supplier_order_dao = SupplierOrderDAO.get_supplier_order_by_id(order_id)
        supplier_order = {}

        if supplier_order_dao:
            supplier_order["order_id"] = supplier_order_dao.order_id
            supplier_order["supplier_id"] = supplier_order_dao.supplier_id
            supplier_order["product_id"] = supplier_order_dao.product_id
            supplier_order["stock_id"] = supplier_order_dao.stock_id
            supplier_order["quantity"] = supplier_order_dao.quantity
            supplier_order["order_date"] = supplier_order_dao.order_date.isoformat()

            # Fetch the product information based on the product_id
            product = ProductDAO.get_product_by_id(supplier_order_dao.product_id)
            if product:
                # Calculate the total price using the product price and quantity
                total_price = supplier_order_dao.quantity * product.price
                supplier_order["total_price"] = total_price
            else:
                supplier_order["total_price"] = None

        return supplier_order


    def get_all_supplier_orders() -> List[SupplierOrder]:
        supplier_orders = SupplierOrder.query.all()
        SupplierOrderList = []

        for supplier_order in supplier_orders:
            supplier_order_data = {}
            supplier_order_data["order_id"] = supplier_order.order_id
            supplier_order_data["supplier_id"] = supplier_order.supplier_id
            supplier_order_data["product_id"] = supplier_order.product_id
            supplier_order_data["stock_id"] = supplier_order.stock_id
            supplier_order_data["quantity"] = supplier_order.quantity
            supplier_order_data["order_date"] = supplier_order.order_date.isoformat()

            # Fetch the product information based on the product_id
            product = ProductDAO.get_product_by_id(supplier_order.product_id)
            if product:
                # Calculate the total price using the product price and quantity
                total_price = supplier_order.quantity * product.price
                supplier_order_data["total_price"] = total_price
            else:
                supplier_order_data["total_price"] = None

            SupplierOrderList.append(supplier_order_data)

        return SupplierOrderList


    def get_orders_by_supplier_id(self, supplier_id: int) -> List[SupplierOrder]:
        supplier_orders = SupplierOrderDAO.get_orders_by_supplier_id(supplier_id)
        supplier_order_list = []

        for supplier_order_dao in supplier_orders:
            supplier_order = {}

            supplier_order["order_id"] = supplier_order_dao.order_id
            supplier_order["supplier_id"] = supplier_order_dao.supplier_id
            supplier_order["product_id"] = supplier_order_dao.product_id
            supplier_order["stock_id"] = supplier_order_dao.stock_id
            supplier_order["quantity"] = supplier_order_dao.quantity
            supplier_order["order_date"] = supplier_order_dao.order_date.isoformat()

            # Fetch the product information based on the product_id
            product = ProductDAO.get_product_by_id(supplier_order_dao.product_id)
            if product:
                # Calculate the total price using the product price and quantity
                total_price = supplier_order_dao.quantity * product.price
                supplier_order["total_price"] = total_price
            else:
                supplier_order["total_price"] = None

            supplier_order_list.append(supplier_order)

        return supplier_order_list


    def get_suppliers_by_order_id(self, order_id: int) -> List[Supplier]:
        suppliers = SupplierOrderDAO.get_suppliers_by_order_id(order_id)
        Suppliers = []
        for supplier in suppliers:
            Supplier = {}
            Supplier["supplier_id"] = supplier.supplier_id
            Supplier["name"] = supplier.name
            Supplier["address"] = supplier.address
            Supplier["contact"] = supplier.contact
            Suppliers.append(Supplier)
        return Suppliers
# ---------------------------------------consumer---------------------------------------------------------------
    
    def get_consumer_by_id(self, consumer_id: int) -> Consumer:
        ConsumerDao = ConsumerDAO.get_consumer_by_id(consumer_id)
        Consumer = {}
        Consumer["consumer_id"] = ConsumerDao.consumer_id
        Consumer["name"] = ConsumerDao.name
        Consumer["address"] = ConsumerDao.address
        Consumer["contact"] = ConsumerDao.contact
        Consumer["email"] = ConsumerDao.email
        return Consumer


    def get_all_consumers(self) -> List[Consumer]:
        consumers = ConsumerDAO.get_all_consumers()
        Consumers = []
        for consumer in consumers:
            Consumer = {}
            Consumer["consumer_id"] = consumer.consumer_id
            Consumer["name"] = consumer.name
            Consumer["address"] = consumer.address
            Consumer["contact"] = consumer.contact
            Consumer["email"] = consumer.email
            Consumers.append(Consumer)
        return Consumers
# -----------------------------------consumerOrder------------------------------------------------
    
    def get_consumer_by_id(self, consumer_id: int) -> Consumer:
        ConsumerDao = ConsumerDAO.get_consumer_by_id(consumer_id)
        Consumer = {}
        Consumer["consumer_id"] = ConsumerDao.consumer_id
        Consumer["name"] = ConsumerDao.name
        Consumer["address"] = ConsumerDao.address
        Consumer["contact"] = ConsumerDao.contact
        Consumer["email"] = ConsumerDao.email
        return Consumer


    def get_all_consumers(self) -> List[Consumer]:
        consumers = ConsumerDAO.get_all_consumers()
        Consumers = []
        for consumer in consumers:
            Consumer = {}
            Consumer["consumer_id"] = consumer.consumer_id
            Consumer["name"] = consumer.name
            Consumer["address"] = consumer.address
            Consumer["contact"] = consumer.contact
            Consumer["email"] = consumer.email
            Consumers.append(Consumer)
        return Consumers
# -----------------------------supplierTransaction------------------------------------------------------------------
    def get_supplier_transaction_by_id(self, transaction_id: int) -> SupplierTransaction:
        SupplierTransactionDao = SupplierTransactionDAO.get_supplier_transaction_by_id(transaction_id)
        SupplierTransaction = {}
        SupplierTransaction["transaction_id"] = SupplierTransactionDao.transaction_id
        SupplierTransaction["supplier_id"] = SupplierTransactionDao.supplier_id
        SupplierTransaction["order_id"] = SupplierTransactionDao.order_id
        SupplierTransaction["transaction_date"] = SupplierTransactionDao.transaction_date.isoformat()

        # Retrieve the associated order
        order = SupplierOrderDAO.get_supplier_order_by_id(SupplierTransactionDao.order_id)
        SupplierTransaction["amount"] = order.quantity * order.product_price if order else None

        return SupplierTransaction


    def get_all_supplier_transactions(self) -> List[SupplierTransaction]:
        supplier_transactions = SupplierTransactionDAO.get_all_supplier_transactions()
        SupplierTransactions = []
        for supplier_transaction in supplier_transactions:
            SupplierTransaction = {}
            SupplierTransaction["transaction_id"] = supplier_transaction.transaction_id
            SupplierTransaction["supplier_id"] = supplier_transaction.supplier_id
            SupplierTransaction["order_id"] = supplier_transaction.order_id
            SupplierTransaction["transaction_date"] = supplier_transaction.transaction_date.isoformat()

            # Retrieve the associated order
            order = SupplierOrderDAO.get_supplier_order_by_id(supplier_transaction.order_id)
            SupplierTransaction["amount"] = order.quantity * order.product_price if order else None

            SupplierTransactions.append(SupplierTransaction)
        return SupplierTransactions


    def get_transactions_by_supplier_id(self, supplier_id: int) -> List[SupplierTransaction]:
        supplier_transactions = SupplierTransactionDAO.get_transactions_by_supplier_id(supplier_id)
        SupplierTransactions = []
        for supplier_transaction in supplier_transactions:
            SupplierTransaction = {}
            SupplierTransaction["transaction_id"] = supplier_transaction.transaction_id
            SupplierTransaction["supplier_id"] = supplier_transaction.supplier_id
            SupplierTransaction["order_id"] = supplier_transaction.order_id
            SupplierTransaction["transaction_date"] = supplier_transaction.transaction_date.isoformat()

            # Retrieve the associated order
            order = SupplierOrderDAO.get_supplier_order_by_id(supplier_transaction.order_id)
            SupplierTransaction["amount"] = order.quantity * order.product_price if order else None

            SupplierTransactions.append(SupplierTransaction)
        return SupplierTransactions


    def get_supplier_by_transaction_id(self, transaction_id: int) -> Optional[Supplier]:
        supplierDao = SupplierTransactionDAO.get_supplier_by_transaction_id(transaction_id)
        if not supplierDao:
            return None
        else:
            Supplier = {}
            Supplier["supplier_id"] = supplierDao.supplier_id
            Supplier["name"] = supplierDao.name
            Supplier["address"] = supplierDao.address
            Supplier["contact"] = supplierDao.contact
            return Supplier


    def get_Supplierorder_by_transaction_id(self, transaction_id: int) -> Optional[SupplierOrder]:
        orderDao = SupplierTransactionDAO.get_order_by_transaction_id(transaction_id)
        if not orderDao:
            return None
        else:
            Order = {}
            Order["order_id"] = orderDao.order_id
            Order["supplier_id"] = orderDao.supplier_id
            Order["product_id"] = orderDao.product_id
            Order["stock_id"] = orderDao.stock_id
            Order["quantity"] = orderDao.quantity
            Order["order_date"] = orderDao.order_date.isoformat()
            Order["amount"] = orderDao.quantity * orderDao.product_price
            return Order


    def get_Suppliertransaction_by_order_id(self, order_id: int) -> Optional[SupplierTransaction]:
        transactionDao = SupplierTransactionDAO.get_transaction_by_order_id(order_id)
        if not transactionDao:
            return None
        else:
            Transaction = {}
            Transaction["transaction_id"] = transactionDao.transaction_id
            Transaction["supplier_id"] = transactionDao.supplier_id
            Transaction["order_id"] = transactionDao.order_id
            Transaction["transaction_date"] = transactionDao.transaction_date.isoformat()

            # Retrieve the associated order
            order = SupplierOrderDAO.get_supplier_order_by_id(transactionDao.order_id)
            Transaction["amount"] = order.quantity * order.product_price if order else None

            return Transaction

# ---------------------------------------consumerOrder-------------------------------------------------------------------------------
        
    def get_orders_by_consumer_id(consumer_id: int) -> List[ConsumerOrder]:
        consumer_orders = ConsumerOrderDAO.get_orders_by_consumer_id(consumer_id)
        ConsumerOrders = []
        for consumer_order in consumer_orders:
            ConsumerOrder = {}
            ConsumerOrder["order_id"] = consumer_order.order_id
            ConsumerOrder["consumer_id"] = consumer_order.consumer_id
            ConsumerOrder["product_id"] = consumer_order.product_id
            ConsumerOrder["quantity"] = consumer_order.quantity
            ConsumerOrder["order_date"] = consumer_order.order_date.isoformat()

            # Fetch the product information based on the product_id
            product = ProductDAO.get_product_by_id(consumer_order.product_id)
            if product:
                # Calculate the total price using the product price and quantity
                total_price = consumer_order.quantity * product.price
                ConsumerOrder["total_price"] = total_price
            else:
                ConsumerOrder["total_price"] = None

            ConsumerOrders.append(ConsumerOrder)
        return ConsumerOrders


    def get_consumers_by_order_id(order_id: int) -> List[Consumer]:
        consumers = ConsumerOrderDAO.get_consumers_by_order_id(order_id)
        Consumers = []
        for consumer in consumers:
            Consumer = {}
            Consumer["consumer_id"] = consumer.consumer_id
            Consumer["name"] = consumer.name
            Consumer["address"] = consumer.address
            Consumer["contact"] = consumer.contact
            Consumer["email"] = consumer.email
            Consumers.append(Consumer)
        return Consumers


    def get_all_consumer_orders() -> List[ConsumerOrder]:
        consumer_orders = ConsumerOrderDAO.get_all_consumer_orders()
        ConsumerOrders = []
        for consumer_order in consumer_orders:
            ConsumerOrder = {}
            ConsumerOrder["order_id"] = consumer_order.order_id
            ConsumerOrder["consumer_id"] = consumer_order.consumer_id
            ConsumerOrder["product_id"] = consumer_order.product_id
            ConsumerOrder["quantity"] = consumer_order.quantity
            ConsumerOrder["order_date"] = consumer_order.order_date.isoformat()

            # Fetch the product information based on the product_id
            product = ProductDAO.get_product_by_id(consumer_order.product_id)
            if product:
                # Calculate the total price using the product price and quantity
                total_price = consumer_order.quantity * product.price
                ConsumerOrder["total_price"] = total_price
            else:
                ConsumerOrder["total_price"] = None

            ConsumerOrders.append(ConsumerOrder)
        return ConsumerOrders
# ======================================consumerTransaction=====================================================================================================================================
    def get_consumer_transaction_by_id(self, transaction_id: int) -> ConsumerTransaction:
        ConsumerTransactionDao = ConsumerTransactionDAO.get_consumer_by_transaction_id(transaction_id)
        ConsumerTransaction = {}
        ConsumerTransaction["transaction_id"] = ConsumerTransactionDao.transaction_id
        ConsumerTransaction["consumer_id"] = ConsumerTransactionDao.consumer_id
        ConsumerTransaction["order_id"] = ConsumerTransactionDao.order_id
        ConsumerTransaction["transaction_date"] = ConsumerTransactionDao.transaction_date.isoformat()

        # Retrieve the associated order
        order = ConsumerOrderDAO.get_consumer_order_by_id(ConsumerTransactionDao.order_id)
        ConsumerTransaction["amount"] = order.quantity * order.product.price if order else None

        return ConsumerTransaction


    def get_all_consumer_transactions(self) -> List[ConsumerTransaction]:
        consumer_transactions = ConsumerTransactionDAO.get_all_consumer_transactions()
        ConsumerTransactions = []
        for consumer_transaction in consumer_transactions:
            ConsumerTransaction = {}
            ConsumerTransaction["transaction_id"] = consumer_transaction.transaction_id
            ConsumerTransaction["consumer_id"] = consumer_transaction.consumer_id
            ConsumerTransaction["order_id"] = consumer_transaction.order_id
            ConsumerTransaction["transaction_date"] = consumer_transaction.transaction_date.isoformat()

            # Retrieve the associated order
            order = ConsumerOrderDAO.get_consumer_order_by_id(consumer_transaction.order_id)
            ConsumerTransaction["amount"] = order.quantity * order.product.price if order else None

            ConsumerTransactions.append(ConsumerTransaction)
        return ConsumerTransactions


    def get_transactions_by_consumer_id(self, consumer_id: int) -> List[ConsumerTransaction]:
        transactions = ConsumerTransactionDAO.get_transactions_by_consumer_id(consumer_id)
        Transactions = []
        for transaction in transactions:
            Transaction = {}
            Transaction["transaction_id"] = transaction.transaction_id
            Transaction["consumer_id"] = transaction.consumer_id
            Transaction["order_id"] = transaction.order_id
            Transaction["transaction_date"] = transaction.transaction_date.isoformat()

            # Retrieve the associated order
            order = ConsumerOrderDAO.get_consumer_order_by_id(transaction.order_id)
            Transaction["amount"] = order.quantity * order.product.price if order else None

            Transactions.append(Transaction)
        return Transactions


    def get_consumer_by_transaction_id(self, transaction_id: int) -> Optional[Consumer]:
        consumerDao = ConsumerTransactionDAO.get_consumer_by_transaction_id(transaction_id)
        if not consumerDao:
            return None
        else:
            Consumer = {}
            Consumer["consumer_id"] = consumerDao.consumer_id
            Consumer["name"] = consumerDao.name
            Consumer["address"] = consumerDao.address
            Consumer["contact"] = consumerDao.contact
            Consumer["email"] = consumerDao.email
            return Consumer


    def get_Consumerorder_by_transaction_id(self, transaction_id: int) -> Optional[ConsumerOrder]:
        orderDao = ConsumerTransactionDAO.get_order_by_transaction_id(transaction_id)
        if not orderDao:
            return None
        else:
            Order = {}
            Order["order_id"] = orderDao.order_id
            Order["consumer_id"] = orderDao.consumer_id
            Order["product_id"] = orderDao.product_id
            Order["quantity"] = orderDao.quantity
            Order["order_date"] = orderDao.order_date.isoformat()
            Order["amount"] = orderDao.quantity * orderDao.product.price
            return Order


    def get_Consumertransaction_by_order_id(self, order_id: int) -> Optional[ConsumerTransaction]:
        transactionDao = ConsumerTransactionDAO.get_transaction_by_order_id(order_id)
        if not transactionDao:
            return None
        else:
            Transaction = {}
            Transaction["transaction_id"] = transactionDao.transaction_id
            Transaction["consumer_id"] = transactionDao.consumer_id
            Transaction["order_id"] = transactionDao.order_id
            Transaction["transaction_date"] = transactionDao.transaction_date.isoformat()

            # Retrieve the associated order
            order = ConsumerOrderDAO.get_consumer_order_by_id(transactionDao.order_id)
            Transaction["amount"] = order.quantity * order.product.price if order else None

            return Transaction


class Mutation:
    
    def create_supplier(name: str, address: str, contact: str, email: str) -> Supplier:
        SupplierDao=SupplierDAO.create_supplier(name, address, contact, email)
        Supplier={}
        Supplier["name"]=SupplierDao.name
        Supplier["address"]=SupplierDao.address
        Supplier["contact"]=SupplierDao.contact
        Supplier["email"]=SupplierDao.email
        return Supplier
    
    def update_supplier(supplier_id: int, name: str = None, address: str = None, contact: str = None, email: str = None) -> Supplier:
        SupplierDao=SupplierDAO.update_supplier(name, address, contact, email)
        Supplier={}
        Supplier["supplier_id"]=SupplierDao.supplier_id
        Supplier["name"]=SupplierDao.name
        Supplier["address"]=SupplierDao.address
        Supplier["contact"]=SupplierDao.contact
        Supplier["email"]=SupplierDao.email
        return Supplier
    
    def delete_supplier(supplier_id: int) -> Supplier:
        supplier_id = SupplierDAO.delete_supplier(supplier_id)
        return {"supplier_id": supplier_id}


    
    def create_product(name: str, description: str, price: float) -> Product:
        ProductDao=ProductDAO.create_product(name, description, price)
        Product={}
        Product["name"]=ProductDao.name
        Product["description"]=ProductDao.description
        Product["price"]=ProductDao.price
        return Product


    
    def update_product(product_id: int, name: str = None, description: str = None, price: float = None) -> Product:
        ProductDao=ProductDAO.update_product(name, description, price)
        Product={}
        Product["name"]=ProductDao.name
        Product["description"]=ProductDao.description
        Product["price"]=ProductDao.price
        return Product

    
    def delete_product(product_id: int) -> Product:
        product_id = ProductDAO.delete_product(product_id)
        return {"product_id": product_id}

    
    def create_stock(self, product_id: int, quantity: int, location: str, threshold: int) -> Stock:
        StockDao = StockDAO.create_stock(product_id, quantity, location, threshold)
        Stock = {}
        Stock["product_id"] = StockDao.product_id
        Stock["quantity"] = StockDao.quantity
        Stock["location"] = StockDao.location
        Stock["threshold"] = StockDao.threshold
        return Stock


    def update_stock(self, stock_id: int, quantity: int = None, location: str = None, threshold: int = None) -> Stock:
        StockDao = StockDAO.update_stock(stock_id, quantity, location, threshold)
        Stock = {}
        Stock["stock_id"] = StockDao.stock_id
        Stock["quantity"] = StockDao.quantity
        Stock["location"] = StockDao.location
        Stock["threshold"] = StockDao.threshold
        return Stock


    def delete_stock(self, stock_id: int) -> Stock:
        stock_id = StockDAO.delete_stock(stock_id)
        return {"stock_id": stock_id}
    
    def create_supplier_order(supplier_id: int, product_id: int, stock_id: int, quantity: int, order_date: str) -> SupplierOrder:
        supplier_order_dao = SupplierOrderDAO.create_supplier_order(supplier_id, product_id, stock_id, quantity, order_date)
        product = ProductDAO.get_product_by_id(product_id)
        
        if product:
            total_price = quantity * product.price
        else:
            total_price = 0.0

        supplier_order = {}
        supplier_order["supplier_id"] = supplier_order_dao.supplier_id
        supplier_order["product_id"] = supplier_order_dao.product_id
        supplier_order["stock_id"] = supplier_order_dao.stock_id
        supplier_order["quantity"] = supplier_order_dao.quantity
        supplier_order["order_date"] = supplier_order_dao.order_date.isoformat()
        supplier_order["total_price"] = total_price

        return supplier_order


    def update_supplier_order(self, order_id: int, quantity: int = None, order_date: str = None) -> SupplierOrder:
        supplier_order_dao = SupplierOrderDAO.update_supplier_order(order_id, quantity, order_date)
        supplier_order = {}

        if supplier_order_dao:
            supplier_order["order_id"] = supplier_order_dao.order_id
            supplier_order["quantity"] = supplier_order_dao.quantity
            supplier_order["order_date"] = supplier_order_dao.order_date.isoformat()

            product = ProductDAO.get_product_by_id(supplier_order_dao.product_id)
            if product:
                supplier_order["total_price"] = supplier_order_dao.quantity * product.price
            else:
                supplier_order["total_price"] = 0.0

        return supplier_order


    def delete_supplier_order(self, order_id: int) -> SupplierOrder:
        order_id = SupplierOrderDAO.delete_supplier_order(order_id)
        return {"order_id": order_id}

    
    def create_consumer(self, name: str, address: str, contact: str, email: str) -> Consumer:
        ConsumerDao = ConsumerDAO.create_consumer(name, address, contact, email)
        Consumer = {}
        Consumer["name"] = ConsumerDao.name
        Consumer["address"] = ConsumerDao.address
        Consumer["contact"] = ConsumerDao.contact
        Consumer["email"] = ConsumerDao.email
        return Consumer


    def update_consumer(self, consumer_id: int, name: str = None, address: str = None, contact: str = None, email: str=None) -> Consumer:
        ConsumerDao = ConsumerDAO.update_consumer(consumer_id, name, address, contact, email)
        Consumer = {}
        Consumer["consumer_id"] = ConsumerDao.consumer_id
        Consumer["name"] = ConsumerDao.name
        Consumer["address"] = ConsumerDao.address
        Consumer["contact"] = ConsumerDao.contact
        Consumer["email"] = ConsumerDao.email
        return Consumer


    def delete_consumer(self, consumer_id: int) -> Consumer:
        consumer_id = ConsumerDAO.delete_consumer(consumer_id)
        return {"consumer_id": consumer_id}

    
    def create_consumer_order(self, consumer_id: int, product_id: int, quantity: int, order_date: str) -> ConsumerOrder:
        consumer_order_dao = ConsumerOrderDAO.create_consumer_order(consumer_id, product_id, quantity, order_date)
        consumer_order = {}

        if consumer_order_dao:
            consumer_order["consumer_id"] = consumer_order_dao.consumer_id
            consumer_order["product_id"] = consumer_order_dao.product_id
            consumer_order["quantity"] = consumer_order_dao.quantity
            consumer_order["order_date"] = consumer_order_dao.order_date.isoformat()

            product = ProductDAO.get_product_by_id(consumer_order_dao.product_id)
            if product:
                consumer_order["total_price"] = consumer_order_dao.quantity * product.price
            else:
                consumer_order["total_price"] = 0.0

        return consumer_order


    def update_consumer_order(self, order_id: int, quantity: int = None, order_date: str = None) -> ConsumerOrder:
        consumer_order_dao = ConsumerOrderDAO.update_consumer_order(order_id, quantity, order_date)
        consumer_order = {}

        if consumer_order_dao:
            consumer_order["order_id"] = consumer_order_dao.order_id
            consumer_order["quantity"] = consumer_order_dao.quantity
            consumer_order["order_date"] = consumer_order_dao.order_date.isoformat()

            product = ProductDAO.get_product_by_id(consumer_order_dao.product_id)
            if product:
                consumer_order["total_price"] = consumer_order_dao.quantity * product.price
            else:
                consumer_order["total_price"] = 0.0

        return consumer_order



    def delete_consumer_order(self, order_id: int) -> ConsumerOrder:
        order_id = ConsumerOrderDAO.delete_consumer_order(order_id)
        return {"order_id": order_id}
    
    def create_supplier_transaction(self, supplier_id: int, order_id: int, transaction_date: str) -> SupplierTransaction:
        supplier = SupplierDAO.get_supplier_by_id(supplier_id)
        order = SupplierOrderDAO.get_supplier_order_by_id(order_id)
        if supplier and order:
            transaction = SupplierTransactionDAO.create_supplier_transaction(supplier_id, order_id, transaction_date)
            SupplierTransaction = {}
            SupplierTransaction["supplier_id"] = transaction.supplier_id
            SupplierTransaction["order_id"] = transaction.order_id
            SupplierTransaction["transaction_date"] = transaction.transaction_date
            return SupplierTransaction
        else:
            raise ValueError("Invalid supplier ID or order ID")

    def update_supplier_transaction(self, transaction_id: int, transaction_date: str = None) -> SupplierTransaction:
        transaction = SupplierTransactionDAO.update_supplier_transaction(transaction_id, transaction_date)
        if not transaction:
            raise ValueError("Invalid transaction ID")
        SupplierTransaction = {}
        SupplierTransaction["transaction_id"] = transaction.transaction_id
        SupplierTransaction["transaction_date"] = transaction.transaction_date
        return SupplierTransaction


    def delete_supplier_transaction(self, transaction_id: int) -> SupplierTransaction:
        transaction = SupplierTransactionDAO.delete_supplier_transaction(transaction_id)
        if not transaction:
            raise ValueError("Invalid transaction ID")
        return {"transaction_id": transaction.transaction_id}
#--------------------------------consumerTransaction----------------------------------------------------------------------------------------------------------- 
    
    def create_consumer_transaction(self, consumer_id: int, order_id: int, transaction_date: str) -> ConsumerTransaction:
        consumer = ConsumerDAO.get_consumer_by_id(consumer_id)
        order = ConsumerOrderDAO.get_consumer_order_by_id(order_id)
        if consumer and order:
            transaction = ConsumerTransactionDAO.create_consumer_transaction(consumer_id, order_id, transaction_date)
            ConsumerTransaction = {}
            ConsumerTransaction["consumer_id"] = transaction.consumer_id
            ConsumerTransaction["order_id"] = transaction.order_id
            ConsumerTransaction["transaction_date"] = transaction.transaction_date
            return ConsumerTransaction
        else:
            raise ValueError("Invalid consumer ID or order ID")


    def update_consumer_transaction(self, transaction_id: int, transaction_date: str = None) -> ConsumerTransaction:
        transaction = ConsumerTransactionDAO.update_consumer_transaction(transaction_id, transaction_date)
        if not transaction:
            raise ValueError("Invalid transaction ID")
        ConsumerTransaction = {}
        ConsumerTransaction["transaction_id"] = transaction.transaction_id
        ConsumerTransaction["transaction_date"] = transaction.transaction_date
        return ConsumerTransaction


    def delete_consumer_transaction(self, transaction_id: int) -> ConsumerTransaction:
        transaction = ConsumerTransactionDAO.delete_consumer_transaction(transaction_id)
        if not transaction:
            raise ValueError("Invalid transaction ID")
        return {"transaction_id": transaction.transaction_id}