# Adicionar novo aluno no dicionário

cadastros = [
    {"nome": "Pedro", "idade": 20, "curso": "T.I"},
    {"nome": "André", "idade": 23, "curso": "Química"}
]

print("--- CADASTROS INICIAS ---")  
for aluno in cadastros:
    print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']}")

print("-"* 40)

novo_aluno = {
    "nome": "Lucas",
    "idade": 19,
    "curso": "Engenharia"
}

cadastros.append(novo_aluno)

cadastros.append({
    "nome": "Mariana",
    "idade": 21,
    "curso": "Medicina"
})

print("=== TABELA ATUALIZADA ===")
print(f"Total de registros na memória: {len(cadastros)}")

for i in range(len(cadastros)):
    registro = cadastros[i]
    print(f"Registro [{i}]: -> Nome: {registro['nome']}")