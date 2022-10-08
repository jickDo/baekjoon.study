import sys

s1=list(sys.stdin.readline().strip())
s2=[]
num=int(sys.stdin.readline().strip())
for i in range(num):
    input_data=sys.stdin.readline().strip().split()
    if input_data[0]=='L':
        if s1:
            s2.append(s1.pop())
    elif input_data[0]=='D':
        if s2:
            s1.append(s2.pop())
    elif input_data[0]=='B':
        if s1:
            s1.pop()
    elif input_data[0]=='P':
        s1.append(input_data[1])

s1.extend(reversed(s2))
print(''.join(s1))