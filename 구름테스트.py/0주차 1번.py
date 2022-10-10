import sys

n,k=map(int,sys.stdin.readline().split())

arr=list()
for i in range(n):
	arr.append(sys.stdin.readline().strip())

	
arr.sort()

arr.sort(key=len)

print(arr[k-1])