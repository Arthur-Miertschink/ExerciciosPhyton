from datetime import datetime
print('Vamos calcular o tempo de download de sua internet')

velocidadeInternet = float(input('Quantos Megabytes por segundo sua internet baixa normalmente (MBPS): '))

tamanhoArquivo = float(input('Qual o tamanho do arquivo, em megabytes, que pretende baixar (em MB): '))

tempoDeDownload = tamanhoArquivo / velocidadeInternet

minutos = tempoDeDownload // 60.0

segundos = tempoDeDownload % 60


print(f'Sua internet leva {minutos} minutos e {segundos: .2f} segundos spara baixar esse arquivo')

