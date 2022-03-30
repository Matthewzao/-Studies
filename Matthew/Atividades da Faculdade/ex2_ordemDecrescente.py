for i in range(3):
    n1 = int(input('digite o primeiro numero: '))
    n2 = int(input('digite o segundo numero: '))
    n3 = int(input('digite o terceiro numero: '))

    if n1 > n2 > n3:
        print(n1, n2, n3)
    if n1 > n3 > n2:
        print(n1, n3, n2)
    if n2 > n3 > n1:
        print(n2, n3, n1)
    if n2 > n1 > n3:
        print(n2, n1, n3)
    if n3 > n2 > n1:
        print(n3, n2, n1)
    if n3 > n1 > n2:
        print(n3, n1, n2)
