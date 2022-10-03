from sys import stdin

a,b,v=map(int, stdin.readline().strip().split())
new_a=v-a
new_b=a-b
res=new_a//new_b
if new_a%new_b==0:
    print(res+1)
else:
    print(res+2)
