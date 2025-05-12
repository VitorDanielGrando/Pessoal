# Faça um algoritmo que receba dois números, calcule e mostre a divisão 
# do primeiro número pelo segundo. Sabe-se que o segundo número não 
# pode ser zero, portanto não é necessário se preocupar com validações.

print(100*"-")
n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
print(100*"-")

while n2 == 0 :
    n2 = float(input("O segundo número nao pode ser zero, tente novamnete: "))
    print(100*"-")



vt = n1 / n2

print(f"O valor da divisão é {vt}")
print(100*"-")