from sys import stdin

point, length=map(int, stdin.readline().strip().split())

arr=list(map(int, stdin.readline().strip().split()))
arr.sort()

res=1
start=arr[0]-0.5
end=start+length

for i in range(point):
    if start<arr[i]<end:
        continue
    else:
        res+=1
        start=arr[i]-0.5
        end=start+length
print(res)