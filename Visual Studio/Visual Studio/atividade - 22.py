# Faça um algoritmo que calcule e mostre a tabuada de um número digitado pelo usuário.


print(100*"-")
numero = int(input("Insira um numero:"))

print(100*"-")
print(f"\nTabuada do {numero}:\n")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
print(100*"-")