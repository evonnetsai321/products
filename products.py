products=[]

while True:
    name=input("請輸入商品名稱:")

    if name=='q':
        break
    price=input('請輸入商品價格:')
    price=int(price)
    p=[name,price] #小清單 
    products.append(p)
    
    
print(products)

for product in products:
    print(product[0],'的價格是',product[1])

with open('products.csv','w',encoding='utf-8') as f:
    f.write('商品,價格\n')
    for product in products:
        f.write( str(p[0]) + ',' +str(p[1])+ '\n' )






















