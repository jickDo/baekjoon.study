from sys import stdin
from collections import Counter

n=int(stdin.readline().strip())

db=[]

for i in range(n):
    db.append(int(stdin.readline().strip()))

db.sort()
#산술평균
sum=0
for i in db:
    sum+=i
print(round(sum/n)) #반올림 함수

#중앙값 출력
print(db[(len(db)//2)])

#최빈값 출력 여러개있다면 최빈값중 두번째 출력

cnt=Counter(db).most_common()

if len(db)>1:
    if cnt[0][1]==cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

#최대값과 최솟값을 출력하기

print(max(db)-min(db))