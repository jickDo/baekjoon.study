from sys import stdin

arr=stdin.readline().strip()
target=stdin.readline().strip()

arr2=arr.split(target)
cnt=0

for i in arr2:
    cnt+=len(i)

print((len(arr)-cnt)//len(target))