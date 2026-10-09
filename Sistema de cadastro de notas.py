cadastros = []


def cadastrar():
    print("\n--- CADASTRO DE ALUNO ---")

    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media,
        "situacao": situacao
    }

    cadastros.append(aluno)

    print("\nAluno cadastrado com sucesso!")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")


def listar():
    print("\n--- LISTA DE ALUNOS ---")

    if len(cadastros) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for i, aluno in enumerate(cadastros, start=1):
            print(f"\nAluno {i}")
            print(f"Nome: {aluno['nome']}")
            print(f"Nota 1: {aluno['nota1']:.2f}")
            print(f"Nota 2: {aluno['nota2']:.2f}")
            print(f"Nota 3: {aluno['nota3']:.2f}")
            print(f"Média: {aluno['media']:.2f}")
            print(f"Situação: {aluno['situacao']}")


def estatisticas():
    print("\n--- ESTATÍSTICAS DA TURMA ---")

    if len(cadastros) == 0:
        print("Não existem alunos cadastrados.")
        return

    total = len(cadastros)

    soma_medias = 0

    for aluno in cadastros:
        soma_medias += aluno["media"]

    media_geral = soma_medias / total

    maior_media = max(cadastros, key=lambda aluno: aluno["media"])
    menor_media = min(cadastros, key=lambda aluno: aluno["media"])

    print(f"Total de alunos: {total}")
    print(f"Média geral da turma: {media_geral:.2f}")
    print(f"Maior média: {maior_media['media']:.2f}")
    print(f"Aluno com maior média: {maior_media['nome']}")
    print(f"Menor média: {menor_media['media']:.2f}")


while True:

    print("\n==================================")
    print("SISTEMA DE CONTROLE DE NOTAS")
    print("==================================")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Exibir estatísticas")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()

    elif opcao == "2":
        listar()

    elif opcao == "3":
        estatisticas()

    elif opcao == "4":
        print("\nSistema encerrado!")
        break

    else:
        print("\nOpção inválida!")