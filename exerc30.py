num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
sinal = str(input("Digite o sinal que voçê quer: "))
if (sinal == "+"):
  resultado = num1+num2
  print("O seu resultado é",resultado)
elif (sinal == "-"):
  resultado = num1-num2
  print("O seu resultado é",resultado)
elif (sinal == "*"):
  resultado = num1*num2
  print("O seu resultado é",resultado)
elif (sinal == "/"):
  resultado = num1/num2
  print("O seu resultado é",resultado)
else:
  print("sinal inválido")