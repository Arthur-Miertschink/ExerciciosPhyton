valoresPares = 0

valoresImpares = 0

for value in range (10, 100):
  if (value % 2 == 0):
    valoresPares += value
  else:
    valoresImpares += value

print(f'A soma dos valores paraes é: {valoresPares}.', end=' ')
print(f'Já a soma dos valores ímpares é: {valoresImpares}.')