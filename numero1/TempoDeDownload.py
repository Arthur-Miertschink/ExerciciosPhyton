from time import time
print('Vamos calcular o tempo de download de sua internet')

velocidadeInternet = float(input('Quantos Megabytes por segundo sua internet baixa normalmente: '))

tamanhoArquivo = float(input('Qual o tamanho do arquivo, em megabytes, que pretende baixar: '))

tempoDeDownload = tamanhoArquivo / velocidadeInternet

print(f'Sua internet leva {tempoDeDownload: .2f} minutos para baixar esse arquivo')

