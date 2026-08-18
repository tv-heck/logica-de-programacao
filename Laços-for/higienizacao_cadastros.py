# Atividade 1 - Padronização de nome e e-mail

nome = " joão pedro da silva "
email = " JOAO.SILVA@ESCOLA.COM "

print(f"Nome oficial: {nome.strip().upper()}")
print(f"E-mail oficial: {email.lower().strip()}")

# Atividade 2 - Limpeza de Documentos

cpf = " 123.456.789-00 "
telefone = " (11) 99999-8888"

print(f"CPF padronizado: {cpf.strip().replace(".", "").replace("-", "").replace(" ", "")}")
print(f"Número de telefone padronizado: {telefone.strip().replace("(", "").replace(")", "").replace("-", "").replace(" ", "")}")

# Atividade 3 - Código de Estoque

código_entrada = " prod-1024-br-sp "

print(f"Código formatado: {código_entrada.strip().upper().replace("-", "_")}")