# Desafio de laços usando strings


# Atividade 1 - Extração de DDD e número de telefone


telefone = input("Digite o telefone no formato (XX)XXXXX-XXXX:")


extração_DDD = telefone[1:3]
extração_numero = telefone[4:]


print(f"DDD: {extração_DDD}")
print(f"Número: {extração_numero}")


# Atividade 2 - Formatador de Data de Nascimento


data_nascimento = input("Insere a sua data de nascimento: ")


dia = data_nascimento[0:2]
mes = data_nascimento[3:5]
ano = data_nascimento[6:]


print(f"Dia:", dia)
print(f"Mês:", mes)
print(f"Ano:", ano)


# Atividade 3 - Criador de Nome de Usuário


email_instituição = input("Inserir o email do aluno da instuitição acadêmica (formato: nome.sobrenome@escola.com): ")


primeiro_nome = email_instituição[0:email_instituição.index(".")]
dominio_email = email_instituição[email_instituição.index("@") + 1:email_instituição.index(".com")]


print(f"Nome de usuário: {primeiro_nome}.{dominio_email}")


