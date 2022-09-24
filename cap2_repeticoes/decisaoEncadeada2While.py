
#FIAP Ver.
resposta="SIM"
while resposta == "SIM":
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()

    while doenca_infectocontagiosa!="SIM" and  doenca_infectocontagiosa!="NAO" :
        print("Digite SIM ou NAO")
        doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para sala AMARELA")
    else:
        print("Encaminhe o paciente para sala BRANCA")
    if idade >= 65:
        print("Paciente com prioridade")
    else:
        genero=input("Digite o genero do paciente: ").upper()

        if genero == "FEMININO" and idade >= 10:
            gravidez=input("A paciente está gravida? ").upper()
            if gravidez == "SIM":
                print("Paciente com prioridade. ")
            else:
                print("Paciente sem prioridade.")
        else:
            print("Paciente sem prioridade. ")

    reposta=input("Digite SIM para continuar: ").upper()


