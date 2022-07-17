#N은 행은 개수를 의미하며, M은 열의 개수를 의미한다.

N,M=map(int, input().split())
smallest=[]
for i in range(N):
    numi=list(map(int, input().split()))
    mini=min(numi)
    smallest.append(mini)

print(max(smallest))

