while True:
    numero = int(input("Informne um número: "))

    if numero == 10:
        continue #pular execução

    print(numero)


for numero in range(100):

    if numero == 10:
        break # curtar a execução

    print(numero, end=" ")
    