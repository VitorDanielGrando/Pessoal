# Faça um algoritmo que calcule e mostre a área de um trapézio. 
# Sabe-se que: A = (base maior + base menor)* altura)/2 ; ,,0,,

print(100*"-")
B = float(input("Insira a base maior:"))
b = float(input("Insira a base menor:"))
h = float(input("Insira a altura:"))
print(100*"-")

A = ((B + b)* h) / 2

print(f"A área do trpézio é {A}") 
print(100*"-")