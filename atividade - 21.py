#  Faça um algoritmo que receba o valor do salário mínimo e o valor do 
# salário de um funcionário, calcule e mostre a quantidade de salários 
# mínimos que ganha esse funcionário.

print(100*"-")
sm = float(input("Insira o valor do salário minimo: "))
s = float(input("Insira o valor do seu salário: "))

v = s / sm

print(100*"-")
print(f"Você ganha {v} salários minimos")
print(100*"-")