#  Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
# a)  a idade dessa pessoa em anos;
# b)  a idade dessa pessoa em meses;
#c ) a idade dessa pessoa em dias;
# d)  a idade dessa pessoa em semanas.

print(100*"-")
ano = int(input("Insira o seu ano de nascimento: "))
ano1 = int(input("Insira o ano atual: "))
print(100*"-")

ia = ano1 - ano
m = ia * 12
d = ia * 365
s= d /  7

print(100*"-")
print(f"Você possio {ia} anos de vida!")
print(f"Você possio {m} meses de vida!")
print(f"Você possio {s} semanas de vida!")
print(f"Você possio {d} dias de vida!")
print(100*"-")