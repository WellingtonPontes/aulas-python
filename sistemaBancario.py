#criar sistema bancarios

# operações: sacar , deposito, visualziar extrato

#deposito posso depositar qualquer quantia positiva
#primeiro não vai ter distições de contas
#guarda todo o valor em uma variaval e exibir na operação 

#operação de saques , sistema deve permitir 3 saques diarios 
#o maximo entre sques de 500 por saque
#se não tiver saldo informa uma mensagem 

#todos os saques devem ser armazeanados e exibidos no extrato 

#formato ixibido de dinhero xxx.xx = 1500.45  = r$ 1500.45


menu =  """

[d] DEPOSITO
[S] SACAR
[e] EXTRATO
[q] SAIR

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

# LIMITE_SAQUE CONSTANT 

while True:
    opcao = input(menu)
    print(opcao)
    
    if opcao == "d":
        deposito = int(input("Quanto deseja depositar? "))
        if deposito <= 0:
            print("valor invalido!")
        else:
            saldo += deposito
            extrato += f"Deposito: R${deposito:.2f}\n"
    elif opcao == "s":
        saque = int(input("Quanto deseja sacar? "))
        if saque <= 0 or saque >= 501:
            print("valor invalido!")
        elif numero_saque == LIMITE_SAQUE:
            print("Limites de saque disponivel esgotado")
        elif saque > saldo:
            print("valor invalido!")
        else:
            saldo -= saque
            extrato += f"Saque: R${saque:.2f}\n"
            numero_saque += 1
    elif opcao == "e":
        print("\n##############################################".center(50))
        print("EXTRATO".center(50))
        print(" Não foram realziados movimentações em sua conta." if not  extrato else extrato)
        print(f"\n Saldo:   R${saldo:.2f}")
        print("\n##############################################".center(50))
    elif opcao == "q":
        break
    else:
        print("\n##############################################".center(50))
        print("Digite uma opção valida")
