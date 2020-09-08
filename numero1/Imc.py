# e)

print('Calculando IMC')

nome = input('Digite seu nome: ')

print(f'Olá! {nome},')

ask = input('Vamos calcular o seu IMC? (Sim ou Não) ')

if ask == 'Sim':
    massa = float(input('Quantos quilos você pesa: '))
    altura = float(input('Entre com sua altura (em metros): '))

    imc = massa / (altura ** 2)

    print(f'Seu IMC é: {imc: .2f}')

else:
    print('Volte Sempre!')