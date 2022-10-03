from sys import stdin

n=int(stdin.readline().strip())

arr=[]
for i in range(n):
    arr.append(int(stdin.readline().strip()))
arr.reverse()
cnt=0
start=arr[0]
num=0
for i in range(1,n):
    if arr[i]>=start:
        num=arr[i]-start
        cnt+=(num)+1
        start=arr[i]-num-1
    else:
        start=arr[i]
print(cnt)