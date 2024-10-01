palavra = input("Digite uma palavra: ")
pala = palavra.lower().strip().replace('', '')
if(pala==pala[::-1]):
  print("é um polidromo")
else:
  print("não é um polidromo")