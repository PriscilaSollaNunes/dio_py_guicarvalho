nome = "Priscila"
idade = 41
profissão = "Progamadora"
linguagem = "Python"
saldo = 45.350

dados = {"nome": "Guilherme", "idade": 28}

print("Nome: %s Idade: %d" % (nome,idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {0} Idade: {1}".format(nome, idade))
print("Nome: {0} Idade: {1} Nome: {0} {0}".format(nome, idade))
print("Nome: {nome} Idade: {idade} Nome: {nome} {nome}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} Nome: {name} Nome: {name}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")