print('Vamos calcular a autonomia do carro')

consumo = 10  # KM/Litro

ladoDoTanque = float(input('Digite o tamanho do lado do tanque do carro (em metros): '))

alturaPreenchidaDoTanque = float(input('Digite a altura equivalente ao volume de combustível presente no tanque: '))

volumeTotalDoTanque = (ladoDoTanque ** 2) * alturaPreenchidaDoTanque

volumeEmLitros = volumeTotalDoTanque * 1000

autonomia = volumeEmLitros * consumo

print(f'A autonomia do veículo é de {autonomia: .2f} km.')
