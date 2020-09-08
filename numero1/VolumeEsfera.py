# f)

print('Calcule o volume em litros de uma esfera: ')

raio = float(input('Digite o raio da esfera (em metros): '))

piEspecifico = input('A questão possui um valor de pi especificado? (Caso não, o sistema irá considerar π = 3.14): ')

if (piEspecifico == "Sim"):
    pi = float(input('Digite o valor de π fornecido pela questão: '))
else:
    pi = 3.14

volumeEsfera = (4/3) * pi * (raio ** 3)

volumeEsferaEmLitros = volumeEsfera * 10000

print(f'O volume da esfera é {volumeEsferaEmLitros: .2f} Litros')