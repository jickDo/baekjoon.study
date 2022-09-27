from sys import stdin

n=int(stdin.readline().strip())

arr=[]
for i in range(n):
    arr.append(int(stdin.readline().strip()))
arr.sort()
sum=[]
for j in range(n):
    sum.append(arr[j]*(n-j))

print(max(sum))