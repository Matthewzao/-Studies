import math
import time

ask = str(input('type something:'))
for i in range(99+1):
    print(ask)

a = int(5)
b = int(5)
soma = a + b
subtracao = a - b
mult = a * b
print(mult) 

valorOriginal = int(input('o salario do mateus é de: '))
valorDescontado = valorOriginal + (valorOriginal * 0.2)
print('seu salario é', valorOriginal)
print('e com o acréscimo após 6 meses vai ser de: ', valorDescontado)




media_1 = float(input('Informe uma nota: '))
media_2 = float(input('informe outra nota: '))
media_3 = float(input('Informe mais uma nota '))
media_4 = float(input('informa só mais uma nota: ')) 
soma = (media_1 + media_2 + media_3 + media_4) /4
print("sua media é:", soma)

                                            #  EXEMPLO DE FOR's

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("fim")

ask = int(input('type it something: '))
for c in range(0,ask+1):
    print(c)
print('FIM')


s = 0
for c in range(0,4):
    n = int(input('Type it a value: '))
    s += n
print('O somaório de todos os valores é,',s )

for i in range(15,0, -1):           
    print(i)
    time.sleep(1)
print("fim")

