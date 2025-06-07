import random

# Tipos de treino atualizados
tipos_treino = [
    ["Bíceps", 40],
    ["Perna", 60],
    ["Costas", 50],
    ["Ombro", 45],
    ["Peito", 55]
]

# Funções atualizadas para o aluno inserido manualmente
def treino_mais_longo_aluno(treinos):
    dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
    max_tempo = max(treinos)
    dia = dias[treinos.index(max_tempo)]
    return dia, max_tempo

def tempo_total_semana_aluno(treinos):
    return sum(treinos)

def mostrar_matriz_alunos():
    print("\n=== MATRIZ DE ALUNOS ===")
    print("Matrícula | Nome     | Idade | Celular         | Mensalidade | Seg | Ter | Qua | Qui | Sex")
    for aluno in matriz_alunos:
        print(f"{aluno[0]:>9} | {aluno[1]:<8} | {aluno[2]:>5} | {aluno[3]:<15} | R${aluno[4]:>11} | "
              f"{aluno[5]:>3} | {aluno[6]:>3} | {aluno[7]:>3} | {aluno[8]:>3} | {aluno[9]:>3}")

def mostrar_tipos_treino():
    print("\n=== TIPOS DE TREINO DISPONÍVEIS ===")
    for i, treino in enumerate(tipos_treino, start=1):
        print(f"{i} - {treino[0]} ({treino[1]} min)")

# Coletar dados do aluno inserido
print("=== PLANOS DE MENSALIDADE ===")
print("Básico: R$100 | Intermediário: R$150 | Avançado: R$200")

nome_input = input("\nDigite o nome do aluno: ")
matricula_input = input("Digite o número da matrícula: ")
mensalidade_input = int(input("Digite o valor da mensalidade escolhida (apenas número): R$"))
idade_input = random.randint(18, 35)
celular_input = f"(41) 9{random.randint(8000,9999)}-{random.randint(1000,9999)}"

# Escolher treino para cada dia da semana
dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
treinos_escolhidos = []

print("\nAgora escolha o treino para cada dia da semana:")
mostrar_tipos_treino()

for dia in dias_semana:
    while True:
        try:
            escolha = int(input(f"{dia}: Escolha o número do treino desejado: "))
            if 1 <= escolha <= len(tipos_treino):
                tempo_treino = tipos_treino[escolha - 1][1]
                treinos_escolhidos.append(tempo_treino)
                break
            else:
                print("Escolha inválida. Digite um número válido.")
        except:
            print("Digite um número válido.")

# Criar a matriz e adicionar o aluno
matriz_alunos = []
aluno_manual = [
    int(matricula_input),
    nome_input,
    idade_input,
    celular_input,
    mensalidade_input
] + treinos_escolhidos

matriz_alunos.append(aluno_manual)

# Gerar os outros 9 alunos automaticamente
nomes_exemplo = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo", "Fernanda", "Gustavo", "Helena", "Igor", "Julia"]
mensalidades = [100, 150, 200]

for i in range(9):
    matricula = random.randint(1000, 9999)
    nome = nomes_exemplo[i]
    idade = random.randint(18, 35)
    celular = f"(41) 9{random.randint(8000,9999)}-{random.randint(1000,9999)}"
    mensalidade = random.choice(mensalidades)
    treinos_semana = [random.choice(tipos_treino)[1] for _ in range(5)]
    linha = [matricula, nome, idade, celular, mensalidade] + treinos_semana
    matriz_alunos.append(linha)

# MENU INTERATIVO
while True:
    print("\n=== MENU ===")
    print("1 - Ver treino mais longo do aluno inserido")
    print("2 - Calcular tempo total semanal do aluno inserido")
    print("3 - Mostrar matriz dos alunos")
    print("4 - Mostrar tipos de treino")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        dia, tempo = treino_mais_longo_aluno(aluno_manual[5:10])
        print(f"Treino mais longo: {dia} com {tempo} minutos")
    elif opcao == '2':
        total = tempo_total_semana_aluno(aluno_manual[5:10])
        print(f"Tempo total da semana: {total} minutos")
    elif opcao == '3':
        mostrar_matriz_alunos()
    elif opcao == '4':
        mostrar_tipos_treino()
    elif opcao == '0':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
