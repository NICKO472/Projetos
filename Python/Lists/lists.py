Compras = ["Arroz", "Feijão", "Suco", "Óleo", "Água", "Sofa", "Televisão"]
#print(Compras)

escolha = input("Qual a posição na lista do item que quer ver? ")
choose = Compras[int(escolha) - 1]
print(choose) # Escolhe algum item pela sua posição, Ex: 3 = Suco. Sem IF porque é um EXEMPLO.
add = input('\nDeseja adicionar algo na Lista? Y/N ')

while add not in ['Y', 'N']:
    add = input('Tente novamente!\nDeseja adicionar algo na Lista? Y/N ')

if add == "Y":
    new = input('Oque deseja adicionar? ')
    Compras.append(new)
    print(new, 'Adicionado à lista!\n', Compras)

elif add == "N":
    print('Entendido! Essa é sua Lista:\n', Compras)