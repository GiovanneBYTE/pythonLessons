with open ("teste.txt", "w") as arquivo:
    arquivo.write("Criando um arquivo")

with open("teste.txt", "a") as arquivo:
    arquivo.write("continuação")

