from sys import stdin
from collections import Counter

n=int(stdin.readline().strip())

arr=[]

for i in range(n):
    arr.append(int(stdin.readline().strip()))

arr.sort()
res=Counter(arr).most_common(1)
print(res[0][0])