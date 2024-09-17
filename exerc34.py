a = float(input("Digite sua altura: "))
sexo = str(input("Digite o seu sexo: "))
if sexo == 'm':
  resultado1 = (72.7*a) - 58
  print(f"Seu peso ideal é em média {resultado1}")
elif sexo == 'f':
  resultado2 = (62.1*a) - 44.7
  print(f"Seu peso ideal é em média {resultado2}")