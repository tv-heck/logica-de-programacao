# Acervo inicial

acervo_biblioteca = [
    {"titulo": "Duna", "autor": "Frank Herbert", "ano": 1965, "disponivel": True},
    {"titulo": "O Alquimista", "autor": "Paulo Coelho", "ano": 1988, "disponivel": True},
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "disponivel": False},
]


# Funções do sistema

# Função para cadastrar um novo livro no acervo
def cadastrar(lista):
    # Solicita o título, autor e ano de publicação do livro ao usuário
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    ano_texto = input("Ano de publicação: ").strip()

    # Validação de entrada para cadastrar um livro
    if not titulo.isalnum() or not autor.isalnum() or not ano_texto.isdigit():
        print("Erro: título, autor ou ano inválido.")
        return

    if ano_texto > "2026":
        print("Erro: ano de publicação inválido.")
        return

    if titulo == "" or autor == "" or ano_texto == "":
        print("Erro: algum campo está nulo.")
        return

    # Adiciona o livro através do append com disponibilidade como verdadeira
    lista.append({
        "titulo": titulo,
        "autor": autor,
        "ano": int(ano_texto),
        "disponivel": True,
    })
    print(f'Livro "{titulo}" cadastrado com sucesso.')

# Exibe o menu principal do sistema e retorna a opção escolhida pelo usuário
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

    # Lista os livros cadastrados com suas informações
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

# Função para buscar e exibir um livro pelo título
def buscar_e_exibir(lista):
    if not lista:
        print("Não há livros cadastrados para buscar.")
        return

    titulo = input("Digite o título do livro: ").strip()

    if titulo == "" or not titulo.isalnum():
        print("Título inválido: digite um título.")
        return
    
    # Pelo título do livro, buscar o índice correspondente na lista
    indice = buscar(lista, titulo)

    if indice == -1:
        print("Livro não encontrado.")
        return

    # Exibir os detalhes do livro encontrado
    livro = lista[indice]
    disponibilidade = "Sim" if livro["disponivel"] else "Não"
    print(
        f'Título: {livro["titulo"]} | '
        f'Autor: {livro["autor"]} | '
        f'Ano: {livro["ano"]} | '
        f'Disponível: {disponibilidade}'
    )

# Função para remover um livro do acervo
def remover(lista):
    if not lista:
        print("Não há livros cadastrados para remover.")
        return

    # Pelo título do livro, buscar o índice correspondente na lista
    titulo = input("Digite o título do livro que deseja remover: ").strip()
    indice = buscar(lista, titulo)

    # Validação de entrada para remover um livro
    if titulo == "" or not titulo.isalpha():
        print("Título inválido: digite um título.")
        return

    if indice == -1:
        print("Livro não encontrado.")
        return

    # Livro é removido por índice para evitar problemas com títulos duplicados
    livro_removido = lista.pop(indice)
    print(f'Livro "{livro_removido["titulo"]}" removido com sucesso.')



# Loop principal do sistema

loop = True
while loop:
    # Solicitar ao usuário se deseja inicializar o sistema
    inicializar_sistema = input("Deseja inicializar o sistema? (s/n): ").strip().lower()

    if inicializar_sistema == "s":
        # Exibir o menu e processar a opção escolhida
        opcao = exibir_menu()

        if opcao not in ["1", "2", "3", "4", "5"]:
            print("Opção inválida. Tente novamente.")
            continue

        # Resultado das opções do menu
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
# Validação de entrada para inicializar o sistema
else: 
    print("Opção inválida. Tente novamente.")
    inicializar_sistema = input("Deseja inicializar o sistema? (s/n): ").strip().lower()

