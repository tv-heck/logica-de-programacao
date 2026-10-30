# Atividade 1 - Cadastro de Produto

produto = {
    "codigo": 101,
    "nome": "Teclado Mecânico Gamer",
    "preco": 250.0,
    "estoque": 14
}

print("=== Produto cadastrado ===")
print(produto)
print(f"Código: {produto['codigo']}")
print(f"Nome: {produto['nome']}")
print(f"Preço: R$ {produto['preco']:.2f}")
print(f"Estoque: {produto['estoque']}")

# Atividade 2 - Atualização de Produto

produto["preco"] = 220.0
produto["categoria"] = "Periféricos"

print("=== Produto atualizado ===")
print(produto)
print(f"Categoria: {produto['categoria']}")
print(f"Código: {produto['codigo']}")
print(f"Nome: {produto['nome']}")

# Atividade 3 - Perfil de Usuário e Métodos de Inspeção

usuario = {
    "nome": "Carlos Eduardo",
    "nivel": "Administrador",
    "ativo": True
}

print("=== Perfil do Usuário ===")
print(f"Nome: {usuario['nome']}")
print(f"Nível: {usuario['nivel']}")
print(f"Ativo: {usuario['ativo']}")