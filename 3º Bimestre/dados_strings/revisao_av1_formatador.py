# Atividade 1 - Formatação de citação

def formatar_citacao(nome_completo):
     partes = nome_completo.strip().split()
     sobrenome = partes[-1].upper()
     primeiro_nome = " ".join(partes[:-1])
     return sobrenome + ", " + primeiro_nome

# Atividade 2 - Gerador de código de aluno

def gerar_codigo(ano, cpf):
     cpf_limpo = cpf.strip()
     tres_digitos = cpf_limpo[0:3]
     return "ALU-" + str(ano) + "-" + tres_digitos


# Testes de fluxo

# Teste 1 - Citação Bibliográfica

autor = "Luca Bendô dos Santos"

citacao_formatada = formatar_citacao(autor)
print("Citação bibliográfica:", citacao_formatada)  # Saída esperada: "DOS SANTOS, Luca Bendô"

# Teste 2 - Geração de código de aluno
ano_matricula = 2024
cpf_aluno = "123.456.789-00"
codigo_gerado = gerar_codigo(ano_matricula, cpf_aluno)
print("Matrícula gerada:", codigo_gerado)  # Saída esperada: "ALU-2024-123" 