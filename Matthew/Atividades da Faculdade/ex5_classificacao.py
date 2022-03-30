codigo = int(input('DIGITE UM CODIGO: '))

if codigo == 1:
    print('Alimento não - Perecível')
if codigo == 2 or codigo == 3 and codigo == 4:
    print('Alimento Perecível')
if codigo == 5 or codigo == 6:
    print('Vestuário')
if codigo == 7:
    print('Higiene Pessoal')
if codigo == 8 or codigo == 9 or codigo == 10 or codigo == 11 or codigo == 12 or codigo == 13 or codigo == 14 or codigo == 15:
    print('Limpeza e utensílios domésticos')
if codigo >= 16:
    print('Inválido')
