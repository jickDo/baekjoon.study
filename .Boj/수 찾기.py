from sys import stdin

def binary_search(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

n=int(stdin.readline().strip())
arr=list(map(int, stdin.readline().strip().split()))
arr.sort()

m=int(stdin.readline().strip())
arr2=list(map(int, stdin.readline().strip().split()))

for i in arr2:
    res=binary_search(arr, i, 0, n-1)
    if res!=None:
        print(1)
    else:
        print(0)