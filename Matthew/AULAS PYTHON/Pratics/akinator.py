
import time
import sys

separar = '*'*75
welcome = '     WELCOME TO MY LITTLE SOFTWARE PRANK \n'
for char in welcome:
          time.sleep(0.08)
          sys.stdout.write(char)
          sys.stdout.flush()
print(separar)
apresentação = 'OLÁ, MEU NOME É JASON TODDY, A NOVA INTELIGÊNCIA ARTIFICIAL DA UP AGENCY! \n'
for char in apresentação:
          time.sleep(0.08)
          sys.stdout.write(char)
          sys.stdout.flush()
time.sleep(1)
print(separar)
hoje = 'HOJE, VOU ADIVINHAR QUEM VOCÊ É \n '
pergunta = 'VOU FAZER ALGUMAS PERGUNTAS! \n'
preparado = 'PREPARADO(a)? /n'
for char in hoje:
          time.sleep(0.06)
          sys.stdout.write(char)
          sys.stdout.flush()
print(separar)

for char in pergunta:
          time.sleep(0.06)
          sys.stdout.write(char)
          sys.stdout.flush()
print(separar)

for char in preparado:
          time.sleep(0.06)
          sys.stdout.write(char)
          sys.stdout.flush()
time.sleep(2)

ask1 = str(input('COMO VOCÊ CONHECEU A UP?: '))
time.sleep(0.7)
ask2 = str(input('DESDE QUE ENTROU AQUI, O QUE VEM ACHANDO DA EMPRESA?: '))
time.sleep(0.7)
print('SHOW! ESPERO QUE CONTINUE EVOLUINDO ACHANDO ISSO DE NÓS')




                        # PESSOAS
keu1 = 'Você seria a Lutadora Mais criativa do Desing?'
fabricio = 'Seria o famoso Bilíonario Fabricião?'
math = ' Você seria o Futuro Papai do ano?'
lari = 'Você seria a futura formada em Moda mais foda em Design?'
gusta = "Você é o dançarino Mais foda da progração?"
vitin = "VOCÊ É O VITINN?"
samuel = 'você é o Samuel?'
mateus = 'VOCÊ É O MATEUS?'

#                         #RERSPOSTAS
# answer1 = ["design", "performance", "suporte",]
# answer2 = ["feminino", "masculino"]
# answer3 = ["leste", "oeste", "sul", "norte"]
# answer4 = ["sim", "não"]

                                                        #PERGUNTAS
perto = 'HMMM... ESTOU CHEGANDO PERTO! \n'
perto2 = 'CARAMBA, JA SEI QUEM VOCÊ É AHAHA \n'

estiloso = str(input('Voce se considera estiloso(a)? '))
if estiloso == 'sim':
    for char in perto:
          time.sleep(0.08)
          sys.stdout.write(char)
          sys.stdout.flush()
time.sleep(1)
papai = str(input('E VOCÊ POR UM ACASO VAI SER PAPAI ESSE ANO? '))
if papai == 'sim':
    print(math)
else:
    salgadinho = str(input('CERTO, ENTÃO VOCÊ COSTUMA COMPRAR SALGADINO DURANTE O TRABALHO? '))
    if salgadinho == 'sim':
        for char in perto2:
          time.sleep(0.08)
          sys.stdout.write(char)
          sys.stdout.flush()
        luta = str(input('VOCÊ LUTA NOS DIAS LIVRES? '))
        if luta == 'sim':
            print(keu1)
            sys.exit()
        else:
            print('error')



quieta = str(input('VOCÊ GERALMENTE É MAIS QUIETA(O) NO ESCRITÓRIO? '))
if quieta == 'sim':
    usp = str(input('VOCÊ POR UM ACASO JA FEZ ALGUM CURSO NA USP? '))
    if usp == 'sim':
        print(lari)
        sys.exit()
    else:
        print(fabricio)
        sys.exit()

internet = str(input('VOCÊ COMPROU ALGO PELA NINTERNET RECENTEMENTE QUE DEMOROU MUITO? '))
if  internet == 'sim':
    pneu = str(input('VOCÊ TROCOU UM PNEU DE CARRO RECENTEMENTE? KKKKKK '))
    if pneu == 'sim':
        print(gusta)
        sys.exit()
    else:
        print(vitin)
        sys.exit()
else:
    notebook = str(input('VOCÊ COMPROU UM NOTEBOOK CARO RECENTEMENTE? '))
    if notebook == 'sim':
        print(samuel)
        sys.exit()
    else:
        queimou = str(input('VOCÊ JA QUEIMOU UM DISPOSITIVO DO(A) COMPANHEIRO(A) ALGUMA VEZ? '))
        if queimou == 'sim':
            print(mateus)
            sys.exit()

        




        


    

   



    





# estiloso = str(input('Voce se considera estiloso(a)? '))
# estiloso.lower()
# if estiloso == 'sim':
#     print(math)
# else:
#     salgado = str(input('você costuma comprar salgadinho durante o trabalho? '))
#     if salgado == 'sim':
#         luta = str(input('você luta no seus momentos livres? '))
#         if luta == 'sim':
#             print(keu1)
#         else:
#             quieta = str(input('você geralmente é mais quieta(o) no escritorio?'))
#             if quieta == 'sim':
#                 usp = str(input('Você ja fez algum curso na USP?'))
#                 if usp == 'sim':
#                     print(lari)
#                 else:
#                     iphone = str(input('você tem um iphone 12?'))
#                     if iphone == 'sim':
#                         print(fabricio)
#             else:

#     else:
#         pneu = str(input('você trocou um pneu de carro recentemente? '))
#         if pneu  == 'sim':
#             print(gusta)




                                                             

                                #final questions
# setorAnswer1 = str(input('Qual setor da Up você trabalho?: '))
# generoAnswer2 = str(input('Qaul seu Gênero?: '))
# regiaoAnswer3 = str(input('Qual zona de são paulo você mora?: '))



# # if 
# if (setorAnswer1.lower() == answer1[0]) and (generoAnswer2.lower() == answer2[0]) and (regiaoAnswer3.lower() == answer3[0]):
#    print(keu1)

# if (setorAnswer1.lower() == answer1[0]) and (generoAnswer2.lower() == answer2[1]) and (regiaoAnswer3.lower() == answer3[3]):
#     print(math)

# if (setorAnswer1.lower() == answer1[0]) and (generoAnswer2.lower() == answer2[0]) and (regiaoAnswer3.lower() == answer3[2]):
#     print(lari)

# if (setorAnswer1.lower() == answer1[1]) and (generoAnswer2.lower() == answer2[1]) and (regiaoAnswer3.lower() == answer3[2]):
#     print(fabricio)

# # else:
# #     print('erro')

# # men = str=(input('você é homem?'))a
# # if men == "Sim":
# #     print('opa, to quase adivinhando quem é...')
# # ai = str=(input('você gosta de design?'))
# # if ai == 'Sim':
# #     print('Você é o math')
# # else:
# #     print('ok, continua ai que vou descobrir quem você é')
    
# # m2 = str(input('Você é uma mulher? '))
# # if m2 == 'Sim':
# #     print('Ok, estou chegando mais perto')
# # mulher2 = str(input("você fez moda? "))
# # if mulher2 == "sim":
# #     print('show, então você é a Lari!')













