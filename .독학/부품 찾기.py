from sys import stdin

def binary_search(arr,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        binary_search(arr,target,start,mid-1)
    else:
        binary_search(arr, target, mid+1, end)
    
n=int(stdin.readline().strip())
arr=list(map(int, stdin.readline().strip().split())) #가게의 물건정보
arr.sort()
m=int(stdin.readline().strip())
arr2=list(map(int, stdin.readline().strip().split())) #손님이 원하는 물건정보



for i in arr2:
    res=binary_search(arr,i,0,n-1)
    if res==None:
        print('no',end=' ')
    else:
        print('yes', end=' ')