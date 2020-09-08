from decimal import Decimal, localcontext

print('Vamos calcular a autonomia de uma caixa d agua de um restaurante')

consumo = 1350 / 1000 # m^3

pi = 3.14

alturaCilindro = float(input('Digite a altura da caixa d água (em metros): '))

raioDoCilindro = float(input('Digite o raio da caixa d água (em metros): '))

volumeDaCaixa = pi * (raioDoCilindro ** 2) * alturaCilindro

autonomiaEmHoras = volumeDaCaixa / consumo



print(f'A autonomia da caixa d água é de {autonomiaEmHoras: .0f} horas')