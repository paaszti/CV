import math
#Zadanie 1
# def f(x):
#     y = math.sqrt(abs(x)) + (math.sin(x) / (1 + x**2))
#     return y
# def g(x):
#     if x > 0:
#         y = f(x)
#         return y
#     elif (x<=0 and x >= -1):
#         y = -(abs(f(x)))**(1/3)
#         return y
#     elif x < -1:
#         return 0
# def main():
#     x = float(input('Podaj argument funkcji: '))
#     print(f'x = {x}, | f(x) = {f(x)} |, g(x) = {g(x)}')

# main()
#Zadanie 2
# def min2(a, b):
#     if a > b:
#         return b
#     else:
#         return a
# def max2(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# def min3(a, b, c):
#     x = min2(a, b)
#     y = min(x, c)
# def max3(a, b, c):
#     x = max3(a, b, c)
#     y = max2(x, c)
#Zadanie 3
# def czy_poprawna_pora(g, m):
#     if ((g <= 24 and g >= 0) and (m <= 59 and m >= 0)):
#         return True
#     else:
#         return False
# def ile_minut(g, m):
#     return (g * 60) + m
#
# def roznica_por(g1, m1, g2, m2):
#     x = ile_minut(g1, m1)
#     y = ile_minut(g2, m2)
#     return (x-y)
#
# def main():
#      hour = int(input('Podaj godzinę: '))
#      minute = int(input('Podaj minutę: '))
#      if czy_poprawna_pora(hour, minute):
#          hour2 = int(input('Podaj godzinę: '))
#          minute2 = int(input('Podaj minutę: '))
#          if czy_poprawna_pora(hour2, minute2):
#             print(f"Różnica wynosi: {roznica_por(hour, minute, hour2, minute2)}")
#          else:
#             print('To nie jest poprawna pora')
#      else:
#         print('Pora niepoprawna')
#
# main()
#Zadanie 4
# def jest_dzielnikiem(d, n):
#     if d % n == 0:
#         return True
#     else:
#         return False
# def czy_przestepny(rok):
#     if (rok % 4 == 0 and rok % 100 != 0) or (jest_dzielnikiem(rok, 400)):
#         return True
#     else:
#         return False
# def liczba_dni(mies, rok):
#     if mies > 12:
#         return 0
#     if mies == 2:
#         if czy_przestepny(rok) == True:
#             return 29
#         else:
#             return 28
#     elif mies == 1 or mies == 3 or mies == 5 or mies == 7 or mies == 10 or mies == 12:
#         return 31
#     else:
#         return 30
#
# def main():
#     year = int(input('Podaj rok: '))
#     month = int(input('Podaj miesiąc: '))
#     print(f"Liczba dni w roku {year} i miesiącu {month} wynosi: {liczba_dni(month, year)}")
# main()
#Zadanie 5
# def suma_cyrf(n):
#     s = 0
#     while n > 0:
#         c = n % 10
#         s = s + c
#         n = n // 10
#     return s
#
# def main():
#     n = int(input('Podaj liczbę: '))
#     suma_cyrf(n)
#     while n < 0:
#         n = int(input('Podaj liczbę: '))
#     print(suma_cyrf(n))
#
# main()
#Zadanie 6
# import random
# def wczytaj_liczbe(pocz, kon):
#     return random.randint(pocz, kon)
# def main():
#     start = int(input('Podaj początkową liczbę: '))
#     stop = int(input("Podaj końcową liczbę: "))
#     print(f'Twoja liczba to: {wczytaj_liczbe(start, stop)}')
# main()
#Zadanie 7*
# def f(m):
#     if m <= 1:
#         return 1
#     if m > 1:
#         return f(m-1) + f(m-2)
# def main():
#     fib = int(input('Podaj wyraz ciągu: '))
#     print(f'{fib} wyraz ciągu jest równy: {f(fib)}')
# main()
#Zadanie 8
# def jest_dzielnikiem(a, b):
#     if a % b == 0:
#         return True
#     else:
#         return False
# def suma_dzielnikow(m):
#     s = 0
#     for i in range(1, m-1):
#         if jest_dzielnikiem(m, i) == True:
#             s += i
#     return s
# def czy_doskonala(m):
#     if m == suma_dzielnikow(m):
#         return True
#     else:
#         return False
#
# def czy_zaprzyjaznione(m, n):
#     if suma_dzielnikow(m) == n and suma_dzielnikow(n) == m:
#         return True
#     else:
#         return False
# print(czy_zaprzyjaznione(1184, 1210))
#Zadanie 9
# def jest_dzielnikiem(a, b):
#     if a % b == 0:
#         return True
#     else:
#         return False
# def dzielniki(a):
#     for i in range(1, a+1):
#         if a % i == 0:
#             print(i, end=", ")
#
# def liczba_pierwsza(m):
#     if m == 1:
#         return False
#     for i in range(2, m):
#         if m % i == 0:
#             return False
#     return True
#Zadanie 10
# def jest_dzielnikiem(a, b):
#     if a % b == 0:
#         return True
#     else:
#         return False
# def liczba_dzielnikow(n, pocz, kon):
#     s = 0
#     for i in range(pocz, kon+1):
#         if jest_dzielnikiem(n, i) == True:
#          s += 1
#     return s
#Zadanie 12
# def NWD(a, b):
#     if  a % b == 0:
#         return b
#     else:
#         while b != 0:
#             rest = a % b
#             a = b
#             b = rest
#             if rest == 0:
#                 return a
# def wzglednie_pierwsze(a, b):
#     if NWD(a, b) == 1:
#         return True
#     else:
#         return False
#Zadanie 13
# def chce_dalej():
#     guess = str(input("Czy chcesz kontynuować? "))
#     if guess == 't' or guess == 'T':
#         return True
#     else:
#         return False
#
