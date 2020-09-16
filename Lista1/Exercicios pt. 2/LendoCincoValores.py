
print('Exercicio 15')

valoresParesLista = []

valoresImparesLista = []

maxValoresPermitidos = 5

v0 = 0

valoresPares = 0

valoresImpares = 0


while v0 < maxValoresPermitidos:
    numeroDigitado = int(input('Digite um valor: '))
    if (numeroDigitado not in valoresParesLista and numeroDigitado > 0 and numeroDigitado % 2 == 0):
        valoresParesLista.append(numeroDigitado)
    elif (numeroDigitado not in valoresImparesLista and numeroDigitado > 0 and numeroDigitado % 2 == 1):
        valoresImparesLista.append(numeroDigitado)
    elif (numeroDigitado < 0):
        print(f'O número {numeroDigitado}, não é positivo. Digite novamente.')
        maxValoresPermitidos += 1
    else:
        print(f'O número {numeroDigitado}, ja foi digitado. Por favor informe outro valor.')
        maxValoresPermitidos += 1
    v0 += 1

for val in valoresParesLista:
        valoresPares += 1
        mediaPar = sum(valoresParesLista) / valoresPares


for val in valoresImparesLista:
    valoresImpares += 1
    mediaImpar = sum(valoresImparesLista) / valoresImpares

print(f'A média dos valores pares é:{mediaPar: .2f} ')
print(f'A média dos valores impares é: {mediaImpar: .2f}')



