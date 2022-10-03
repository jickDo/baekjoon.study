from sys import stdin

arr=list(map(int, stdin.readline().strip()))
arr.sort()
sum=0
for i in arr:
    if sum<=1:
        sum+=i
    else:
        sum*=i

print(sum)