from sys import stdin

n,m=map(int, stdin.readline().strip().split())
arr=list(map(int,stdin.readline().strip().split() ))
arr.sort()
res=0
for i in range(n):
    for j in range(i+1,n):
        if arr[i]==arr[j]:
            continue
        elif arr[i]!=arr[j]:
            res+=1

print(res)