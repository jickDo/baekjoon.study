from sys import stdin

num=stdin.readline().strip()
num=list(num)

for i in range(1,len(num)):
    for j in range(i,0,-1):
        if num[j]<num[j-1]:
            num[j],num[j-1]=num[j-1],num[j]
        else:
            break
num.reverse()

for j in num:
    print(j,end='')