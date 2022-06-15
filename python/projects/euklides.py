def euklides(a,b):
    if a%b == 0:
        return b
    else:
        while b != 0:
            rest = a % b
            a = b
            b = rest
            if rest == 0:
                return a
a1=int(input("Enter first number: "))
b1=int(input("Enter second number: "))
euklides(a1,b1)

