#  Calcule o volume de uma caixa d'água cilíndrica.

print(100*"-")
r = float(input("Insira o raio da caixa d'água: "))
h = float(input("Insira a altura da caixa d'água: "))
print(100*"-")

volume = 3.14 * (r * r) * h

print(100*"-")
print(f"O volume da caixa d'água é {volume}")
print(100*"-")