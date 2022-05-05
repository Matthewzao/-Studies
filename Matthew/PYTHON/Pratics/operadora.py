# UMA OPERADORA DE TELEFONIA COBRA R$50.00 POR UM PLANO BÁSICO QUE DA DIREITO A 100 MINUTOS. CADA MINUTO EXCEDENTE CUSTA R$2.00

minutos = int(input("Digite a quantidade de minutos: "))

valorPago = 50.0
if minutos > 100:
    valorPago = valorPago + 2 * (minutos -100)
    print("Você pagará o total de",valorPago)
else:
    print(50.0)
