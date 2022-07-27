alp=['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt=0
word=input()
word2=word
for i in range(len(alp)):
    if alp[i] in word:
        word=word.replace(alp[i], '*')
cnt=len(word)
print(cnt)
