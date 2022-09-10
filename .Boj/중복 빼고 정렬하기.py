from sys import stdin

n=int(stdin.readline().strip())

arr=[]
arr=list(map(int, stdin.readline().strip().split()))
arr=list(set(arr))
arr.sort()

for i in arr:
    print(i,end=' ')