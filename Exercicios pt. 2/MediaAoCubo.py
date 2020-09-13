print('Exercicio 13')

num1 = float(input('Digite um número qualquer: '))

num2 = float(input('Digite um número qualquer: '))

num3 = float(input('Digite um número qualquer: '))

media = (num1 + num2 + num3) / 3

if(media >= 115.2743 and media <= 2305.486):
    print(f'A média destes valores é:{media: .5f}')
else:
    mediaAoCubo = media ** 3
    print(f'A média ao cubo destes valores é: {mediaAoCubo: .5f}')