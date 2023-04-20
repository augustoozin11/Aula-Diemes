def ler_temperatura():
    temperatura = float(input("Digite a temperatura em Celsius: "))
    return temperatura

def converter_fahrenheit(temperatura_celsius):
    temperatura_fahrenheit = (9 * temperatura_celsius + 160) / 5
    return temperatura_fahrenheit

def mostrar_resultado(temperatura_fahrenheit):
    print("A temperatura em Fahrenheit é:", temperatura_fahrenheit)

temperatura_celsius = ler_temperatura()
temperatura_fahrenheit = converter_fahrenheit(temperatura_celsius)
mostrar_resultado(temperatura_fahrenheit)
