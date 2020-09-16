from datetime import datetime, timedelta


valorPor30Min = float(input('Digite o valor a ser pago a cada 30 min: '))

horaEntrada = str(input('Digite a hora de entrada (HH:MM): '))
horaSaida = str(input('Digite a hora da saída (HH:MM): '))
fmt = '%H:%M'


tdelta = datetime.strptime(horaSaida, fmt) - datetime.strptime(horaEntrada, fmt)

if tdelta.days < 0:
    print('De acordo com as regras do estacionamento não é possível a permanência por mais de 24h no estabelecimento. Por favor, insira os valores novamente.')
elif(tdelta <= timedelta(minutes=30)):
    valorTotal = valorPor30Min * 0
    print(f'Total a pagar: R$ {valorTotal: .2f}')
else:
    valorTotal = valorPor30Min * (tdelta / timedelta(minutes=30))
    print(f'Total a pagar: R$ {valorTotal: .2f}')














