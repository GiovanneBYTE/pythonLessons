ips={}
resp="S"
while resp=="S":
    ips[(input("Digite os dois primeiros octetos: "),
         input("Digite os dois ultimos octetos: "))] = input("Nome da maquina: ")
    resp=input("Digite <S> para continuar: ").upper()

print("Exibindo ip's: ")
for ip in ips.keys():
    print(ip[0]+"."+ip[1])

print("Exibindo maquinas com o mesmo endereço: ")
pes=input("digite os dois ultimos octetos: ")
for ip,nome in ip.items():
    print("Mauqinas no mesmo endereço (redes diferentes)")
    if(ip[1]==pes):
        print(nome)
print("Exibindo as máquinas que compõem uma mesma rede: ")
rede=input("Digite os dois primeiros octetos: ")
for ip,nome in ips.items():
    if(ip[0]==rede):
        print(nome)