# Atividade 1 - Cadastro de Produto

produto = {
    "codigo": 101,
    "nome": "Teclado Mecânico Gamer",
    "preco": 250.0,
    "estoque": 14
}

# Atividade 2 - Atualização de Produto

produto["preco"] = 220.0
produto["categoria"] = "Periféricos"

print("Produto atualizado:", produto)

# Atividade 3 - Perfil de Usuário e Métodos de Inspeção

usuario = {
    "nome": "Carlos Eduardo",
    "nivel": "Administrador",
    "ativo": True
}

print("Chaves do usuário:", usuario.keys())
print("Dados do usuário:", usuario.values())