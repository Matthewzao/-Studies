# import datetime
# from datetime import date
# ano = int(input('em que ano você nasceu' ))

# anoNasc = datetime.date(ano)
# diferenca = (date.today() - anoNasc)

# resultado =



ano = int(input('que ano vc nasceu '))

idade = 2022 - ano
print('você tem', idade, 'anos, então')
if idade < 16:
    print('você não pode votar e não pode tirar uma CNH')
if idade >= 16 and idade < 18:
    print('você pode votar mas não pode tirar uma CNH')
if idade > 18:
    print('você pode votar e tirar uma CNH')
