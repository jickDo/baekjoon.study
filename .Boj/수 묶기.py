from sys import stdin

n=int(stdin.readline().strip())

arr=[]
for i in range(n):
    arr.append(list(int(stdin.readline().split())))

print(arr)