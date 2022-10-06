import sys

num=int(sys.stdin.readline())

arr=[]
new_arr=[]
for i in range(num):
    words=sys.stdin.readline().split()
    for j in range(len(words)):
        sum=words[j]
        new_arr.append(sum[::-1])
    arr.append(new_arr[0:j+1])
    new_arr.clear()

for i in range(num):
    arr[i]=' '.join(arr[i])
    print(arr[i])