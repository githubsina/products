import os 

#读取档案
def read_file(filename):
	products = []
	with open (filename, 'r' , encoding='utf-8') as f:
		for line in f:
			if '商品,价格' in line:
				continue #是指跳过此回合，继续进行if中下一回合，如果break，则跳出if循环
			name, price = line.strip().split(',')
			products.append([name,price])
	return products


# 让使用者输入--------------------------------------------
def user_input(products):
		while True:
			name = input('请输入商品名称:')
			if name == 'q':         #----------------- if 语句记得写冒号！
			   break
			price = input('请输入商品价格:')
			price = int(price)
			products.append([name,price]) 
		print(products)
		return products

			#p = []
			#p.append(name)
			#p.append(price)
			#products.append(p)

			#简洁写法 p = [name,price] 
			# products.append(p)


# 输出购买记录-------------------------------------------
def print_products(products):
	for p in products:
		print(p[0],'的价格是:', p[1])



# 写入档案
def write_file(filename, products):
	with open(filename,'w', encoding='utf-8') as f:
		f.write('商品，价格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')


# 开始执行
def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #检查档案是否在
		print('yeah!find you!')#相对路径，是在相同程式文件夹下
		products = read_file(filename)
	else:
		print('找不到档案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv',products)

main()

