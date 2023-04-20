def ler_valores():
    tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
    velocidade_media = float(input("Digite a velocidade média durante a viagem (em km/h): "))
    return tempo, velocidade_media

def calcular_distancia(tempo, velocidade_media):
    distancia = tempo * velocidade_media
    return distancia

def calcular_litros(distancia):
    litros_usados = distancia / 12
    return litros_usados

def apresentar_resultado(tempo, velocidade_media, distancia, litros_usados):
    print("Velocidade média:", velocidade_media, "km/h")
    print("Tempo gasto na viagem:", tempo, "horas")
    print("Distância percorrida:", distancia, "km")
    print("Quantidade de litros utilizada na viagem:", litros_usados, "litros")

tempo, velocidade_media = ler_valores()
distancia = calcular_distancia(tempo, velocidade_media)
litros_usados = calcular_litros(distancia)
apresentar_resultado(tempo, velocidade_media, distancia, litros_usados)
