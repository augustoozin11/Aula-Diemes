altura = float(input("Digite a sua altura em metros: "))
peso = float(input("Digite o seu peso em kg: "))

# Calcular IMC
imc = peso / altura ** 2

# Exibir resultado
print("O seu IMC é:", imc)