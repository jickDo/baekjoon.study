import sys

arr=list(sys.stdin.readline().strip())
tmp=''
stick=0
cnt=0
for i in range(0,len(arr)-1):
    if arr[i]=='(':
        if arr[i+1]==')':
            cnt+=stick
        else:
            stick+=1
    else:
        if arr[i+1]=='(':
            pass
        else:
            stick-=1
            cnt+=1

print(cnt)