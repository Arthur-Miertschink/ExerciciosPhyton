print('Convertendo moedas')



moedaDeEntrada = int(input('Digite a moeda que deseja converter ( 1: Real // 2: Dólar // 3: Libra ): '))

moedaDeSaida = int(input('Digite a moeda desejada ( 1: Real // 2: Dólar // 3: Libra ): '))

if (moedaDeEntrada != 1 and moedaDeEntrada != 2 and moedaDeEntrada != 3):
    print('A moeda de entrada foi digitada incorretamente. Por favor, digite novamente.')
elif(moedaDeSaida != 1 and moedaDeSaida!= 2 and moedaDeSaida != 3):
    print('A moeda de saída foi digitada incorretamente. Por favor, digite novamente.')
else:
    valorDesejado = float(input('Digite o valor que deseja converter: '))
    if (moedaDeEntrada == 1 and moedaDeSaida == 2):
        valorConvertido = valorDesejado * 0.19
        print(f'R$ {valorDesejado} em Dólares é US$ {valorConvertido}')
    elif (moedaDeEntrada == 1 and moedaDeSaida == 3):
        valorConvertido = valorDesejado * 0.15
        print(f'R$ {valorDesejado} em Libras é £ {valorConvertido}')
    elif (moedaDeEntrada == 2 and moedaDeSaida == 1):
        valorConvertido = valorDesejado * 5.32
        print(f'US$ {valorDesejado} em Real é R$ {valorConvertido}')
    elif (moedaDeEntrada == 2 and moedaDeSaida == 3):
        valorConvertido = valorDesejado * 0.78
        print(f'US$ {valorDesejado} em Libras é £ {valorConvertido}')
    elif (moedaDeEntrada == 3 and moedaDeSaida == 1):
        valorConvertido = valorDesejado * 6.81
        print(f'£ {valorDesejado} em Reais é R$ {valorConvertido}')
    elif (moedaDeEntrada == 3 and moedaDeSaida == 2):
        valorConvertido = valorDesejado * 1.28
        print(f'£ {valorDesejado} em Dólares é US$ {valorConvertido}')
    else:
        print('Algo de errado aconteceu. Tente novamente.')

