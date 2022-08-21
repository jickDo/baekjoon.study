from sys import stdin

T=int(stdin.readline())
card=[0]*T
result=[]
avg=0
sum,cnt=0,0
small,big=0,0
for i in range(T):
    card[i]=int(stdin.readline())
    avg+=card[i]
card.sort()
avg=avg/T

for k in range(T):
    if card[k]<avg:
        small+=1
    else:
        big+=1
if small>big:
    for j in range(T-1):   
        sum=card[0]+card[1]
        cnt+=sum
        card.pop(0)
        card.insert(0, sum)
        card.pop(1)
else:
    for c in range(T-1):
        sum=card[0]+card[T-c]
        cnt+=sum
        card.pop(0)
        card.insert(0,sum)
        card.pop(T-c)

print(cnt)
