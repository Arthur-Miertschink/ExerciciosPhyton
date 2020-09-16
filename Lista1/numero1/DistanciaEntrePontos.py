print('Vamos calcular a distância entre dois pontos!!')

pontoPx = float(input('Digite as coordenadas de X do ponto P: '))

pontoPy = float(input('Digite as coordenadas de Y do ponto P: '))

pontoQx = float(input('Digite as coordenadas de X do ponto Q: '))

pontoQy = float(input('Digite as coordenadas de Y do ponto Q: '))

distanciaEntrePontos = ( ((pontoQx - pontoPx) ** 2) + ((pontoQy - pontoPy) ** 2)) ** 0.5

print(f'A distancia entre os pontos é de:{distanciaEntrePontos: .2f} metros')