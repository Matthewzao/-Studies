

# for i in range(2):
#     alturaHomem = '72.7'
#     alturaMulher = '62.8'
#     generoHomem = 'masculino'
#     generoFeminino = 'feminino'

#     ask1 = str(input('qual seu genero: '))
#     ask2 = float(input('qual sua altura: '))

#     if ask1 == 'masculino' and ask2 == 72.7:
#         print('seu peso ideial é 58')

#     if ask1 == 'feminino' and ask2 == 62.1:
#         print('seu peso ideal é 44.7')
 

m = 'feminino'
h = 'masculino'

ask1 = str(input('qual seu genero? '))
ask2 = float(input('qual a sua altura? '))

if ask1 == m:
    print((ask2 *62.1) - 44.7)

if ask1 == h:
    print((ask2 *72.7) - 58)