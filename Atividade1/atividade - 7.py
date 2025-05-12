# Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar. 
# Faça um algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor total 
# economizado, em reais. Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e 
# ainda moedas de 1 real. Não havendo moeda de um tipo, a quantidade respectiva é zero.

print(100*"-")
m1 = int(input("Insira a quantiedade de moedas de 0,01 centavo: "))
v1 = m1 * 0.01


print(100*"-")
m5 = int(input("Insira a quantiedade de moedas de 0,05 real: "))
v5 = m5 * 0.05


print(100*"-")
m10 = int(input("Insira a quantiedade de moedas de 0,10 real: "))
v10 = m10 * 0.10


print(100*"-")
m25 = int(input("Insira a quantiedade de moedas de 0,25 real: "))
v25 = m25 * 0.25


print(100*"-")
m50 = int(input("Insira a quantiedade de moedas de 0,50 real: "))
v50 = m50 * 0.50

vt = v1 + v5 + v10 + v25 + v50

print(100*"-")
print(f"O valor total de todas as moedas é de {vt} reais!")
print(100*"-")