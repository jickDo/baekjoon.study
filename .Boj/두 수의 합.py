from sys import stdin

n=int(stdin.readline().strip())

arr=[]
arr=list(map(int, stdin.readline().strip().split()))
arr.sort()
x=int(stdin.readline().strip())

left,right=0,n-1
sum,cnt=0,0

while right>left:
    sum=arr[left]+arr[right]
    if sum==x: cnt+=1
    if sum<x:
        left+=1
        continue
    else:
        right-=1

print(cnt)