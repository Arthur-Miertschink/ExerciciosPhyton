# a)

print('Calculando o reajuste da mercadoria')

precoDaMercadoria = float(input('Digite o preco da mercadoria (R$): '))

porcentagem = float(input('Digite a porcentagem de reajuste: '))

escolha = int(input(f'Quer acrescentar ou descontar ao preço da mercadoria (1: Descontar // 2: Acrescentar ): '))

if (porcentagem < 0):
    print('O valor da porcentagem está incorreto. Por favor, informe-o novamente.')
elif(precoDaMercadoria < 0):
    print('O preço digitado está incorreto. Por favor, digite novamente')
else:
    if (escolha == 1):
        precoDaMercadoria = precoDaMercadoria * (1 - (porcentagem / 100))
        print(f'O preço da mercadoria com desconto é: R$ {precoDaMercadoria: .2f}')
    elif (escolha == 2):
        precoDaMercadoria = precoDaMercadoria * (1 + (porcentagem / 100))
        print(f'O preço da mercadoria com acréscimo é de: R$ {precoDaMercadoria: .2f}')
    else:
        print('Opção não encontrada. Digite novamente.')