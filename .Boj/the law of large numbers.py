#배열의 크기N, 숫자가 더해지는 횟수M, 연속하는 횟수 K
#a는 큰수의 곲해지는수 b는 작은수의 곱해지는수

sum=0

N,M,K=map(int, input().split())

num=list(map(int, input().split()))
bigN=max(num)

if M==K:
  print(bigN*k)

elif num.count(bigN)>=2:
  print(bigN*k)

else:
  num.remove(bigN)
  bigN2=max(num)
  a=M//K
  b=M%K
  sum=((bigN*a*K)+bigN2*b)
  print(sum)