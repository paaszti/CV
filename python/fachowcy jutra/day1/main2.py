#Zadanie 1
# x = float(input('Podaj liczbę: '))
# if x%5 == 0:
#     print('Liczba jest podzielna przez 5')
# else:
#     print("Liczba nie jest podzielna przez 5 ")
#Zadanie 2
# x = float(input('Podaj liczbę: '))
# y = float(input('Podaj liczbę: '))
# if x > y:
#     print(y)
# else:
#     print(x)
#Zadanie 3
# h = int(input('Podaj godzinę: '))
# m = int(input('Podaj minutę: '))
# suma = (h *60) + m
# if suma >= 465 and suma <= 690:
#     print('Możesz zjeść śniadanie.')
# else:
#     print('Nie możesz zjeść śniadania.')
#Zadanie 4
# a = float(input('Podaj długość boku kwadratu: '))
# if a > 0:
#     print(f'Obwód wynosi: {4*a}, a pole wynosi: {a**2}')
# else:
#     print('Error')
#Zadanie 5
# x1 = int(input('Podaj punkt pierwszą współrzędną x: '))
# y1 = int(input('Podaj punkt pierwszą współrzędną y: '))
# x2 = int(input('Podaj punkt drugą współrzędną x: '))
# y2 = int(input('Podaj punkt drugą współrzędną y: '))
# if x1 == x2 and y1 == y2:
#     print('Pokrywają się.')
# else:
#     lenght = (abs(x2 - x1)**2 + abs(y2 - y1)**2)**0.5
#     print('Długość odcinka wynosi: ',lenght)
#Zadanie 6
# x = int(input('Podaj liczbę: '))
# t = x//1000
# s = (x-t*1000)//100
# d = (x-t*1000-s*100)//10
# j = x%10
# if x < 0 or x > 9999:
#     print('Błąd')
# else:
#     print(f'Tysiące: {t}, setki: {s}, dziesiątki: {d}, jedności: {j} ')
#Zadanie 7
# a = float(input('Podaj długość boku a: '))
# b = float(input('Podaj długość boku b: '))
# c = float(input('Podaj długość boku c: '))
# if (a+b>c and b+c>a and a+c>b):
#     p = (a+b+c)/2
#     s = (p*(p-a)*(p-b)*(p-c))**0.5
#     print(f'Można zbudować trójkąt, jego pole wynosi: {s}')
# else:
#     print('Nie można zbudować trójkąta')
#Zadanie 8
# x = float(input('Podaj współrzędną x: '))
# y = float(input('Podaj współrzędną y: '))
# if 0<=x and x<=5 and 0<=y and y<=x:
#     print(f'Punkt {x}, {y} należy do zadanego trójkąta')
# else:
#     print(f'Punkt {x}, {y} nie należy do zadanego trójkąta')
#Zadanie 9
# n = float(input('Podaj nadgodziny: '))
# s = float(input('Podaj stawkę: '))
# if n < 30:
#     p=n*s
#     print(f'Płaca = {p}')
# else:
#     p=30*s+(n-30)*s*1.5
#     print(f'Płaca = {p}')
#Zadanie 11
# import math
# r = float(input('Podaj długość promienia: '))
# if r > 0:
#     print(f'Obwód koła wynosi: {2*math.pi*r}, a pole wynosi {(4*math.pi)*(r**2)}')
#Zadanie 12
# yo = int(input('Podaj wiek: '))
# if yo >= 18:
#     print('Jesteś już dorosły')
# elif yo < 12:
#     print('Jesteś dzieckiem')
# else:
#     print('Jesteś nastolatkiem')
#Zadanie 13
# x = float(input('Podaj x: '))
# if x <= -1:
#     print(f'y = {x+1}')
# elif (x > -1 and x <= 0):
#     print(f'y = {(x**2)+((x-1)/(x+2))}')
# elif x > 0:
#     print(f'y = {x}')
#Zadanie 14
# salary = float(input('Podaj dochód: '))
# tax_1 = 14539.17+(0.32*(salary-85528))
# tax_2 = (0.17*salary)-525.12
# if salary > 85528:
#     print(f'Podatek wynosi: {tax_1}')
# elif tax_2 > 0:
#     print(f'Podatek wynosi: {tax_2}')
# else:
#     print("Błąd")
#Zadanie 15
# a = float(input('Podaj a: '))
# b = float(input('Podaj b: '))
# if a != 0:
#     print(f'Rozwiązaniem równania jest: {-b/a}')
# elif b==0:
#     print(f'Rozwiązaniem równania jest: {abs(-b/a)}')
# else:
#     print('Błąd')
#Zadanie 16
# import math
# a = float(input('Podaj długość boku a: '))
# b = float(input('Podaj długość boku b: '))
# alfa = int(input('Podaj kąt między nimi: '))
# if (a>0 and b>0 and alfa>0):
#     c = math.sqrt((a**2) + (b**2) - (2*a*b*math.cos(alfa)))
#     p = a+b+c/2
#     s = math.sqrt(p*(p-a)*(p-b)*(p-c))
#     print(f'Bok c wynosi: {c} ,a pole wynosi: {s}')
# else:
#     print('Błąd')
# Zadanie 17
# a = float(input('Podaj a: '))
# b = float(input('Podaj b: '))
# if (a > 0 and b > 0):
#     print('Prosta przechodzi przez I, II i III ćwiartkę')
# elif (a > 0 and b < 0):
#     print('Prosta przechodzi przez I, III i IV ćwiartkę')
# elif (a < 0 and b == 0):
#     print('Prosta przechodzi przez II i IV ćwiartkę')
# elif (a > 0 and b==0):
#     print('Prosta przechodzi przez I i III ćwiartkę')
# elif a==0:
#     print(f'y = {b}')
