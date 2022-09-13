from sys import stdin

tree,need=map(int, stdin.readline().strip().split())

arr=list(map(int, stdin.readline().strip().split()))

start,end=0,max(arr)
result=0

while start<=end:
    total=0
    mid=(start+end)//2
    for i in arr:
        if i>mid:
            total=total+(i-mid)
    if total<need:
        end=mid-1
    else:
        result=mid
        start=mid+1


print(result)
    