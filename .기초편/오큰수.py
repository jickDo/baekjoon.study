import sys

n=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().strip().split()))
stack=[]
res=[0]*n

for i in range(n):
    while stack and arr[stack[-1]]<arr[i]:
        res[stack.pop()]=arr[i]
    stack.append(i)

while stack:
    res[stack.pop()]=-1

ans=''
for i in res:
    ans+=str(i)+' '

print(ans)