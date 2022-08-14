num=int(input())
a1,sum=1,0

while True:
    if sum>num: 
        a1-=2
        print(a1)
        break
    else:
        sum+=a1
        a1+=1
        continue