num=int(input())
s30=[]
sum=0
for i in str(num):
    s30.append(i)
s30.sort(reverse=True)

if '0' not in s30:
    print(-1)
    exit()
else:
    pass

for i in range(len(s30)):
    sum+=int(s30[i])

if sum%3==0:
    s30="".join(s30)
    print(s30)
else:
    print(-1)
