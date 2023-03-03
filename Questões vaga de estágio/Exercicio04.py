distancia_total = 100
velocidade_carro = 110
velocidade_caminhao = 80
tempo_pedagio = 5 / 60

# x + y = 100
# (100 - y) / 110 = (y / 80) + (2 x 5 / 60)
# y = 53,33 km

y = (distancia_total / (velocidade_carro + velocidade_caminhao)) * velocidade_caminhao
x = distancia_total - y

distancia_ribeirao = x
distancia_franca = y + tempo_pedagio * 2 * velocidade_caminhao

if distancia_ribeirao < distancia_franca:
    print("O carro está mais próximo de Ribeirão Preto.")
else:
    print("O caminhão está mais próximo de Ribeirão Preto.")
