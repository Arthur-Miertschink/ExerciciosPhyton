# h)

print('Quanto custa para pintar o cilindro?')

inputRaio = float(input('Digite o raio do Cilindro desejado: '))

inputAltura = float(input('Digite a altura do cilindro desejado: '))

piEspecifico = int(input('A questão possui um valor de pi especificado? (Caso não, o sistema irá considerar π = 3.14) // (1: Sim // 2: Não): '))

if (piEspecifico == 1):
        pi = float(input('Digite o valor de π fornecido pela questão: '))
elif (piEspecifico == 2):
     pi = 3.14
else:
    print('Opção não disponível. Por Favor, digite novamente.')
    exit()

areaDaBase = pi * (inputRaio ** 2)

areaLateral = (2 * pi) * inputRaio * inputAltura

areaTotal = (2 * areaDaBase) + areaLateral

print(f'A área total do cilindro desejado é: {areaTotal} m^2')

precoDaLata = 50

quantidadeDeLatas = areaTotal / 15

gastoTotal = quantidadeDeLatas * precoDaLata

print(f'Para pintar o cilindro desejado, será necessário {quantidadeDeLatas: .2f} latas. O custo total será de R$ {gastoTotal: .2f}')