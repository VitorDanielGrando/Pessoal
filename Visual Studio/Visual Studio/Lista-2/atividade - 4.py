# A granja Frangotech possui um controle automatizado de cada frango da sua produção. 
# No pé direito do frango há um anel com um chip de identificação; no pé esquerdo 
# são dois anéis para indicar o tipo de alimento que ele 
# deve consumir. Sabendo que o anel com chip custa R$4,00 e o anel de alimento 
# custa R$3,50, faça um algoritmo para calcular o gasto total da granja para 
# marcar todos os seus frangos.

print(100*"-")
galinha = int(input("Insira o numero de galinha da granja: "))

v1 = (galinha * 4)
v2 = (galinha * 2) * 3.50
v3 = v1 + v2

print(100*"-")
print(f"O valor para comprar os anéis necessários é R$:{v3}")
print(f"Sendo {v1} o valor total dos anéis de R$: 4,00")
print(f"E {v2} sendo o valor dos anéis de R$: 3,50")
print(100*"-")