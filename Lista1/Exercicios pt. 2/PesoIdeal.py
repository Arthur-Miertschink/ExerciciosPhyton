print('Você está no seu peso ideal')

alturaPessoa = float(input('Digite sua altura (em metros): '))

print('Qual o seu sexo: ')
print('1: Masculino')
print('2: Feminino')


sexo = int(input('Selecione sua opção: '))

if(alturaPessoa <= 0):
    print('Altura inválida, digite novamente')
elif(sexo == 1):
    pesoHomem = (72.7 * alturaPessoa) - 58
    print(f'Seu peso ideal é: {pesoHomem: .2f}')
elif(sexo == 2):
    pesoMulher = (62.1 * alturaPessoa) - 44.7
    print(f'Seu peso ideal é: {pesoMulher: .2f}')
else:
    print('A opção escolhida não é válida, tente novamente.')
