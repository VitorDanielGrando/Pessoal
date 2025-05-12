# João recebeu seu salário de R$ 1200,00 e precisa pagar duas contas
# (C1=R$ 200,00 e C2=R$120,00) que estão atrasadas. Como as contas estão 
# atrasadas, João terá de pagar multa de 2% sobre cada conta. Faça um 
# algoritmo que calcule e mostre quanto restará do salário do João


c1 = 200
c2 = 120

multa1 = 200 - ((2/100)*200)
multa2 = 120 - ((2/100)*120)
vt = 1200 - multa1 - multa2

print(100*"-")
print(f"Sobrará {vt} do seu salário!")
print(100*"-")

