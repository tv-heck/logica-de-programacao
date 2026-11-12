acervo = [
    {"codigo": 101, "titulo": "Quarta Asa", "autor": "Rebecca Yarros", "paginas": 400, "disponivel": True},
    {"codigo": 104, "titulo": "Corte de Espinhos e Rosas", "autor": "Sarah J. Maas", "paginas": 464, "disponivel": True},
    {"codigo": 203, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkein", "paginas": 1200, "disponivel": True},
    {"codigo": 501, "titulo": "Épico de Gilgamesh", "autor": "Desconhecido/Tradição Oral", "paginas": 300, "disponivel": False},
]

novo_livro = {
    "codigo": 502,
    "titulo": "Odisseia",
    "autor": "Homero",
    "paginas": 400,
    "disponivel": True
}

acervo.append(novo_livro)

for livro in acervo:
    if livro["disponivel"] == True and livro["paginas"] > 250:
        print(f"Código: {livro['codigo']} | Título: {livro['titulo']} | Autor: {livro['autor']} | Páginas: {livro['paginas']} | Disponível: {livro['disponivel']}")


flag = False

for livro in acervo:
    if livro["codigo"] == 104:
        flag = True
        break

if flag:
    print(f"Livro encontrado! É o {livro['titulo']} do autor {livro['autor']}.")
else:
    print("O livro de código 104 não foi encontrado.")


emprestimo = input("Deseja realizar um empréstimo? (S/N): ").strip().upper()

if emprestimo == "S":
    codigo_emprestimo = int(input("Digite o código do livro que deseja emprestar: "))

    for livro in acervo:
        if livro["codigo"] == codigo_emprestimo:
            if livro["disponivel"]:
                livro["disponivel"] = False
                print(f"Empréstimo realizado! O livro {livro['titulo']} agora está indisponível.")
            else:
                print(f"O livro {livro['titulo']} existe no acervo, mas não está disponível.")
            break
    else:
        print("Esse código não existe no acervo.")
else:
    print("Obrigado por utilizar o sistema e até a próxima!")