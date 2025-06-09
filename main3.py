def calcular_tempo_total(matriz, treino_semanal):
    total = 0
    for dia_idx, treino_idx in enumerate(treino_semanal):
        total += matriz[treino_idx][dia_idx]
    return total

def treino_mais_longo(tipos_treino, matriz, treino_semanal):
    soma_por_treino = [0] * 10
    for dia_idx, treino_idx in enumerate(treino_semanal):
        soma_por_treino[treino_idx] += matriz[treino_idx][dia_idx]
    indice_mais_longo = soma_por_treino.index(max(soma_por_treino))
    return tipos_treino[indice_mais_longo], soma_por_treino[indice_mais_longo]

# Lista de grupos musculares
tiposTreino = [
    "Peitoral", "Dorsal", "Deltoides", "Bíceps", "Tríceps",
    "Abdômen", "Glúteos", "Quadríceps", "Isquiotibiais", "Panturrilhas"
]

# Matriz 10x10 de tempos fixos (linha = treino, coluna = dia)
matriz_tempos = [
    [40, 35, 30, 45, 50, 0, 0, 0, 0, 0],  # Peitoral
    [30, 40, 35, 30, 45, 0, 0, 0, 0, 0],  # Dorsal
    [25, 20, 30, 35, 30, 0, 0, 0, 0, 0],  # Deltoides
    [20, 25, 20, 25, 30, 0, 0, 0, 0, 0],  # Bíceps
    [30, 30, 25, 30, 35, 0, 0, 0, 0, 0],  # Tríceps
    [15, 20, 15, 20, 25, 0, 0, 0, 0, 0],  # Abdômen
    [40, 45, 50, 40, 50, 0, 0, 0, 0, 0],  # Glúteos
    [35, 30, 40, 45, 35, 0, 0, 0, 0, 0],  # Quadríceps
    [25, 30, 25, 30, 30, 0, 0, 0, 0, 0],  # Isquiotibiais
    [20, 25, 30, 25, 20, 0, 0, 0, 0, 0]   # Panturrilhas
]

# Entrada de dados do aluno
nome = input("Digite o nome do aluno: ")
matricula = int(input("Digite a matrícula do aluno: "))
mensalidade = float(input("Digite o valor da mensalidade: "))

# Montar treino semanal (segunda a sexta)
print("\nMonte o treino da semana (segunda a sexta):")
print("Escolha o número correspondente ao grupo muscular:")
for i, treino in enumerate(tiposTreino, 1):
    print(f"{i}. {treino}")

treino_semanal = []
for dia in ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]:
    escolha_valida = False
    while not escolha_valida:
        entrada = input(f"{dia}-feira (1 a 10): ")
        if entrada.isdigit():
            escolha = int(entrada)
            if 1 <= escolha <= 10:
                treino_semanal.append(escolha - 1)
                escolha_valida = True
            else:
                print("Escolha um número entre 1 e 10.")
        else:
            print("Digite apenas números.")


# Mostrar treino semanal com os tempos
print("\nTreino da semana:")
dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
for dia_idx, treino_idx in enumerate(treino_semanal):
    tempo = matriz_tempos[treino_idx][dia_idx]
    print(f"{dias_semana[dia_idx]} - {tiposTreino[treino_idx]}: {tempo} minutos")

# Menu de operações
while True:
    print("\nMENU")
    print("1. Calcular tempo total de treinos na semana")
    print("2. Identificar o grupo muscular com mais tempo acumulado")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        total = calcular_tempo_total(matriz_tempos, treino_semanal)
        print(f"Tempo total de treinos na semana: {total} minutos")
    elif opcao == "2":
        treino, tempo = treino_mais_longo(tiposTreino, matriz_tempos, treino_semanal)
        print(f"O grupo muscular mais treinado foi '{treino}' com {tempo} minutos.")
    elif opcao == "3":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
