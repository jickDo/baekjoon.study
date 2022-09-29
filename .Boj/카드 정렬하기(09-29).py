from sys import stdin

n=int(stdin.readline().strip())
arr=[]
for i in range(n):
    arr.append(int(stdin.readline().strip()))
arr.sort()
sum,result=0,0
if len(arr)==1:
    print(0)
    exit()

while len(arr)!=1:
    sum=arr[0]+arr[1]
    del arr[:2]
    arr.append(sum)
    arr.sort()
    result+=sum
    sum=0

print(result)