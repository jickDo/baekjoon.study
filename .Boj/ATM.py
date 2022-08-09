T=int(input())
ATM=list(map(int, input().split()))
ATM.sort()
sum,num=0,0
for i in range(T):
    num=ATM[i]*(T-i)
    sum+=num

print(sum)