#Faça um algoritmo que receba o preço de um produto, calcule e 
# mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.

print(100*"-")
produto = float(input("Insira o valor do produto: "))

desconto = (10 / 100) * produto
vt = produto - desconto

print(100*"-")
print(f"O valor final do produto com desconto foi: {vt}")
print(f"O valor do desconto foi de {desconto}")
print("-"*100)