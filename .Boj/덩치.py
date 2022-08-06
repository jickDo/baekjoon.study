T=int(input())

hei_wei=[]
hei_wei_cnt=[]

for i in range(T):
    x,y=map(int, input().split())
    hei_wei.append((x,y))

for j in range(T):
    cnt=0
    for k in range(T):
        if hei_wei[j][0]<hei_wei[k][0] and hei_wei[j][1]<hei_wei[k][1]:
            cnt+=1
    hei_wei_cnt.append(cnt+1)

for q in hei_wei_cnt:
    print(q,end=" ")
