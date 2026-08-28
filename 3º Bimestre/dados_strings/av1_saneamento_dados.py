# ==============================================================================
# PROVA PRÁTICA AV1 - 3º BIMESTRE
# ARQUIVO: av1_saneamento_dados.py
# Nome do Aluno: Thiago Viel Heck
# Data: 28/08/2026
# ==============================================================================

# Lista de cadastros brutos recebidos do sistema
cadastros_brutos = [
   "  joao da silva;11988887777  ",
   "  maria sousa;21977776666  ",
   "  carlos edgardo oliveira;31966665555  ",
   "  ana paula lima;41955554444  "
]

cadastro_limpo = []

print("==================================================")
print("     SISTEMA DE SANEAMENTO DE DADOS - AV1         ")
print("==================================================\n")

for i in range (len(cadastros_brutos)):
   
    cadastro_limpo = cadastros_brutos[i].strip()
    partes = cadastros_brutos[i].split(";")
    nome = partes[0].strip().upper()
    ddd = partes[1].strip()[:2]
    telefone = partes[1].strip()
   
    print(f"Funcionário: {nome} | DDD: {ddd} | Telefone: {telefone}")

print("\n==================================================")
print("             PROCESSAMENTO CONCLUÍDO              ")
print("==================================================")