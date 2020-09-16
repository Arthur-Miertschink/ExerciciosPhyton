print('Vamos converter temperaturas')

escalaEscolhida = int(input('Selecione a escala de entrada: ( 1: Fahrenheit // 2: Celsius ): '))



if(escalaEscolhida != 1 and escalaEscolhida != 2):
    print('A escala de temperatura foi informada incorretamente. Digite novamente.')
else:
    temperaturaInformada = float(input('Digite a temperatura que deseja converter: '))
    if (escalaEscolhida == 1):
        temperaturaConvertida = (temperaturaInformada - 32) / 1.8
        print(f'{temperaturaInformada}º em Fahrenheit equivale a {temperaturaConvertida}º em Celsius')
    else:
        temperaturaConvertida = (temperaturaInformada * 1.8) + 32
        print(f'{temperaturaInformada}º em Celsius equivale a {temperaturaConvertida}º em Fahrenheit')




