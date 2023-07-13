from schemas import *
import json

def lambda_handler(event, context):
      print(event)
      if event.get('info').get('fieldName')=='get_product_by_id':
            
            return Query.get_product_by_id(event.get('arguments').get('product_id'))
    
        
    