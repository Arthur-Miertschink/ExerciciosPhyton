print('Calculando o perimetro do retangulo')

baseRetangulo = float(input('Digite o valor da base do retangulo (em centimetros): '))

alturaRetangulo = float(input('Digite o valor da altura de um retangulo (em centimetros): '))

if (baseRetangulo <= 0 or alturaRetangulo <= 0):
    print('Percebemos que algum valor foi digitado errado, digite novamente')
else:
    perimetro = (2 * baseRetangulo) + (alturaRetangulo * 2) #centimetros

    perimetroEmPolegadas = perimetro / 2.54

    perimetroEmJardas = perimetro / 91.44

    print(f'O perimetro em centímetros é: {perimetro: .2f}')

    print(f'O perimetro em polegadas é: {perimetroEmPolegadas: .2f}')

    print(f'O perimetro em jardas é: {perimetroEmJardas: .2f}')