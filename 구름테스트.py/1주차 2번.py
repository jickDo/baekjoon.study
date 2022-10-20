import sys

num,m=map(str,sys.stdin.readline().strip().split())
cnt=0
for i in range(int(num)):
    name = sys.stdin.readline().strip()
    if m in name:
        cnt += 1


print(cnt)