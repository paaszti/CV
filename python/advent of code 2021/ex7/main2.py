import cmath
list=[16,1,2,0,4,2,7,1,2,14]
list_1=[]
fuel=[]
x=max(list)+1
k=0
lenght=len(list)
for z in range(1, x):
    for i in range(lenght):
        y = abs(list[i] - x)
        list_1.append(y)
    for i in range(len(list_1)):
        for j in range(1, list_1[i]):
            list_1[i]+=j






