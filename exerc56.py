ext = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']
dezenas = ["zero", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
num = int(input("Digite um número: "))
if num >= 0 and num <= 100:
  if num < 21:
    print(f"{ext[num]}")
  else:
    x = divmod(num, 10)
    if (x[1] == 0):
      print(dezenas[x[0]])
    else:
      print(f"{dezenas[x[0]]} e {ext[x[1]]}")
else:
  print("Tente novamente!")