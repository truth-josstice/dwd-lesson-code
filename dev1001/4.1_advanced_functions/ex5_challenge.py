# Challenge Exercise

# ONLY ATTEMPT IF YOU HAVE COMFORTABLY COMPLETED THE OTHER EXERCISES!

# Given a list of product dictionaries,
# use map, filter, reduce, and lambda functions to:
# 1. Get a list of names of all products that are in stock (stock > 0).
# 2. Calculate the total value of all 'Electronics' products currently in stock
# 3. (Challenge): Get a list of strings, where each string is "Product Name - $Price"
#       for all products in the 'Apparel' category.
# 4. (Extra Challenge): Refactor #3 to use a list comprehension.

products = [
    {'name': 'Laptop', 'price': 1200.00, 'stock': 10, 'category': 'Electronics'},
    {'name': 'T-Shirt', 'price': 20.00, 'stock': 50, 'category': 'Apparel'},
    {'name': 'Keyboard', 'price': 75.00, 'stock': 0, 'category': 'Electronics'},
    {'name': 'Mug', 'price': 15.00, 'stock': 100, 'category': 'Homeware'},
    {'name': 'Jeans', 'price': 60.00, 'stock': 0, 'category': 'Apparel'},
    {'name': 'Monitor', 'price': 300.00, 'stock': 5, 'category': 'Electronics'}
]

in_stock = map(lambda item: item.get('name'), filter(lambda x: x['stock'] > 0, products))
print(f'Items currently in stock: {list(in_stock)}')

total_price = map(lambda x: (x.get('price')) * (x.get('stock')), filter(lambda x: x['category'] == 'Electronics', products))
print(f'Total price of electronics category: ${sum(total_price):.2f}')

newlist = map(lambda x: str(f'{x['name']} - ${x['price']:.2f}'), filter(lambda x: x['category'] == 'Apparel', products))
print(list(newlist))

listcomp = [str(f'{x['name']} - ${x['price']:.2f}') for x in products if x['category'] == 'Apparel']
print(listcomp)