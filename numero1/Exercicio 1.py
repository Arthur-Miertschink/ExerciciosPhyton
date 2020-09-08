"""
Exercício 1:
"""

# a)

catetoAdjascente = float(input('Qual é a medida do cateto adjascente do triângulo desejado: '))

catetoOposto = float(input('Qual é a medida do cateto oposto do triângulo desejado: '))


hipotenusa = float(((catetoOposto ** 2) + (catetoAdjascente ** 2)) ** 0.5)

print(f'O valor da hipotenusa é: {hipotenusa: .2f}')




