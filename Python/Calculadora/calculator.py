n1 = input('Escolha um número! ')
while n1.isnumeric() == False:
  n1 = input('Isso são é um número! Escolha novamente! ')

n2 = input('Escolha outro! ')
while n2.isnumeric() == False:
  n2 = input('Isso são é um número! Escolha novamente! ')

tipo = input('Deseja fazer, Soma, Subtração, Divisão ou Multiplicação? ')
while tipo not in ["Soma", "Subtração", "Divisão", "Multiplicação"]:
  tipo = input('Não entendi. Utilize apenas as chaves: Soma, Subtração, Divisão ou Multiplicação. ')

if tipo == "Soma":
    resultado = float(n1) + float(n2)
    print(resultado)
elif tipo == "Subtração":
    if n1 < n2:
      resultado = float(n2) - float(n1)
    else:
      resultado = float(n1) - float(n2)
    
    print(resultado)
elif tipo == "Divisão":
    resultado = float(n1) / float(n2)
    print(resultado)
elif tipo == "Multiplicação":
    resultado = float(n1) * float(n2)
    print(resultado)
else:
    print('Não entendi o que você quis dizer.')