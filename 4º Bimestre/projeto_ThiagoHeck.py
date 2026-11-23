acervo_biblioteca = [
    {"titulo": "Duna", "autor": "Frank Herbert", "ano": 1965, "disponivel": True},
    {"titulo": "O Alquimista", "autor": "Paulo Coelho", "ano": 1988, "disponivel": True},
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "disponivel": False},
                     ]

inicializar_sistema = input("Deseja inicializar o sistema? (S/N): ").strip().upper()

if inicializar_sistema == "S":
    print("\n Bem vindo ao sistema da biblioteca! \n")
    print("1. Listar livros disponíveis")
    print("2. Cadastrar novo livro")
    print("3. Buscar livro por título")
    print("4. Realizar empréstimo de livro")
    print("5. Transferir livro para outro acervo")
    print("6. Sair do sistema")

opcao = input("Escolha uma opção (1-6): ").strip()
if opcao == "1":
    print("\n Livros disponíveis: \n")
    for livro in acervo_biblioteca:
        if livro["disponivel"]:
            print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]}, Ano: {livro["ano"]}')

elif opcao == "2":
    titulo = input("Digite o título do livro: ").strip()
    autor = input("Digite o autor do livro: ").strip()
    ano = int(input("Digite o ano de publicação do livro: ").strip())
    novo_livro = {"titulo": titulo, "autor": autor, "ano": ano, "disponivel": True}
    acervo_biblioteca.append(novo_livro)
    print(f'\n Livro "{titulo}" cadastrado com sucesso! \n')

elif opcao == "3":
    titulo_busca = input("Digite o título do livro que deseja buscar:" ).strip()
    encontrado = False
    for livro in acervo_biblioteca:
        if livro["titulo"].lower() == titulo_busca.lower():
            print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]}, Ano: {livro["ano"]}')
            encontrado = True
        elif type(livro["titulo"]) is not str:
            print(f'\n ERRO: O título do livro deve ser texto! \n')
            encontrado = False
    if not encontrado:
        print(f'\n Livro "{titulo_busca}" não encontrado! \n')

elif opcao == "4":
    titulo_emprestimo = input("Digite o título do livro que deseja emprestar: ").strip()
    for livro in acervo_biblioteca:
        if livro["titulo"].lower() == titulo_emprestimo.lower():
            if livro["disponivel"]:
                livro["disponivel"] = False
                print(f'\n Empréstimo do livro "{titulo_emprestimo}" realizado com sucesso! \n')
            else:
                print(f'\n O livro "{titulo_emprestimo}" não está disponível para empréstimo. \n')
            break
    else:
        print(f'\n Livro "{titulo_emprestimo}" não encontrado! \n')
elif opcao == "5":

    titulo_transferencia = input("Digite o título do livro que deseja transferir: ").strip()
    for livro in acervo_biblioteca:
        if livro["titulo"].lower() == titulo_transferencia.lower():
            acervo_biblioteca.remove(livro)
            print(f'\n Livro "{titulo_transferencia}" transferido para outro acervo com sucesso! \n')
            break
    else:
        print(f'\n Livro "{titulo_transferencia}" não encontrado! \n')

elif opcao == "6":
    print("\n Saindo do sistema. Até logo! \n")
    
else:
    print("\n Opção inválida! Por favor, escolha uma opção entre 1 e 6. \n")
