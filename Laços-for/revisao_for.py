# -- ATIVIDADE DE REVISÃO DE LAÇOS FOR --
# Respostas das questões:
#   1. Resultado: 6
#  2.  A falta do passo -1.



# Resposta da número 3:
gols = 0

partidas_sem_gols = 0

for i in range(1, 6):

    gols_partida = int(input(f"Digite o número de gols do jogador na partida {i}: "))

    gols += gols_partida

    if gols_partida == 0:

        partidas_sem_gols += 1

    media = gols / i

print("--- RELATÓRIO DE PERFORMANCE ---")

print(f"Total de gols marcados: {gols}")

print(f"Média de gols por partida: {media}")
print(f"Partidas sem gols: {partidas_sem_gols}")