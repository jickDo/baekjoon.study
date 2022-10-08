import sys
num=int(sys.stdin.readline())
for i in range(num):
    vps=sys.stdin.readline()
    cnt=0
    for j in vps:
        if j=='(':
            cnt+=1
        elif j==')':
            cnt-=1
        if cnt<0:
            break
    if cnt==0:
        print('YES')
    else:
        print('NO')

