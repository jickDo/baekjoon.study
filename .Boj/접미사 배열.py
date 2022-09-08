from sys import stdin

s=stdin.readline().strip()

#1.받은 문자열 앞에서 부터 없애고 리스트에 담기 2.나열
array=[s]
for i in range(1,len(s)):
    array.append(s[i:len(s)])

array.sort()
result='\n'.join(array)

print(result)
