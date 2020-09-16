print('Convertendo Massa')



massaDeEntrada = int(input('Digite a unidade de massa que deseja converter ( 1: Onça (Oz) // 2: Quilogramas (kg) // 3: Toneladas (T) ): '))

massaDeSaida = int(input('Digite a unidade de massa desejada ( 1: Onça (Oz) // 2: Quilogramas (kg) // 3: Toneladas (T) ): '))

if (massaDeEntrada != 1 and massaDeEntrada != 2 and massaDeEntrada != 3):
    print('A massa de entrada foi digitada incorretamente. Por favor, digite novamente.')
elif(massaDeEntrada != 1 and massaDeEntrada!= 2 and massaDeEntrada != 3):
    print('A massa de saída foi digitada incorretamente. Por favor, digite novamente.')
else:
    valorDesejado = float(input('Digite o valor que deseja converter: '))
    if (massaDeEntrada == 1 and massaDeSaida == 2):
        valorConvertido = valorDesejado * 0.02835
        print(f'{valorDesejado} Oz em Quilogramas é {valorConvertido} kg')
    elif (massaDeEntrada == 1 and massaDeSaida == 3):
        valorConvertido = valorDesejado * 0.00002835
        print(f' {valorDesejado} Oz em Toneladas é {valorConvertido} T')
    elif (massaDeEntrada == 2 and massaDeSaida == 1):
        valorConvertido = valorDesejado * 35.274
        print(f'{valorDesejado} kg em Onça é {valorConvertido} Oz')
    elif (massaDeEntrada == 2 and massaDeSaida == 3):
        valorConvertido = valorDesejado * 0.001
        print(f'{valorDesejado} kg em Toneladas é {valorConvertido} T')
    elif (massaDeEntrada == 3 and massaDeSaida == 1):
        valorConvertido = valorDesejado * 35274
        print(f'{valorDesejado} T em Onça é {valorConvertido} Oz')
    elif (massaDeEntrada == 3 and massaDeSaida == 2):
        valorConvertido = valorDesejado * 1000
        print(f'{valorDesejado} T em Quilogramas é {valorConvertido} kg')
    else:
        print('Algo de errado aconteceu. Tente novamente.')