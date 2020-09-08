print('Arrecadação e público do jogo de futebol')

valorDoIngresso = float(input('Digite o valor do ingresso (R$): '))

publicoTotal = 0

receitaTotal = 0

if(valorDoIngresso < 0):
    print('O valor do ingresso foi digitado incorretamente. Por favor, digite novamente.')
else:
    while True:
        print('O que deseja fazer: ')
        print('1: Inserir um novo espectador')
        print('0: Encerrar a entrada e visualizar os dados (público e arrecadação total)')
        opcao = int(input('Digite a opção desejada: '))

        if opcao == 0:
            print(f'O púbilco total: {publicoTotal} pessoas.')
            print(f'A Receita total foi de: R$ {receitaTotal}.')
            break
        if opcao != 1 and opcao != 0:
            print('Opção inválida. Digite novamente.')
        else:
            idadeDoEspectador = int(input('Digite a idade do espectador: '))
            doouAlimento = \
                int(input('O espectador trouxe pelo menos 1 kg de alimento para doação? (1 = Sim // 2 = Não): '))
            if idadeDoEspectador < 0:
                print('A idade foi digitada incorretamente. Por favor, digite novamente.')
            elif idadeDoEspectador <= 10:
                valorDoIngresso = 0
                receitaTotal += valorDoIngresso
                publicoTotal += 1
            elif idadeDoEspectador <= 17 or doouAlimento == 1:
                valorDoIngressoMeia = valorDoIngresso / 2
                receitaTotal += valorDoIngressoMeia
                publicoTotal += 1
            else:
                receitaTotal += valorDoIngresso
                publicoTotal += 1



