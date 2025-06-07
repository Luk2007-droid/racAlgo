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

def MostrarMatrizAlunos():
    print("\n=== MATRIZ DE ALUNOS ===")
    print("Matrícula | Nome     | Idade | Celular         | Mensalidade | Seg | Ter | Qua | Qui | Sex")
    for aluno in matrizAlunos:
        print(f"{aluno[0]:>9} | {aluno[1]:<8} | {aluno[2]:>5} | {aluno[3]:<15} | R${aluno[4]:>11} | "
              f"{aluno[5]:>3} | {aluno[6]:>3} | {aluno[7]:>3} | {aluno[8]:>3} | {aluno[9]:>3}")

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
idadeInput = int(input("Digite a idade do aluno: "))
celularInput = input("Digite o número de celular do aluno: ")

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

# Adiciona mais 9 alunos com dados fixos
matrizAlunos += [
    [1001, "Luís",     20, "(41) 91234-5678", 99.50, 40, 60, 50, 45, 55],
    [1002, "Bruna",   22, "(41) 91234-5679", 150.00, 60, 60, 60, 60, 60],
    [1003, "Carlos",  25, "(41) 91234-5680", 200.00, 50, 50, 50, 50, 50],
    [1004, "Diego",   21, "(41) 91234-5681", 150.00, 40, 40, 40, 40, 40],
    [1005, "Caio", 23, "(41) 91234-5682", 99.50, 45, 45, 45, 45, 45],
    [1006, "Flavia",19, "(41) 91234-5683", 200.00, 55, 55, 55, 55, 55],
    [1007, "Guilherme", 27, "(41) 91234-5684", 150.00, 60, 50, 40, 45, 55],
    [1008, "Leonardo",  24, "(41) 91234-5685", 99.50, 40, 60, 40, 60, 40],
    [1009, "Gabriel",    28, "(41) 91234-5686", 150.00, 50, 50, 60, 60, 60],
    [1009, "Luíz",    22, "(41) 91234-5686", 200.00, 50, 50, 60, 60, 60]
]

# MENU
while True:
    print("\n=== MENU ===")
    print("1 - Ver treino mais longo do aluno inserido")
    print("2 - Calcular tempo total semanal do aluno inserido")
    print("3 - Mostrar matriz dos alunos")
    print("4 - Mostrar tipos de treino")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        dia, tempo = TreinoMaisLongoAluno(alunoManual[5:10])
        print(f"Treino mais longo: {dia} com {tempo} minutos")
    elif opcao == '2':
        total = TempoTotalSemanaAluno(alunoManual[5:10])
        print(f"Tempo total da semana: {total} minutos")
    elif opcao == '3':
        MostrarMatrizAlunos()
    elif opcao == '4':
        MostrarTiposTreino()
    elif opcao == '0':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")