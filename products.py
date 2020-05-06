import os
products=[]

if os.path.isfile('product.csv'):
	print('恭喜中獎')
	with open('product.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line: #不能空格
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)

else:
	print('找不到檔案....')

#讀取檔案


#使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格: ')
	price = int(price)
	products.append([(name), (price)])
print(products)
#寫入檔案
with open ('product.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
