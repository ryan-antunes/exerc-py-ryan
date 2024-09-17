import math
area = float(input("Digite a area a ser pintada: "))
tinta = 18
preco = 80
quantidade_lata = math.ceil(area/tinta)
preco_total = quantidade_lata*preco
print(quantidade_lata)
print("A quantidade que você vai ter que comprar é de: ", quantidade_lata)