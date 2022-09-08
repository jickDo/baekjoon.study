from sys import stdin

n,m=map(int, stdin.readline().strip().split())
array=[]
array2=[]
result=[]
for i in range(n):
    array.append(stdin.readline().strip())

for j in range(m):
    array2.append(stdin.readline().strip())

result=list(set(array).intersection(set(array2)))
result.sort()

print(len(result))
for k in result:
    print(k)