import sys

num=int(sys.stdin.readline())

stack=[]

for j in range(num):
    move_types=sys.stdin.readline().split()
    if move_types[0]=='push':
        stack.append(move_types[1])
    elif move_types[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif move_types[0]=='size':
        print(len(stack))
    elif move_types[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif move_types[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])