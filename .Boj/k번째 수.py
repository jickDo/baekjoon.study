from sys import stdin

n,k=map(int, stdin.readline().strip().split())

arr=[]

arr=list(map(int, stdin.readline().strip().split()))
arr.sort()

print(arr[k-1])