from schemas import *
import json


# def lambda_handler(event, context):
#     print(event)
    
#     if event.get('info').get('fieldName') == 'get_supplier_by_id':
#         print(event)
#         supplier = Query.get_supplier_by_id(event.get('arguments').get('supplier_id'))
#         return supplier
    
#     elif event.get('info').get('fieldName') == 'get_all_suppliers':
#         print(event)
#         suppliers = Query.get_all_suppliers()
#         return suppliers

def lambda_handler(event, context):
    print(event)
    
    query = Query()  # Instantiate the Query class
    
    if event.get('info').get('fieldName') == 'get_supplier_by_id':
        print(event)
        supplier_id = event.get('arguments').get('supplier_id')
        supplier = query.get_supplier_by_id(supplier_id)
        return supplier
    
    elif event.get('info').get('fieldName') == 'get_all_suppliers':
        print(event)
        suppliers = query.get_all_suppliers()
        return suppliers


    elif event.get('info').get('fieldName') == 'get_product_by_id':
        return query.get_product_by_id(event.get('arguments').get('product_id'))
    
    elif event.get('info').get('fieldName') == 'get_all_products':
        return query.get_all_products()
    
    elif event.get('info').get('fieldName') == 'get_stock_by_id':
        return query.get_stock_by_id(event.get('arguments').get('stock_id'))
    
    elif event.get('info').get('fieldName') == 'get_all_stocks':
        return query.get_all_stocks()
    
    elif event.get('info').get('fieldName') == 'get_supplier_order_by_id':
        return query.get_supplier_order_by_id(event.get('arguments').get('order_id'))
    
    elif event.get('info').get('fieldName') == 'get_all_supplier_orders':
        return query.get_all_supplier_orders()
    
    elif event.get('info').get('fieldName') == 'get_orders_by_supplier_id':
        return query.get_orders_by_supplier_id(event.get('arguments').get('supplier_id'))
    
    elif event.get('info').get('fieldName') == 'get_suppliers_by_order_id':
        return query.get_suppliers_by_order_id(event.get('arguments').get('order_id'))
    
    elif event.get('info').get('fieldName') == 'get_consumer_by_id':
        return query.get_consumer_by_id(event.get('arguments').get('consumer_id'))
    
    elif event.get('info').get('fieldName') == 'get_all_consumers':
        return query.get_all_consumers()
    
    elif event.get('info').get('fieldName') == 'get_consumers_by_order_id':
        return query.get_consumers_by_order_id(event.get('arguments').get('order_id'))
    
    elif event.get('info').get('fieldName') == 'get_all_consumer_orders':
        return query.get_all_consumer_orders()
    
    elif event.get('info').get('fieldName') == 'get_orders_by_consumer_id':
        return query.get_orders_by_consumer_id(event.get('arguments').get('consumer_id'))
    
    elif event.get('info').get('fieldName') == 'get_consumers_by_order_id':
        return query.get_consumers_by_order_id(event.get('arguments').get('order_id'))
    
    elif event.get('info').get('fieldName') == 'get_supplier_transaction_by_id':
        return query.get_supplier_transaction_by_id(event.get('arguments').get('transaction_id'))
    
    elif event.get('info').get('fieldName') == 'get_all_supplier_transactions':
        return query.get_all_supplier_transactions()
    
    elif event.get('info').get('fieldName') == 'get_transactions_by_supplier_id':
        return query.get_transactions_by_supplier_id(event.get('arguments').get('supplier_id'))
    
    elif event.get('info').get('fieldName') == 'get_supplier_by_transaction_id':
        return query.get_supplier_by_transaction_id(event.get('arguments').get('transaction_id'))
    
    elif event.get('info').get('fieldName') == 'get_Supplierorder_by_transaction_id':
        return query.get_Supplierorder_by_transaction_id(event.get('arguments').get('transaction_id'))
    
    elif event.get('info').get('fieldName') == 'get_Suppliertransaction_by_order_id':
        return query.get_Suppliertransaction_by_order_id(event.get('arguments').get('order_id'))
    
    elif event.get('info').get('fieldName') == 'get_consumer_transaction_by_id':
        return query.get_consumer_transaction_by_id(event.get('arguments').get('transaction_id'))
    
    elif event.get('info').get('fieldName') == 'get_all_consumer_transactions':
        return query.get_all_consumer_transactions()
    
    elif event.get('info').get('fieldName') == 'get_transactions_by_consumer_id':
        return query.get_transactions_by_consumer_id(event.get('arguments').get('consumer_id'))
    
    elif event.get('info').get('fieldName') == 'get_consumer_by_transaction_id':
        return query.get_consumer_by_transaction_id(event.get('arguments').get('transaction_id'))
    
    elif event.get('info').get('fieldName') == 'get_Consumerorder_by_transaction_id':
        return query.get_Consumerorder_by_transaction_id(event.get('arguments').get('transaction_id'))
    
    elif event.get('info').get('fieldName') == 'get_Consumertransaction_by_order_id':
        return query.get_Consumertransaction_by_order_id(event.get('arguments').get('order_id'))
    
    elif event.get('info').get('fieldName') == 'create_supplier':
        print(event)
        csupplier = Mutation.create_supplier(
            event.get('arguments').get('name'),
            event.get('arguments').get('address'),
            event.get('arguments').get('contact'),
            event.get('arguments').get('email')
        )
        return csupplier
    
    elif event.get('info').get('fieldName') == 'update_supplier':
        print(event)
        usupplier = Mutation.update_supplier(
            event.get('arguments').get('supplier_id'),
            event.get('arguments').get('name'),
            event.get('arguments').get('address'),
            event.get('arguments').get('contact'),
            event.get('arguments').get('email')
        )
        return usupplier
    
    elif event.get('info').get('fieldName') == 'delete_supplier':
        print(event)
        dsupplier =  Mutation.delete_supplier(event.get('arguments').get('supplier_id'))
        return dsupplier
    
    elif event.get('info').get('fieldName') == 'create_product':
        return Mutation.create_product(
            event.get('arguments').get('name'),
            event.get('arguments').get('description'),
            event.get('arguments').get('price')
        )
    
    elif event.get('info').get('fieldName') == 'update_product':
        return Mutation.update_product(
            event.get('arguments').get('product_id'),
            event.get('arguments').get('name'),
            event.get('arguments').get('description'),
            event.get('arguments').get('price')
        )
    
    elif event.get('info').get('fieldName') == 'delete_product':
        return Mutation.delete_product(event.get('arguments').get('product_id'))
    
    elif event.get('info').get('fieldName') == 'create_stock':
        return Mutation().create_stock(
            event.get('arguments').get('product_id'),
            event.get('arguments').get('quantity'),
            event.get('arguments').get('location'),
            event.get('arguments').get('threshold')
        )
    
    elif event.get('info').get('fieldName') == 'update_stock':
        return Mutation().update_stock(
            event.get('arguments').get('stock_id'),
            event.get('arguments').get('quantity'),
            event.get('arguments').get('location'),
            event.get('arguments').get('threshold')
        )
    
    elif event.get('info').get('fieldName') == 'delete_stock':
        return Mutation().delete_stock(event.get('arguments').get('stock_id'))
    
    elif event.get('info').get('fieldName') == 'create_supplier_order':
        return Mutation().create_supplier_order(
            event.get('arguments').get('supplier_id'),
            event.get('arguments').get('product_id'),
            event.get('arguments').get('stock_id'),
            event.get('arguments').get('quantity'),
            event.get('arguments').get('order_date')
        )
    
    elif event.get('info').get('fieldName') == 'update_supplier_order':
        return Mutation().update_supplier_order(
            event.get('arguments').get('order_id'),
            event.get('arguments').get('quantity'),
            event.get('arguments').get('order_date')
        )
    
    elif event.get('info').get('fieldName') == 'delete_supplier_order':
        return Mutation().delete_supplier_order(event.get('arguments').get('order_id'))
    
    elif event.get('info').get('fieldName') == 'create_consumer':
        return Mutation().create_consumer(
            event.get('arguments').get('name'),
            event.get('arguments').get('address'),
            event.get('arguments').get('contact'),
            event.get('arguments').get('email')
        )
    
    elif event.get('info').get('fieldName') == 'update_consumer':
        return Mutation().update_consumer(
            event.get('arguments').get('consumer_id'),
            event.get('arguments').get('name'),
            event.get('arguments').get('address'),
            event.get('arguments').get('contact'),
            event.get('arguments').get('email')
        )
    
    elif event.get('info').get('fieldName') == 'delete_consumer':
        return Mutation().delete_consumer(event.get('arguments').get('consumer_id'))
    
    elif event.get('info').get('fieldName') == 'create_consumer_order':
        return Mutation().create_consumer_order(
            event.get('arguments').get('consumer_id'),
            event.get('arguments').get('product_id'),
            event.get('arguments').get('quantity'),
            event.get('arguments').get('order_date')
        )
    
    elif event.get('info').get('fieldName') == 'update_consumer_order':
        return Mutation().update_consumer_order(
            event.get('arguments').get('order_id'),
            event.get('arguments').get('quantity'),
            event.get('arguments').get('order_date')
        )
    
    elif event.get('info').get('fieldName') == 'delete_consumer_order':
        return Mutation().delete_consumer_order(event.get('arguments').get('order_id'))
    
    elif event.get('info').get('fieldName') == 'create_supplier_transaction':
        return Mutation().create_supplier_transaction(
            event.get('arguments').get('supplier_id'),
            event.get('arguments').get('order_id'),
            event.get('arguments').get('transaction_date')
        )
    
    elif event.get('info').get('fieldName') == 'update_supplier_transaction':
        return Mutation().update_supplier_transaction(
            event.get('arguments').get('transaction_id'),
            event.get('arguments').get('transaction_date')
        )
    
    elif event.get('info').get('fieldName') == 'delete_supplier_transaction':
        return Mutation().delete_supplier_transaction(event.get('arguments').get('transaction_id'))
    
    elif event.get('info').get('fieldName') == 'create_consumer_transaction':
        return Mutation().create_consumer_transaction(
            event.get('arguments').get('consumer_id'),
            event.get('arguments').get('order_id'),
            event.get('arguments').get('transaction_date')
        )
    
    elif event.get('info').get('fieldName') == 'update_consumer_transaction':
        return Mutation().update_consumer_transaction(
            event.get('arguments').get('transaction_id'),
            event.get('arguments').get('transaction_date')
        )
    
    elif event.get('info').get('fieldName') == 'delete_consumer_transaction':
        return Mutation().delete_consumer_transaction(event.get('arguments').get('transaction_id'))