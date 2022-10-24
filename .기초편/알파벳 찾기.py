import sys

arr=sys.stdin.readline().strip()
res=[-1]*26

for i in arr:
    res[ord(i)-97]=arr.find(i)

for i in res:
    print(i,end=' ')