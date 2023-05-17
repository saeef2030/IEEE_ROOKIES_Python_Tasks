import math
user_input = list(input(" please enter your words sir: ").split())
list1=[]
list2=[]
for i in range(len(user_input)):
    list1.append(user_input[i][:(math.ceil(len(user_input[i])/2))])
    list2.append(user_input[i][(math.ceil(len(user_input[i])/2)):])
print(list1,"+",list2)