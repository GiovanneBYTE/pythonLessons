with open("index.html", "w") as pagina:
    pagina.write("<body> <h1> Está é um teste para uma pagina WEB </h1>")
    pagina.write("<br> <h2> Abaixo seguem alguns nomes importantes para o projeto: </h2>")
    pagina.write("<h3>")
    nome = ""
    while nome != "SAIR":
        nome = input("Digite um nome ou Sair: ").upper()
        if nome != "SAIR":
            pagina.write("<br>" + nome)
    pagina.write("</h3> </body>")