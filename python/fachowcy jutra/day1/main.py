# #Zadanie 1
# a = float(input('Podaj długość boku a: '))
# b = float(input('Podaj długość boku b: '))
# print(f'Prostokąt o bokach {a} i {b} ma pole: {a*b} i obwód {2*a+2*b}')
# #Zadanie 2
# a = int(input('Podaj a: '))
# b = int(input('Podaj b: '))
# c = int(input('Podaj c: '))
# d = int(input('Podaj d: '))
# print(f'Średnia arytmetyczna wynosi: {a+b+c+d/4}')
#Zadanie 3
# a = int(input('Podaj liczbę a: '))
# b = int(input('Podaj liczbę b: '))
# if b != 0:
#     print(f'Suma tych liczb wynosi {a+b}, różnica {a-b}, iloczyn {a*b} a iloraz jest równy {a/b} ')
# else:
#     print(f'Suma tych liczb wynosi {a+b}, różnica {a-b}, iloczyn {a*b}, nie da się dzielić przez zero!')
#Zadanie 4
# C = float(input('Podaj stopnie w Celsjuszach: '))
# print(f'Temperatura w Fahrenheita: {32+(1.8*C)}')
#Zadanie 5
# F = float(input("Podaj stopnie w Fahremheitach: "))
# print(f'Temperatura w Celsjuszach wynosi: {5/9*(F-32)}')
#Zadanie 6
# a = float(input('Podaj liczbę: '))
# proc = int(input('Podaj procent: '))
# print(f'{proc}% z liczby {a} jest równy {a*(proc*0.01)}')
#Zadanie 7
# a = input('Podaj liczbę: ')
# b = input('Podaj liczbę: ')
# c = a
# a = b
# b = c
# print(a, b)
#Zadanie 8
# a = int(input('Podaj liczbę : '))
# b = int(input('Podaj liczbę: '))
# c = a
# a = b + a
# b = c
# print(f'{a, b}')
#Zadanie 9
# x1 = int(input('Podaj punkt pierwszą współrzędną x: '))
# y1 = int(input('Podaj punkt pierwszą współrzędną y: '))
# x2 = int(input('Podaj punkt drugą współrzędną x: '))
# y2 = int(input('Podaj punkt drugą współrzędną y: '))
# lenght = (abs(x2 - x1)**2 + abs(y2 - y1)**2)**0.5
# print(f'Równanie prostej: {(y2-y1)/(x2-x1)}*x{y2-(y2-y1)/(x2-x1)*x1}')
# print(f'Długość odcinka: {lenght}')
#Zadanie 10
# a = int(input('Podaj a: '))
# b = int(input('Podaj b: '))
# c = int(input('Podaj c: '))
# print(f'Średnia arytmetyczna: {(a+b+c)/3}, geometryczna {(a*b*c)**(1/3)}, harmoniczna {3/((1/a)+(1/b)+(1/c))} ')
#Zadanie 11
# a = float(input('Podaj pierwszą współrzędną: '))
# b = float(input('Podaj drugą współrzędną: '))
# print(f'({a}, {b})')
#Zadanie 12
# a = float(input('Podaj długość krawędzi podstawy: '))
# b = float(input('Podaj długość drugiej krawędzi podstawy: '))
# c = float(input('Podaj długość krawędzi bocznej: '))
# print(f'Przekątna prostopadłościaniu wynosi: {(a**2+b**2+c**2)**0.5}')
#Zadanie 13
# year = int(input('Podaj rok: '))
# H = (24+19*(year%19))%30
# I = H - (H//28)
# J = (year + (year//4) + I - 13) % 7
# L = I - J
# Easter_Month = 3 + ((L+40)//44)
# Easter_Day = L + 28 - 31 * (Easter_Month//4)
# if year < 2022:
#     print(f'W {year} roku Święta Wielkanocne były w miesiącu: {Easter_Month} ,a Wielka Niedziela była {Easter_Day}')
# else:
#     print(f'W {year} roku Święta Wielkanocne będą w miesiącu: {Easter_Month} ,a Wielka Niedziela będzie {Easter_Day}')
#Zadanie 14
# x1 = int(input('Podaj punkt pierwszą współrzędną x: '))
# y1 = int(input('Podaj punkt pierwszą współrzędną y: '))
# x2 = int(input('Podaj punkt drugą współrzędną x: '))
# y2 = int(input('Podaj punkt drugą współrzędną y: '))
# x3 = int(input('Podaj punkt trzecią współrzędną x: '))
# y3 = int(input('Podaj punkt tzrecią współrzędną y: '))
# lenght_a = (abs(x2 - x1)**2 + abs(y2 - y1)**2)**0.5
# lenght_b = (abs(x3 - x2)**2 + abs(y3 - y2)**2)**0.5
# lenght_c = (abs(x3 - x1)**2 + abs(y3 - y1)**2)**0.5
# p = (lenght_a+lenght_b+lenght_c)/2
# s = p*(p-lenght_a)*(p-lenght_b)*(p-lenght_c)**0.5
# print(f'Pole trójkąta wynoszsi: {s}')


