#products
#14:40-15:40  学习记账程式的编写

products = []
while True:
	name = input('请输入商品名称:')
	if name == 'q':   #-------- if 语句记得写冒号！
	   break
	price = input('请输入商品价格:')
	#p = []
	#p.append(name)
	#p.append(price)
	#products.append(p)

	#简洁写法 p = [name,price] 
	# products.append(p)
	products.append([name,price]) #--最简
print(products)


'''
github 后续上传更新指令 
git add products.py
git commit -m " add procducts.py
git push origin master
'''

'''github 初次上传创建文件指令
echo "# products" >> README.md
git init
git commit -m "first commit"
git remote add origin https://github.com/githubsina/products.git	
git push -u origin master
'''