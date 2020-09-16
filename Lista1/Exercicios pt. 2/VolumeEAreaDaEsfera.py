print('Vamos calcular o volume e a área da esfera')

pi = 3.14

raio = float(input('Digite o raio da esfera (em metros): '))

if(raio <= 0):
    print('O raio está incorreto, tente novamente!')
else:
    area = 4 * pi * (raio ** 2)

    volume = (4/3) * pi * (raio ** 3)

    print(f'A area e o volume da esfera são, respectivamente: {area: .2f} m^2 e {volume: .2f} m^3')