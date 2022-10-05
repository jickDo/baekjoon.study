from sys import stdin

n=int(stdin.readline().strip())

arr=[]
for i in range(n):
    arr.append(stdin.readline().strip())

result=0
check_list=[]
arr2=[]#리스트 원소뽑아내기
for i in range(n):
    cnt=0
    arr2=[]
    check_list=[]
    check_list=list(arr[i]) #입력받은것을 알파벳으로 쪼갠것
    arr2.append(check_list[0])
    if len(arr[i])==1:
        result+=1
        continue
    for j in range(1,len(check_list)):
        if check_list[j-1]==check_list[j]:
            continue
        elif check_list[j-1]!=check_list[j]:
            if check_list[j] in arr2:
                cnt+=1
                break
            else:
                arr2.append(check_list[j])
    if cnt==0:
        result+=1

print(result)