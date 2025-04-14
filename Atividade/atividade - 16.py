# Faça um algoritmo que receba o peso de uma pessoa, calcule e mostre:

# a)  o novo peso se a pessoa engordar 15% sobre o peso digitado;
# b)  o novo peso se a pessoa emagrecer 20% sobre o peso digitado.


print("-"*100)
peso = float(input("Insira seu peso: "))
print("-"*100)

porcentagem1 = (15 / 100) * peso
peso1 = peso + porcentagem1

porcentagem2 = (20/100)* peso
peso2 = peso - porcentagem2


print(f"Caso você engorde 15%. ficaria com o peso: {peso1}")
print(f"Caso você emagreça 20%. ficaria com o peso: {peso2}")
print("-"*100)