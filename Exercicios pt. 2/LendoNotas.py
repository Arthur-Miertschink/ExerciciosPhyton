print('Vamos ler a nota do aluno')

numeroAulas = 10

nome = input('Digite o nome do aluno: ')

av1 = float(input('Digite a nota obtida pelo aluno na AV1: '))

av2 = float(input('Digite a nota obtida pelo aluno na AV2: '))

totalFaltas = int(input('Digite o total de faltas do aluno: '))

mediaParcial = (av1 + av2) / 2

mediaParaAprovacao = 7.0

minimoParaRecuperacao = 3.0

if(av1 < 0 or av2 < 0):
    print('Existem notas com valores incorretos. Digite novamente.')
else:
    if(mediaParcial < minimoParaRecuperacao):
        print(f'O aluno foi reprovado. Sua média parcial foi: {mediaParcial: .2f}')
    elif(mediaParcial < mediaParaAprovacao):
        print(f'O aluno ficou de recuperação. Sua média parcial foi {mediaParcial: .2f}')
        provaFinal = float(input('Digite a nota obtida pelo aluno na prova final: '))
        if((provaFinal + mediaParcial) >= mediaParaAprovacao):
            print(f'O aluno foi aprovado após fazer a prova final. Seu resultado final foi: {(provaFinal + mediaParcial)}')
        else:
            print(f'O aluno está reprovado, pois não conseguiu atingir a nota necessária na prova final. Seu resultado final foi: {(provaFinal + mediaParcial)}')
    elif(totalFaltas > (numeroAulas * 0.25)):
        print(f'O aluno foi reprovado por faltas, pois faltou mais do que 25% das aulas. Sua média parcial foi: {mediaParcial: .2f}')
    else:
        print(f'O aluno foi aprovado. Sua nota final foi: {mediaParcial: .2f}')

