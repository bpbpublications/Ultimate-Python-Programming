prices = {'pencil': 23, 'pen': 34, 'eraser': 12, 'sharpener': 13, 'marker': 30}
costly_products = [product for product, price in prices.items() if price > 20]
print(costly_products)
