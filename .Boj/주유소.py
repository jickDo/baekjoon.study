city_num=int(input())
distance=list(map(int, input().split()))
oil_price=list(map(int, input().split()))
oil_price.pop()
sum=0
dis=0
min_price=min(oil_price)
num=oil_price.index(min_price) #가장싼주유소 인덱스

for i in range(0,num):
    if oil_price[i]>=oil_price[i+1]:
        sum=sum+(oil_price[i]*distance[i])
    elif oil_price[i]<oil_price[i+1]:
        sum=sum+(oil_price[i]*distance[i])
        oil_price[i+1]=oil_price[i]

for j in range(num,len(distance)):
    dis+=distance[j]

sum=sum+(dis*min_price)
print(sum)