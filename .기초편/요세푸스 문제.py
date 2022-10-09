import sys

num,k=map(int, sys.stdin.readline().strip().split())
arr=[]
for i in range(1,num+1):
    arr.append(i)
rem=[]
cnt=0

for t in range(num):
    cnt += k-1
    if cnt>=len(arr):
        cnt = cnt%len(arr)
    
    rem.append(str(arr.pop(cnt)))
print("<",', '.join(rem),">",sep='')