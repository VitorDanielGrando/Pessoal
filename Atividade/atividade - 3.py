# A empresa Hipotheticus paga R$10,00 por hora normal 
# trabalhada, e R$15,00 por hora extra. Faça um 
# algoritmo para calcular e imprimir o salário 
# bruto e o salário líquido de um determinado 
# funcionário. Considere que o salário líquido é 
# igual ao salário bruto descontando-se 10% de 
# impostos.

print(100*"-")
h = float(input("Insira a quantiedade de horas trabalhadas no mês: "))
print(100*"-")

he = h - 160 
hn = h - he
sb = ((hn * 10) + (he * 15))
desconto = (10 / 100) * sb
sl = sb - desconto

print(f"O salario Bruto deste mês foi de R$:{sb}")
print(f"O deconto de 10% é R$:{desconto}")
print(f"O salário liquido  ficou R$:{sl}")
print(100*"-")