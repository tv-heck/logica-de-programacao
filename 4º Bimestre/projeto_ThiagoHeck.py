acervo_biblioteca = [
    {"titulo": "Duna", "autor": "Frank Herbert", "ano": 1965, "disponivel": True},
    {"titulo": "O Alquimista", "autor": "Paulo Coelho", "ano": 1988, "disponivel": True},
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "disponivel": False},
]



def cadastrar(lista):
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    ano_texto = input("Ano de publicação: ").strip()

    if not titulo or not autor or not ano_texto:
        print("Todos os campos são obrigatórios.")
        return

    if not ano_texto.isdigit():
        print("Ano inválido: digite um número.")
        return

    lista.append({
        "titulo": titulo,
        "autor": autor,
        "ano": int(ano_texto),
        "disponivel": True,
    })
    print(f'Livro "{titulo}" cadastrado com sucesso.')


def exibir_menu():
    print("\n=== Sistema da Biblioteca ===")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Buscar livro por título")
    print("4. Remover livro")
    print("5. Sair")
    return input("Escolha uma opção (1-5): ").strip()


def listar(lista):
    if not lista:
        print("Não há livros cadastrados.")
        return

    print("\nLivros cadastrados:")
    for livro in lista:
        disponibilidade = "Sim" if livro["disponivel"] else "Não"
        print(
            f'Título: {livro["titulo"]} | '
            f'Autor: {livro["autor"]} | '
            f'Ano: {livro["ano"]} | '
            f'Disponível: {disponibilidade}'
        )


def buscar(lista, titulo):
    for indice, livro in enumerate(lista):
        if livro["titulo"].lower() == titulo.lower():
            return indice
    return -1


def buscar_e_exibir(lista):
    if not lista:
        print("Não há livros cadastrados para buscar.")
        return

    titulo = input("Digite o título do livro: ").strip()

    if titulo == "":
        print("Título inválido: digite um título.")
        return

    indice = buscar(lista, titulo)

    if indice == -1:
        print("Livro não encontrado.")
        return

    livro = lista[indice]
    disponibilidade = "Sim" if livro["disponivel"] else "Não"
    print(
        f'Título: {livro["titulo"]} | '
        f'Autor: {livro["autor"]} | '
        f'Ano: {livro["ano"]} | '
        f'Disponível: {disponibilidade}'
    )


def remover(lista):
    if not lista:
        print("Não há livros cadastrados para remover.")
        return

    titulo = input("Digite o título do livro que deseja remover: ").strip()
    indice = buscar(lista, titulo)

    if indice == -1:
        print("Livro não encontrado.")
        return

    livro_removido = lista.pop(indice)
    print(f'Livro "{livro_removido["titulo"]}" removido com sucesso.')


inicializar_sistema = input("Deseja inicializar o sistema? (s/n): ").strip().lower()

if inicializar_sistema == "s":
    while True:
        opcao = exibir_menu()

        if opcao not in ["1", "2", "3", "4", "5"]:
            print("Opção inválida. Tente novamente.")
            continue

        if opcao == "1":
            cadastrar(acervo_biblioteca)
        elif opcao == "2":
            listar(acervo_biblioteca)
        elif opcao == "3":
            buscar_e_exibir(acervo_biblioteca)
        elif opcao == "4":
            remover(acervo_biblioteca)
        elif opcao == "5":
            print("Saindo do sistema. Até logo!")
            break
elif inicializar_sistema == "n":
    print("Sistema não inicializado. Encerrando o programa.")
    exit()

else: 
    print("Opção inválida. Tente novamente.")
    inicializar_sistema = input("Deseja inicializar o sistema? (s/n): ").strip().lower()

