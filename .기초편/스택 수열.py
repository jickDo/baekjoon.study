import sys
num=int(sys.stdin.readline())
stack=[] #마지막에 비교하기위해 넣어두는값 정답이라면 마지막에 input_data와값이동일
cnt=1
result=[]
dummy=0
for i in range(num):
    num=int(sys.stdin.readline())
    while cnt<=num:
        stack.append(cnt)
        result.append('+')
        cnt+=1
    if num==stack[-1]:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        dummy+=1
        break
if dummy==0:
    for i in result:
        print(i)
