from sys import stdin

k,n=map(int, stdin.readline().strip().split())
line=[0]*k
for i in range(k):
    line[i]=int(stdin.readline().strip())

start,end=1,max(line)
result=0
while start<=end:
    total=0
    mid=(start+end)//2
    for i in line:
        total=total+(i//mid)
    if total<n:
        end=mid-1
    else:
        start=mid+1
        result=mid

print(result)