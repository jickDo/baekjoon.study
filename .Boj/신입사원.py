from sys import stdin
T=int(stdin.readline())


for i in range(T):
    people=int(stdin.readline())
    grade=[0]*people
    for j in range(people):
        grade[j]=list(map(int, stdin.readline().split()))

    grade.sort()

    t=grade[0][1]
    cnt=1
    for k in range(1,people):
        if t>grade[k][1]:
            cnt+=1
            t=grade[k][1]
    print(cnt)

