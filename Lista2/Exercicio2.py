"""
Escrever um algoritmo para exibir os múltiplos de 11, a soma e a média dos múltiplos de 11, em ordem
decrescente (inversa), compreendidos entre o intervalo: [200 100].')
"""

valores = []

soma = 0

for value in range (100, 201):
  if (value % 11 == 0):
    valores.append(value)
    valores.sort(reverse = True)
print(f'Os valores multiplos de 11 dentro do intervalo solicitado são: {valores}')

for value in valores:
  soma += value
print(f'A soma dos valores presente no intervalo é: {soma}')

media = soma / len(valores)

print(f'A média dos valores do intervalo é: {media}')