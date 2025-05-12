# Como calcular a quantidade de novelos de lã necessários 
# para produzir cada blusa em uma confecção, considerando 
# que cada blusa requer uma quantidade de 120 metros de 
# fio e que cada novelo contém 125 de metros de fio?

print(100*"-")
blusas = int(input("Insira a quantidade de blusas que serao confeccionadas: "))

ndm = 120 * blusas
ndn = ndm / 125

print(100*"-")
print(f"Serão necessários {ndn} novelos de lã!")
print(f"Sendo necessários {ndm} metros de lã para confeccionar as {blusas} blusas de lã")
print(100*"-")