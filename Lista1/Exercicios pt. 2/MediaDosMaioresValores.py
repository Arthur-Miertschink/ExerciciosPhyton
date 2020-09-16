print('Exercicio 16')

valores = []

maxValoresPermitidos = 3

quantidadeDeValoresDigitados = 0

v1 = 0

v2 = 0

while quantidadeDeValoresDigitados < maxValoresPermitidos:
    numeroDigitado = float(input('Digite um valor: '))
    if (numeroDigitado not in valores):
        valores.append(numeroDigitado)
    else:
        print(f'O número {numeroDigitado} já foi digitado. Por favor digite outro número.')
        maxValoresPermitidos += 1
    quantidadeDeValoresDigitados += 1

for val in valores:
    if (val > v1):
        v1 = val

for val2 in valores:
    if(val2 > v2 and val2 < v1):
        v2 = val2

print(f'A média dos valores {v1} e {v2} é: {(v1 + v2)/ 2}')