from sys import stdin

data=list(stdin.readline().strip())
length=len(data)//2

arr1=[x for x in data[0:length]]
arr2=[x for x in data[length:]]
sum1,sum2=0,0
for i in arr1:
    sum1+=int(i)

for i in arr2:
    sum2+=int(i)

if sum1==sum2:
    print('LUCKY')
else:
    print('READY')