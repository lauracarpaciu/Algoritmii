orders = [
    {'name': "Ion Popescu",
     'clientCode':"Ab12",
     'products':{'sku': "sku",
                 'quantity':1,
                 "price": 25}},

    {'name': "Ion Popescu",
     'clientCode': "Ab12",
     'products': {'sku': "sku",
                  'quantity': 1,
                  "price": 25}},

    {'name': "Ion Popescu",
     'clientCode': "Ab12",
     'products': {'sku': "sku",
                  'quantity': 1,
                  "price": 25}},
]

for order in orders:
    clientCode = order.get(clientCode)
    for product in order.get(product):
        productCode=product.find("sku")