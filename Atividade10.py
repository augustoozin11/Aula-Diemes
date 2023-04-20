def calcular_media(lista):
    soma = 0
    for numero in lista:
        soma += numero
    media = soma / len(lista)
    return media

numeros = [10, 20, 30, 40, 50]
media = calcular_media(numeros)
print("A média dos números é:", media)
