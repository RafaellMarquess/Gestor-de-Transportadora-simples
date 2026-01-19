caminhoneiros = [
    {"nome": "Cesar", "caminhao": "A1", "localização": "Chile"},
    {"nome": "Marcos", "caminhao": "B2", "localização": "Brasil"},
    {"nome": "Joao", "caminhao": "C3", "localização": "Argentina"},
    {"nome": "Paulo", "caminhao": "D4", "localização": "Paraguai"},
    {"nome": "Rafael", "caminhao": "E5", "localização": "Uruguai"},
    {"nome": "Lucas", "caminhao": "F6", "localização": "Bolivia"},
    {"nome": "Andre", "caminhao": "G7", "localização": "Peru"},
    {"nome": "Bruno", "caminhao": "H8", "localização": "Colombia"},
    {"nome": "Diego", "caminhao": "I9", "localização": "Equador"},
    {"nome": "Felipe", "caminhao": "J10", "localização": "Venezuela"},
    {"nome": "Gustavo", "caminhao": "K11", "localização": "Brasil"},
    {"nome": "Henrique", "caminhao": "L12", "localização": "Chile"},
    {"nome": "Igor", "caminhao": "M13", "localização": "Argentina"},
    {"nome": "Julio", "caminhao": "N14", "localização": "Brasil"},
    {"nome": "Kevin", "caminhao": "O15", "localização": "Paraguai"},
    {"nome": "Leandro", "caminhao": "P16", "localização": "Uruguai"},
    {"nome": "Mateus", "caminhao": "Q17", "localização": "Bolivia"},
    {"nome": "Nathan", "caminhao": "R18", "localização": "Peru"},
    {"nome": "Otavio", "caminhao": "S19", "localização": "Colombia"},
    {"nome": "Pedro", "caminhao": "T20", "localização": "Brasil"},
    {"nome": "Renan", "caminhao": "U21", "localização": "Chile"},
    {"nome": "Samuel", "caminhao": "V22", "localização": "Argentina"},
    {"nome": "Tiago", "caminhao": "W23", "localização": "Brasil"},
    {"nome": "Victor", "caminhao": "X24", "localização": "Paraguai"},
    {"nome": "William", "caminhao": "Y25", "localização": "Uruguai"}
]

print("Seja Bem-Vindo gestor oque gostaria de fazer?")
print("\n1-Procurar caminhao \n2-Sair")

while True:
    resposta = input("")

    if resposta == "1":
        caminhao = input("Qual Caminhao deseja procurar?\n ").upper()
        encontrado = False

        for n in caminhoneiros:
            if caminhao == n["caminhao"]:
                print(f"Caminhao {n['caminhao']} está em {n['localização']}")
                print("\n1-Procurar caminhao \n2-Sair")
                encontrado = True
                break

        if not encontrado:
            print("Não encontrado")
            print("\n1-Procurar caminhao \n2-Sair")


    elif resposta == "2":
        break

    else:
        print("Erro na digitacao")