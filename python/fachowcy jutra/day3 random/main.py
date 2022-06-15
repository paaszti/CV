import random as r
#Zadanie 1
# x = 0
# while x != 6:
#     x = r.randint(1, 6)
#     print(x)
#Zadanie 2/3/4
# def chce_dalej():
#     znak = 'x'
#     while znak != 't' or znak != 'T' or znak != 'n' or znak != 'N':
#         znak = input('Czy chcesz kontynuować? ')
#     return znak == 't' or znak == 'T'
# while True:
#     x = r.randint(1, 10)
#     guess = int(input('Podaj liczbę: '))
#     i = 1
#     while x != guess:
#         if guess > x:
#             print('Podałeś za dużo!')
#         else:
#             print('Podałeś za mało!')
#         guess = int(input('Podaj liczbę jeszcze raz: '))
#         i += 1
#     print(f'Gratulację zgadłeś za {i} razem! ')
#     if not chce_dalej():
#         break
#Zadanie 5
# def losuj(n, a, b):
#     poprzednia = a -1
#     x = r.randint(a, b)
#     for i in range(n):
#         if x == poprzednia:
#             x = r.randint(a, b)
#         print(x)
#         poprzednia = x
#
# def main():
#     losuj(10, 1, 49)
#
# main()
#Zadanie 6
# list = ["orzeł", "reszka"]
# orzeł = 0
# reszka = 0
# n = int(input('Podaj liczbę: '))
# while n < 0:
#     n = int(input('Podaj liczbę: '))
# for i in range(n):
#     x = r.randint(0, 1)
#     print(f'{i+1} rzut wypadł: {list[x]} ')
#     if list[x] == "orzeł":
#         orzeł += 1
#     else:
#         reszka += 1
# if orzeł == 1 and reszka == 1:
#     print(f'Orzeł wypadł {orzeł} raz, a reszka {reszka} raz. ')
# elif orzeł == 1:
#     print(f'Orzeł wypadł {orzeł} raz, a reszka {reszka} razy. ')
# elif reszka == 1:
#     print(f'Orzeł wypadł {orzeł} razy, a reszka {reszka} raz. ')
# else:
#     print(f'Orzeł wypadł {orzeł} razy, a reszka {reszka} razy.')
#
#


