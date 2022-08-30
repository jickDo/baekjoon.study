from sys import stdin

n,m=map(int, stdin.readline().split())

ice=[]
for i in range(n):
    ice.append(list(map(int,stdin.readline().strip())))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if ice[x][y]==0:
        ice[x][y]=1
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x+1,y)
        return True
    return False

cnt=0

for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            cnt+=1

print(cnt)
#github수정