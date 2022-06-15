#Zadanie 15
# z = int(input("Podaj liczbę: "))
# i = 0
# while z <= 0:
#     z = int(input("Podaj liczbę: "))
# while i <= z-1:
#     i += 1
#     print(i, end=', ')
#Zadanie 16
# z = int(input("Podaj liczbę: "))
# list=[]
# i = 0
# while z <= 0:
#     z = int(input("Podaj liczbę: "))
# while i <= z-1:
#     i += 1
#     list.append(str(i))
#     x = ", ".join(list)
#     print(x)
#PĘTLAMI
# z = int(input("Podaj liczbę: "))
# while z <= 0:
#     z = int(input("Podaj liczbę: "))
# i = 1
# while i <= z:
#     j = 1
#     while j < i:
#         print(j, end=", ")
#         j += 1
#     print(j)
#     i += 1
#Zadanie 17
# z = int(input('Podaj liczbę: '))
# silnia = 1
# for i in range(1, z+1):
#     silnia *= i
# print(f'n!: {silnia}')
#Zadanie 18
# z = int(input('Podaj liczbę liczb: '))
# iloczyn = 1
# for i in range(z):
#     x = int(input(f'Podaj {i+1} liczbę: '))
#     iloczyn *= x
# print(f'Iloczyn liczb wynosi: {iloczyn}')
#Zadanie 19
# z = int(input('Podaj liczbę liczb: '))
# iloczyn = 1
# while z <= 1:
#     z = int(input('BŁĄD! Podaj ponownie liczbę: '))
# for i in range(z):
#     x = int(input(f'Podaj {i+1} liczbę: '))
#     iloczyn *= x
# print(f'Iloczyn liczb wynosi: {iloczyn}')
#Zadanie 20
# z = int(input('Podaj liczbę liczb: '))
# stop = False
# iloczyn = 1
# while z <= 1:
#     z = int(input('BŁĄD! Podaj ponownie liczbę: '))
# for i in range(z):
#     x = int(input(f'Podaj {i+1} liczbę: '))
#     if x == 0:
#         print('Iloczyn wynosi 0!')
#         stop = True
#         break
#     iloczyn *= x
# if stop==False:
#     print(f'Iloczyn liczb wynosi: {iloczyn}')
#Zadanie 21
# n = int(input('Podaj liczbę liczb: '))
# while n <= 0:
#     n = int(input('Podaj ponownie liczbę liczb: '))
# avg = 0
# geo = 1
# harm = 1
# for i in range(n):
#     x = int(f'Podaj {i+1} liczbę: ')
#     if x < 0:
#         break
#     avg =
