import sys

arr=list(map(int,sys.stdin.readline().strip().split()))
arr.sort()

sum=arr[3]-arr[0]
sum=abs(sum)

sum2=arr[2]-arr[1]
sum2=abs(sum2)

sum+=sum2
print(sum)