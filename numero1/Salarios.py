# g)

print('Calculando salários!')

salarioHora = float(input('Quanto vale a sua hora de trabalho: '))

horasTrabalhadasMes = int(input('Quantas horas você trabalha no mês: '))

salarioBruto = salarioHora * horasTrabalhadasMes

inss = 0.08

ir = 0.11

sindicato = 0.05

print(f'Seu salário bruto é {salarioBruto}')

pagamentoInss = salarioBruto * inss

print(f'Você pagou R$ {pagamentoInss: .2f} referente ao INSS ')

pagamentoIr = salarioBruto * ir

print(f'Você pagou R$ {pagamentoIr: .2f} referentes ao IR')

pagamentoSindicato = salarioBruto * sindicato

print(f'Você pagou R$ {pagamentoSindicato} referente ao sindicato')

salarioLiquido = salarioBruto - (pagamentoSindicato + pagamentoIr + pagamentoInss)

print(f'Seu salário líquido é: R$ {salarioLiquido: .2f}')