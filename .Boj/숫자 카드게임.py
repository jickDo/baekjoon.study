N,M=map(int, input().split())
smallest=[]
for i in range(N):
    numi=list(map(int, input().split()))
    mini=min(numi)
    smallest.append(mini)

print(max(smallest))