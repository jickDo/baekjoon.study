from sys import stdin

m=int(stdin.readline())
words=[]
for i in range(m):
    words.append(stdin.readline().strip())

words=set(words)
words=list(words)

words.sort()
words.sort(key=len)


for i in words:
    print(i)