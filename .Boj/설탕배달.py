from sys import stdin

sugar=int(stdin.readline().strip())

d=[10001]*(sugar+5)
d[3]=1
d[5]=1
for i in range(3,sugar+1):
    if i-3>=0:
        d[i]=min(d[i], d[i-3]+1)
    if i-5>=0:
        d[i]=min(d[i], d[i-5]+1)

if d[sugar]==10001:
    print(-1)
else:
    print(d[sugar])
