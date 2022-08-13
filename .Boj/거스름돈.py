money=int(input())
money=1000-money
change=[500,100,50,10,5,1]
cnt=0
for i in range(len(change)):
    if money>=change[i]:
        cnt+=(money//change[i])
        money=money%change[i]

print(cnt)