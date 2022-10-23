import sys

word=sys.stdin.readline().strip()
arr=[0]*26

for i in word:
    arr[ord(i)-97]+=1

for i in arr:
    print(i,end=' ')
