products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	price = int(price)
	products.append([(name), (price)])
print(products)

with open ('product.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
