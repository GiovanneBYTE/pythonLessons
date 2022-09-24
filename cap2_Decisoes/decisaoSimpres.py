nome=input("Digite um nome: ")
idade=int(input("Digite a idade: "))
prioridade="Não"

if idade >= 65:
    prioridade="Sim"
print("O paciente " + nome + " possui atedimento prioritario? " + prioridade)

