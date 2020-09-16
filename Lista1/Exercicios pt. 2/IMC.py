print('Calclculando IMC')

massa = float(input('Digite sua massa (kg): '))

altura = float(input('Digite sua altura (m): '))

if(massa <= 0 or altura <= 0):
    print('A altura e/ou a massa foram digitados incorretamente. Tente novamente.')
else:
    imc = massa / (altura ** 2)
    if (imc < 18.5):
        print(f"Seu IMC = {imc: .2f}  está classificado como magreza.")
    elif (imc < 25):
        print(f'Seu IMC = {imc: .2f}  está classificado como saudável')
    elif (imc < 30):
        print(f'Seu IMC = {imc: .2f}  está classificado como sobrepeso.')
    elif (imc < 35):
        print(f'Seu IMC = {imc: .2f}  está classificado como obesidade grau I.')
    elif(imc < 40):
        print(f'Seu IMC = {imc: .2f} está classificado como obesidade grau II (severa).')
    else:
        print(f'Seu IMC = {imc: .2f}  está classificado como obesidade grau III (mórbida).')