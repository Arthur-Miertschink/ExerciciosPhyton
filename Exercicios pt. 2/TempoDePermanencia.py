print('Quanto tempo você percebeu no laboratório')

permanenciaEmSegundos = int(input('Digite o tempo de permanência do aluno no laboratório (em segundos): '))

if(permanenciaEmSegundos < 0):
    print('O valor está incorreto, digite novamente.')
else:
    horas = permanenciaEmSegundos // 3600
    segundosRestantesHora = permanenciaEmSegundos % 3600

    minutos = segundosRestantesHora // 60

    segundos = segundosRestantesHora % 60

    print(f'O usuário ficou {horas} hora(s), {minutos} minutos e {segundos} segundos no laboratório da UVV.')