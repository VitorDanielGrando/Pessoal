# A lanchonete Gostosura vende apenas um tipo de sanduíche,
# cujo recheio inclui duas fatias de queijo, uma fatia de 
# presunto e uma rodela de hambúrguer. Sabendo que cada 
# fatia de queijo ou presunto pesa 50 gramas, e que a 
# rodela de hambúrguer pesa 100 gramas, faça um algoritmo 
# em que o dono forneça a quantidade de sanduíches a fazer,
# e a máquina informe as quantidades (em quilos) de queijo,
# presunto e carne necessários para compra.
print("Seja Bem-Vindo!")
print(100*"-")
s = int(input("Insira a quantiedade de sanduiches que devem ser feitos: "))
print(100*"-")

q = ((s * 2) * 50) / 1000
p = (s * 50) / 1000
h = ((s * 100 )) / 1000


print(f"Deve ser cmprado {q} kilos de queijo! ")
print(f"Deve ser cmprado {p} kilos de presunto! ")
print(f"Deve ser cmprado {h} kilos de hambúrguer! ")
print(100*"-")