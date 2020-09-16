print('Exercicio 17')

valor1 = float(input('Digite um valor: '))

valor2 = float(input('Digite um valor: '))

valor3 = float(input('Digite um valor: '))

if(valor1 < 0 or valor2 < 0 or valor3 < 0):
    print('Não são permitidos valores negativos. Por favor, digite novamente.')
elif(valor1 > (valor2 + valor3) or valor2 > (valor1 + valor3) or valor3 > (valor1 + valor3)):
    print('Os valores digitados não correspondem as medidas de um triângulo.')
else:
    if(valor1 == valor2 == valor3):
        print(f'O triângulo de valores {valor1, valor2, valor3} é um triângulo Equilátero.')
    elif(valor1 == valor2 or valor1 == valor3 or valor2 == valor3):
        print(f'O triângulo de valores {valor1, valor2, valor3} é um triângulo Isósceles.')
    else:
        print(f'O triângulo de valores {valor1, valor2, valor3} é um triângulo Escaleno.')