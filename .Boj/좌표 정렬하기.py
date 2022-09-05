from sys import stdin

m=int(stdin.readline().strip())
array=[]
for i in range(m):
    input_data=list(map(int,stdin.readline().strip().split()))
    array.append((input_data[0],input_data[1]))


array2=sorted(array,key=lambda x:(x[0],x[1]))


for j in array2:
    print(j[0],end=' ')
    print(j[1])
