opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair: \n: "))

    if opcao == 1:
        print("Sacando...")

    elif opcao == 2:
        print("Exibindo o estrato...")

else:
    print("Obrigada por usar nosso sistema bancário, até logo!")