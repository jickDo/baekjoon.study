from sys import stdin

s=stdin.readline()
s1=s.split('0')
s2=s.split('1')

s1=' '.join(s1).split()
s2=' '.join(s2).split()
s1=len(s1)
s2=len(s2)

if s1>=s2:
    print(s2)
else:
    print(s1)
