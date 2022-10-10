import math
import sys

num=int(sys.stdin.readline())
ai_arr=[]
ai_arr=sys.stdin.readline().strip().split()

arr=[True for i in range(num+1)]

for i in range(2,int(math.sqrt(num))+1):
	if arr[i]==True:
		k=2
		while i*k<=num:
			arr[i*k]=False
			k+=1
sum=0
for j in range(2,num+1):
	if arr[j]==True:
		sum+=int(ai_arr[j-1])
print(sum)