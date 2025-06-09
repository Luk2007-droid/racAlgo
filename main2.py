# Tipos de treino fixos
tiposTreino = [
    ["Bíceps", 40],
    ["Perna", 60],
    ["Costas", 50],
    ["Ombro", 45],
    ["Peito", 55]
]

# Funções
def TreinoMaisLongoAluno(treinos):
    dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
    maxTempo = max(treinos)
    dia = dias[treinos.index(maxTempo)]
    return dia, maxTempo

def TempoTotalSemanaAluno(treinos):
    return sum(treinos)


def MostrarTiposTreino():
    print("\n=== TIPOS DE TREINO DISPONÍVEIS ===")
    for i, treino in enumerate(tiposTreino, start=1):
        print(f"{i} - {treino[0]} ({treino[1]} min)")

# Coleta de dados do aluno
print("=== PLANOS DE MENSALIDADE ===")
print("Básico: R$99.50 | Intermediário: R$150.00 | Avançado: R$200.00")

nomeInput = input("\nDigite o nome do aluno: ")
matriculaInput = int(input("Digite o número da matrícula: "))
mensalidadeInput = float(input("Digite o valor da mensalidade escolhida (apenas número): R$"))

# Escolher treino para cada dia
diasSemana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
treinosEscolhidos = []

print("\nAgora escolha o treino para cada dia da semana:")
MostrarTiposTreino()

for dia in diasSemana:
    while True:
        try:
            escolha = int(input(f"{dia}: Escolha o número do treino desejado: "))
            if 1 <= escolha <= len(tiposTreino):
                tempoTreino = tiposTreino[escolha - 1][1]
                treinosEscolhidos.append(tempoTreino)
                break
            else:
                print("Escolha inválida. Digite um número válido.")
        except:
            print("Digite um número válido.")

# Adiciona o aluno digitado
alunoManual = [
    int(matriculaInput),
    nomeInput,
    idadeInput,
    celularInput,
    mensalidadeInput
] + treinosEscolhidos

matrizAlunos = [alunoManual]

# MENU
while True:
    print("\n=== MENU ===")
    print("1 - Ver treino mais longo do aluno inserido")
    print("2 - Calcular tempo total semanal do aluno inserido")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        dia, tempo = TreinoMaisLongoAluno(alunoManual[5:10])
        print(f"Treino mais longo: {dia} com {tempo} minutos")
    elif opcao == '2':
        total = TempoTotalSemanaAluno(alunoManual[5:10])
        print(f"Tempo total da semana: {total} minutos")
    elif opcao == '0':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")