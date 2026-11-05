turma = [
    {"nome": "Ana", "idade": 16, "nota": 8.5},
    {"nome": "Bruno", "idade": 17, "nota": 7.0},
    {"nome": "Carla", "idade": 16, "nota": 9.5},
]

print(turma[0]["nome"])
print(turma[2]["nota"])

print("--- RELATÓRIO DA TURMA ---")

for aluno in turma:
    print(f"Nome: {aluno['nome']} | Nota: {aluno['nota']}")

# Atividade 1 - Lista de dicionários

produtos = [
    {"produto": "PS5 Pro", "preco": 4399.99, "em_estoque": False},
    {"produto": "RTX 4090", "preco": 14999.99, "em_estoque": True},
    {"produto": "iPhone 18 Pro Max", "preco": 7999.99, "em_estoque": True}
]

for produto in produtos:
    print(f"Produto: {produto['produto']} | Preço: R$ {produto['preco']}")