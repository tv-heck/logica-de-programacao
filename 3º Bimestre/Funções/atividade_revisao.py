# Atividade 1 - A variável invisível
def criar_usuario():
   nome_usuario = "Dev_Python"
   nivel_acesso = "Admin"
   return nome_usuario, nivel_acesso # Funciona por causa de return que retorna os valores das variáveis 

# Tentativa de acesso fora da função
print("--- FORA DA FUNÇÃO ---")
print(criar_usuario()) # Essa é a forma correta de chamar a função e exibir o resultado, pois ela retorna os valores das variáveis.

# Atividade 3 - Erro de memória
def funcao_infinita(contador):
   print(f"Chamada número: {contador}")
   # ERRO: Não existe 'if' para parar!
   funcao_infinita(contador + 1)

funcao_infinita(1)