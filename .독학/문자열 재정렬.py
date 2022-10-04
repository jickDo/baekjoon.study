from sys import stdin

input_data=stdin.readline().strip()
n_list=['0','1','2','3','4','5','6','7','8','9']
input_data=list(input_data) #입력받은값
num_data=[] #입력받은 값에서 숫자만 뽑아내기
sum=0
for i in input_data:
    if i in n_list:
        num_data.append(i)
        sum+=int(i)

new_list=[x for x in input_data if x not in num_data]
new_list.sort()

new_list.append(str(sum))
new_list=''.join(new_list)
print(new_list)