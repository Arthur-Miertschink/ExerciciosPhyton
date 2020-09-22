values = []

n = int(input('Digite um valor que deseja obter os múltiplos, lembre-se, o valor precisa ser maior ou igual a 2: '))

limiteSuperior = int(input('Digite o valor do limite superior do intervalo que deseja obter os múltiplos: '))

limiteInferior = int(input('Digite o valor do limite inferior do intervalo que deseja obter os múltiplos:'))

if (n < 2):
  print('n Não pode ser menor do que 2')
elif (limiteSuperior < limiteInferior):
  print('Não podemos ter um limite inferior maior do que o superior')
else:
  for value in range(limiteInferior, limiteSuperior + 1):
    if (value % n == 0):
      values.append(value)
  print(f'Os valores múltiplos de {n} dentro do intervalo {limiteInferior, limiteSuperior} são: {values}')