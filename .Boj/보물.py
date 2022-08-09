T=int(input())
sum=0
listA=list(map(int, input().split()))
listB=list(map(int, input().split()))

listA.sort()
listB.sort()
listA.reverse()

for i in range(T):
    sum+=listA[i]*listB[i]

print(sum)