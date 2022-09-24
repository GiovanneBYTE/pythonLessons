#Giovanne version
access=input("Digite seu tipo de acesso: ").upper()
gender=input("Digite seu genero: ").upper()

#laço adm
if access == "ADM" and gender == "MASCULINO":
    print("Olá administrador!")
elif access == "ADM" and gender == "FEMININO":
        print("Olá administradora")

#laço usr
elif access == "USR" and gender == "MASCULINO":
    print("Olá Usuario!")
elif access == "USR" and gender == "FEMININO":
     print("Olá usuaria!")

elif access == "Guest" and  gender == "FEMININO" or gender == "MASCULINO":
    print("Olá Visitante!")
else:
    print("Olá Desconhecido(a)")

#FIAP version
nivel=input("Digite o nível de acesso: ").upper()
if nivel=="ADM" or nivel=="USR":
    genero=input("Digite o seu gênero: ").upper()
    if nivel=="ADM":
        if genero=="FEMININO":
            print("Olá administradora")
        else:
            print("Olá administrador")
    else:
        if genero=="FEMININO":
            print("Olá usuária")
        else:
            print("Olá usuário")
elif nivel=="GUEST":
    print("Olá visitante")
else:
    print("Olá desconhecido(a)")