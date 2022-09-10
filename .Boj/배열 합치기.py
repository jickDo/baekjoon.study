from sys import stdin

n,m =map(int, stdin.readline().strip().split())

list_a=list(map(int, stdin.readline().strip().split()))
list_b=list(map(int, stdin.readline().strip().split()))

list_a=list_a+list_b
list_a.sort()

for i in list_a:
    print(i,end=' ')