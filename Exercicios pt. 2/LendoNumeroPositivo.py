print('Exercício 6)')

numeroDigitado = float(input('Digite um número: '))

numeroDigitadoAoQuadrado = numeroDigitado ** 2

if (numeroDigitadoAoQuadrado % 11 == 0 and numeroDigitadoAoQuadrado % 2 != 0):
    print(f'O número {numeroDigitadoAoQuadrado}, que é o quadrado de {numeroDigitado}, é múltiplo de 11 e ímpar')
elif (numeroDigitadoAoQuadrado % 2 != 0):
    print(f'O número {numeroDigitadoAoQuadrado}, que é o quadrado de {numeroDigitado}, é ímpar mas não múltiplo de 11.')
else:
    print(f'O número {numeroDigitadoAoQuadrado}, que é o quadrado de {numeroDigitado}, não é ímpar mas é múltiplo de 11.')