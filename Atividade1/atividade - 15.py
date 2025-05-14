# Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. 
# Faça um algoritmo que receba o salário fixo de um funcionário e o valor de 
# suas vendas, calcule e mostre a comissão e o salário final do funcionário.

salario_fixo = float(input("Digite o salário fixo do funcionário: "))
valor_vendas = float(input("Digite o valor total das vendas: "))

# Calculando a comissão
comissao = valor_vendas * 0.04  # Comissão de 4%

# Calculando o salário final
salario_final = salario_fixo + comissao

# Mostrando o resultado
print("A comissão do funcionário é de: R$", comissao)
print("O salário final do funcionário é de: R$", salario_final)