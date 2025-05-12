# Faça um algoritmo que receba duas notas, calcule e mostre a média 
# ponderada dessas notas, considerando peso 2 para a primeira nota 
# e peso 3 para a segunda nota.

print(100*"-")
n1 = float(input("Insira a primeira nota:"))
n2 = float(input("Insira a Segunda nota:"))
n3 = float(input("Insira a Terceira nota:"))
print(100*"-")

media = ((n1 * 2) + n3 + (n2 * 3)) / 6

print(f"A media ponderada fechou em: {media}")
print(100*"-")