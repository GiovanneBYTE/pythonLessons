with open("teste.txt", "rb") as arquivo:
    conteudo = arquivo.read()
print("tipo de dado da variavel", type(conteudo))
print("conteudo do arquivo: ", conteudo)