nums=[]
sum=0
T=int(input())

for i in range(T):
    num=int(input())
    if num==0:
        nums.pop()
    else:
        nums.append(num)


for i in range(len(nums)):
    sum+=nums[i]

print(sum)