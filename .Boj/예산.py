from sys import stdin
import math

game,win=map(int, stdin.readline().strip().split())
ratio=math.trunc((win/game)*100)
new_ratio=0
if game==win:
    print(-1)
cnt=0
while True:
    ratio=math.trunc((win/game)*100)
    win+=1
    game+=1
    new_ratio=math.trunc((win/game)*100)
    cnt+=1
    if ratio!=new_ratio:
        print(cnt)
        break