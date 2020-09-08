print('Convertendo moedas')

moedaDeEntrada = int(input('Digite a moeda que deseja converter ( 1: Real // 2: Dólar // 3: Libra ): '))

moedaDeSaida = int(input('Digite a moeda desejada ( 1: Real // 2: Dólar // 3: Libra ): '))

if (moedaDeEntrada != 1 and moedaDeEntrada != 2 and moedaDeEntrada != 3):
    print('A moeda de entrada foi digitada incorretamente. Por favor, digite novamente.')
elif(moedaDeSaida != 1 and moedaDeSaida!= 2 and moedaDeSaida != 3):
    print('A moeda de saída foi digitada incorretamente. Por favor, digite novamente.')
else:
    valorDesejado = float(input('Digite o valor que deseja converter: '))
