from sys import stdin

people=int(stdin.readline().strip())
arr=[]

for i in range(people):
    input_data=(stdin.readline().strip().split())
    arr.append((int(input_data[0]),int(input_data[1])))

arr2=sorted(arr,key=lambda x:(x[1],x[0]))

start=arr2[0][1]
cnt=1

for i in range(1,people):
    if start<=arr2[i][0]:
        start=arr2[i][1]
        cnt+=1

print(cnt)