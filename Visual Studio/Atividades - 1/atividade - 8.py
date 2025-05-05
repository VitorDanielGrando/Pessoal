# Num dia de sol, você deseja medir a altura de um prédio, porém, 
# a trena não é suficientemente longa. Assumindo que seja possível 
# medir sua sombra e a do prédio no chão, e que você lembre da sua 
# altura, faça um algoritmo para ler os dados necessários e calcular 
# a altura do prédio.

print(100*"-")
altura = float(input("Insira a sua altura: "))
sombra = float(input("Insira a altura de sua sombra: "))
sombrap = float(input("Insira a altura da sombra do prédio: "))
print(100*"-")

alturap = (altura * sombrap) / sombra

print(f"A altura do prédio é de: {alturap}")
print(100*"-")
