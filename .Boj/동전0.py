num, sum=map(int, input().split())
coins=[]
cnt=0
coin=0
for i in range(num):
    coin=int(input())
    coins.append(coin)

coins.reverse()

for i in range(num):
    if coins[i]>sum:
        continue
    elif coins[i]<=sum:
        cnt+=(sum//coins[i])
        sum=sum%coins[i]

print(cnt)