import json
import csv

products = []

with open('products.txt') as f:
    for line in f:
        split = (line.split(':'))
        products.append({'name': split[0], 'category': split[1], 'price': float(split[2])})

    with open('products_export.json', 'w') as f:
        json.dump(products, f, indent=2)
    
    with open('products.export.csv', 'w') as f:
        for items in products:
            keys = list(items.keys())
        writer = csv.DictWriter(f, fieldnames=[keys[0], keys[1], keys[2]])
        writer.writeheader()
        writer.writerows(products)