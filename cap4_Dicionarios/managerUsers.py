from cap4_Dicionarios.funcoes import *
usuarios = {}

opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    if opcao == "P":
        pesquisar(usuarios, input("Qual o login que deseja pesquisar? "))
    if opcao == "E":
        excluir(usuarios, input("Qual usuario deseja excluir? "))
    if opcao == "L":
        listar(usuarios)

    opcao = perguntar()