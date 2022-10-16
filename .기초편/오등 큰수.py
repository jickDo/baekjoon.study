import sys
from collections import Counter
n=int(sys.stdin.readline())
A=list(map(int, sys.stdin.readline().strip().split()))
res=[-1]*n 
stack=[0] 
nums_count = Counter(A)

for i in range(1,n):
    while stack and nums_count[A[stack[-1]]]<nums_count[A[i]]:
        res[stack.pop()]=A[i]
    stack.append(i)

print(*res)