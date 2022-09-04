from sys import stdin

m=int(stdin.readline())
grade=[0]*m

for i in range(m):
    grade[i]=int(stdin.readline())

grade.sort()

for j in range(m):
    print(grade[j])