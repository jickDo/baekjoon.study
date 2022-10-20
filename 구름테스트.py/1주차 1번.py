import sys
num=int(sys.stdin.readline())

arr=list(map(int,sys.stdin.readline().strip().split()))
sum=1
for i in arr:
	sum*=i
	
print(sum)