size = ['S', 'M', 'L', 'XL']
garment = ['Shirt', 'Trousers', 'Jacket']
clothes = {(x, y) for x in size for y in garment}
print(clothes)