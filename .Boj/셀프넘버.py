from sys import stdin

use_list=[]
res_list=[]
dummy_list=[x for x in range(1,10001)]
for i in range(1,10001):
    use_list.clear()
    use_list=' '.join(str(i)).split()
    sum=0
    sum=int(i)
    for j in use_list:
        sum+=int(j)
    if sum>10000:
        pass
    res_list.append(sum)

new_list=[x for x in dummy_list if x not in res_list]
for i in new_list:
    print(i)