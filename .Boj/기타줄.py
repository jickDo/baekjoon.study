from sys import stdin
line,brand=map(int, stdin.readline().split())
result=0
min_price=[]
min_price2=[]
min_a,min_b,num=0,0,0
for i in range(brand):
    big,small=map(int, stdin.readline().split())
    min_price.append(big)
    min_price2.append(small)

min_a=min(min_price) #세트값
min_b=min(min_price2)

if min_a>min_b*6:
    result+=min_b*line
else:
    result+=min_a*(line//6)
    if min_a<(line%6)*min_b:
        result+=min_a
    else:
        result+=(line%6)*min_b

print(result)
