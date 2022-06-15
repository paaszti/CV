c=[]
number=int(input("Enter the number: "))
list=[]
for i in range (1, number+1):
    if number%i==0:
        list.append(i)
number2=int(input("Enter next number: "))
list1=[]
for i in range (1, number+1):
    if number%i==0:
        list1.append(i)
c=[]
for elements in list:
        if elements in list1:
                c.append(elements)
print(c)
