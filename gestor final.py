funcionarios = [
    {"nome": "Rafael", "cargo": "Desenvolvedor Frontend", "salario": 6000.0},
    {"nome": "Ana", "cargo": "Designer UX", "salario": 5200.0},
    {"nome": "Pedro", "cargo": "Gerente de TI", "salario": 8500.0},
    {"nome": "Maria", "cargo": "Desenvolvedora Frontend", "salario": 5800.0},
    {"nome": "Lucas", "cargo": "Estagiário", "salario": 1800.0},
    {"nome": "Carla", "cargo": "Analista de Dados", "salario": 6200.0},
    {"nome": "Bruno", "cargo": "Desenvolvedor Mobile", "salario": 5900.0},
    {"nome": "Beatriz", "cargo": "Product Owner", "salario": 7500.0},
    {"nome": "Ricardo", "cargo": "Suporte Técnico", "salario": 3200.0},
    {"nome": "Julia", "cargo": "Recursos Humanos", "salario": 4500.0}
]

print("\nEscolha sua ação:\n\n1- Adicionar Funcionario\n2- Excluir Funcionario\n3- Listar funcionarios\n4- Sair")
while True:
    resposta = input("")
    if resposta == "1":
            novo_nome = input("Nome do funcionario:")
            novo_cargo = input("Cargo do funcionario:")
            novo_salario = float(input("Salario do funcionario:"))

            lista = {
                "nome":novo_nome,
                "cargo":novo_cargo,
                "salario":novo_salario,
            } 
            funcionarios.append(lista)
            print(f"{novo_nome} adicionado com sucesso!")
    
    if resposta == "2":
             for i, n in enumerate(funcionarios):
                  print(f"{i}:{n['nome']}")

             indice = int(input("Digite o número: "))

             apagar = funcionarios.pop(indice)

             print(f"{n['nome']} foi apagado com sucesso!")

    if resposta == "3":
        for n in funcionarios:
            print(f"Nome: {n['nome']} | Cargo: {n['cargo']} | Salário: R$ {n['salario']:.2f}")

    if resposta == "4":
        print("saindo...")
        exit()