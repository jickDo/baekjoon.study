#예시1번-시간초과

from sys import stdin
num,bag=map(int, stdin.readline().strip().split()) #보석 갯수, 가방 갯수

arr=[0]*num
for i in range(num):
    input_data=stdin.readline().strip().split()
    arr.append(list((int(input_data[0]),int(input_data[1]))))

arr_bag=[0]*bag
for j in range(bag):
    arr_bag.append(int(stdin.readline().strip()))
arr_bag.sort()
arr.sort(key=lambda x:(-x[1],x[0]))                    
cnt=0

for k in range(bag):
    for c in range(num):
        if arr_bag[k]>arr[c][0]:
            cnt+=arr[c][1]
            arr[c][0]=max(arr_bag)
            break

print(cnt)

