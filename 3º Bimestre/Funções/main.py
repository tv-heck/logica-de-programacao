# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: Thiago Viel Heck
# Data: 18/09/2026
# Link do Repositório: https://github.com/tv-heck/logica-de-programacao
# ==============================================================================

# Lista inicial de dados brutos (Exemplo: Sistema de RH / Atendimento)
# Os dados estão no formato: "nome_completo;cargo_ou_setor;telefone_ou_cpf"
dados_brutos = [
   "  carlos eduardo silva;desenvolvedor;11988887777  ",
   "  ana paula mendes;analista de rh;21977776666  ",
   "  roberto carlos oliveira;gerente de projetos;31966665555  ",
   "  pedro henrique da silva;diretor de operações;11955542222  ",
   "  joão g. silva;estagiário;4899924444  ",
   "  luca b. santos;auditor;11988883333  "
]


# ------------------------------------------------------------------------------
# 1. FUNÇÕES DO SISTEMA (Mínimo de 3 funções)
# ------------------------------------------------------------------------------

def limpar_e_formatar_texto(texto):
   """
   FUNÇÃO 1:
   - Deve receber uma string.
   - Deve remover espaços extras das pontas (.strip()).
   - Deve converter o texto para letras MAIÚSCULAS (.upper()).
   - Retorna o texto devidamente formatado.
   """
   texto = texto.strip().upper()
   return texto


def extrair_codigo_ou_ddd(dado):
   dado = dado.strip()
   return dado[0:2]


def processar_e_exibir_cadastros(lista_dados):
   total = 0
   for dado in lista_dados:
      partes = dado.split(";")
      nome = limpar_e_formatar_texto(partes[0])
      cargo = limpar_e_formatar_texto(partes[1])
      ddd = extrair_codigo_ou_ddd(partes[2])
      print(f"Nome: {nome}, Cargo: {cargo}, DDD: {ddd}")
      total += 1
   return total


# ------------------------------------------------------------------------------
# 2. PROGRAMA PRINCIPAL (FLUXO DE EXECUÇÃO)
# ------------------------------------------------------------------------------

def main():
   print("==================================================")
   print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
   print("==================================================\n")

   print("Iniciando o processamento dos dados...\n")
   total_processado = processar_e_exibir_cadastros(dados_brutos)
   # TODO: Exiba uma mensagem final mostrando a quantidade total de registros processados.

   print(f"\nTotal de registros processados: {total_processado}")

   print("\n==================================================")
   print("             PROCESSAMENTO CONCLUÍDO              ")
   print("==================================================")


# Execução do programa
if __name__ == "__main__":
   main()