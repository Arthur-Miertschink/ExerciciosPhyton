print('Calculando o reajuste da mercadoria')

precoDaMercadoria = float(input('Digite o preco da mercadoria (R$): '))

escolha = int(input(f'Quer acrescentar ou descontar ao preço da mercadoria (1: Descontar // 2: Acrescentar ): '))

if(precoDaMercadoria < 0):
    print('O preço digitado está incorreto. Por favor, digite novamente')
else:
    if (escolha != 1 and escolha != 2):
        print('Opção não encontrada. Digite novamente.')
    if (escolha == 1):
        precoDaMercadoria = precoDaMercadoria * 0.97
        print(f'O preço da mercadoria com desconto é: R$ {precoDaMercadoria: .2f}')
    if (escolha == 2):
        precoDaMercadoria = precoDaMercadoria * 1.03
        print(f'O preço da mercadoria com acréscimo é de: R$ {precoDaMercadoria: .2f}')


