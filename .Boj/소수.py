from sys import stdin

start=int(stdin.readline().strip())
end=int(stdin.readline().strip())
arr=[]

for i in range(start,end+1):
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        arr.append(i)

if len(arr)==0:
    print(-1)
    exit()

sum=0
for i in arr:
    sum+=i

print(sum)
print(min(arr))
