matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

soma_elementos = 0  

for linha in matriz:
    for elemento in linha:
        soma_elementos += elemento 
        
print("A matriz é:")
for linha in matriz:
    print(linha)

print("A soma de todos os elementos é:", soma_elementos)