from sys import stdin

A,B= map(int, stdin.readline().split())
cnt=1
num=0
while A!=B:
    if A>B:
        print(-1)
        break
    elif B%2==0:
        B=B//2
        cnt+=1
    elif B%2==1 and B%10==1:
        B=(B-1)//10
        cnt+=1
    else:
        print(-1)
        break

if A==B:
    print(cnt)