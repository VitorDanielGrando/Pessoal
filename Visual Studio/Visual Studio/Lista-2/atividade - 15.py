# Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. 
# Faça um algoritmo que receba o salário fixo de um funcionário e o valor de 
# suas vendas, calcule e mostre a comissão e o salário final do funcionário.

print(100*"-")
salario = float(input("Insira seu salário fixo: "))
vendas = int(input("Insira o total de vendas realizadas: "))

porcentagem = (4 / 100) * salario
comissao = porcentagem * vendas
vt = salario + comissao
print("-"*100)
print(f"O valor total com as comissões foi de {vt }")
print(f"O valor da comissão foi de: {comissao}")
print("-"*100)
