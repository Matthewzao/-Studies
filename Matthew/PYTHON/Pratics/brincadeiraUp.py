import time

for i in range (5):
    
    nome = str(input('qual seu nome? '))
    nomeAtt = nome.lower()
    if nomeAtt == "keu":
        for n in range(3):
            print('analisando..')
            time.sleep(1)
        print('FUTURA LUTADORA')
    if nomeAtt == 'math':
        for n in range(3):
            print('analisando..')
            time.sleep(1)
        print('O PAI DE UM FUTURO MENINÃO')
    if nomeAtt == "gustavo":
        for n in range(3):
            print('analisando..')
            time.sleep(1)
        print('o cara que vai casar no final do ano')
    elif nomeAtt == 'fabricio':
        for n in range(3):
            print('analisando..')
            time.sleep(1)
        print('futuro bilionário')
    elif nomeAtt == 'mateus':
        for n in range(3):
            print('analisando..')
            time.sleep(1)
        print('Futuro bilionário e pai do Mateuzinho Jr.')
    print('boa tarde {}'.format(nome))
    time.sleep(1)
    print('*****PRÓXIMO*****')
    time.sleep(1)
print("finished")
