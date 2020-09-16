# d)

print('Vamos calcular a área e o comprimento de um círculo!')

piEspecifico = input('A questão possui um valor de pi especificado? (Caso não, o sistema irá considerar π = 3.14): ')

if (piEspecifico == "Sim"):
    pi = float(input('Digite o valor de π fornecido pela questão: '))
else:
    pi = 3.14

raio = float(input('Digite o valor do raio do círculo (R): '))

area = pi * (raio ** 2)

comprimento = 2 * pi * raio

print(f'Área = {area: .2f}')

print(f'Comprimento = {comprimento: .2f}')