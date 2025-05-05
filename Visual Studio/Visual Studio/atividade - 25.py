#Faça um algoritmo que receba o valor dos catetos de um triângulo, calcule e mostre o valor da hipotenusa.
import math

print(100*"-")
c1 = float(input("Insira o valor do primeiro cateto: "))
c2 = float(input("Insira o valor do segundo cateto: "))
print(100*"-")

h = math.sqrt( (c1 ** 2) + (c2 ** 2) )

print(100*"-")
print(f"O cateto da hipotenusa é {h}")
print(100*"-")