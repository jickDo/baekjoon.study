from sys import stdin

n=int(stdin.readline().strip())

arr=list(map(int, stdin.readline().strip().split()))
arr.sort()

result=0
sum=0

for i in arr:
    sum+=1
    if sum>=i:
        result+=1
        sum=0
    
print(result)