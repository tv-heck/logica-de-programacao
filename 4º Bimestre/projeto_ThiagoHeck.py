acervo_biblioteca = [
    {"titulo": "Duna", "autor": "Frank Herbert", "ano": 1965, "disponivel": True},
    {"titulo": "O Alquimista", "autor": "Paulo Coelho", "ano": 1988, "disponivel": True},
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "disponivel": False},
                     ]

inicializar_sistema = input("Deseja inicializar o sistema? (S/N): ").strip().upper()

while inicializar_sistema == "S":
    print("\n Bem vindo ao sistema da biblioteca! \n")
    print("1. Listar livros disponíveis")
    print("2. Cadastrar novo livro")
    print("3. Buscar livro por título")
    print("4. Realizar empréstimo de livro")
    print("5. Transferir livro para outro acervo")
    print("6. Sair do sistema")

opcao = input("Escolha uma opção (1-6): ").strip()