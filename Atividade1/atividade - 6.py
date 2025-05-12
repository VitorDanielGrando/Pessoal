 # A fábrica de refrigerantes Meia-Cola vende seu produto em três formatos: lata de 350 ml, 
 # garrafa de 600 ml e garrafa de 2 litros. Se um comerciante compra uma determinada 
 # quantidade de cada formato, faça um algoritmo para calcular quantos litros de 
 # refrigerante ele comprou.

print(100*"-")
lata = int(input("Insira a quantiedade de latinhas desejadas para compra:  (caso nao queira comprar latas digite 0)"))
 
vlata = (lata * 350) / 1000
 
print(100*"-")
garrafa = int(input("Insira a quantiedade de garrafas desejadas para compra:  (caso nao queira comprar garrafas digite 0)"))
 
vg = (lata * 600) / 1000

print(100*"-")
litros = int(input("Insira a quantiedade de Garrafas grandes desejadas para compra:  (caso nao queira garrafas grandes digite 0)"))
 
vgg = (lata * 600) / 1000


vt = vlata + vg + vgg

print(100*"-")
print(f"O total de liros obtidos na compra foi de {vt} litros")
print(100*"-")