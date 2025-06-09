from random import sample, choice
from time import sleep

def dias_treino(quant_treinos):
    dias_mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    dias_treino = sample(dias_mes, quant_treinos)

    return dias_treino

def grupos_dia(grupos_treinados, dias):
    grupos_escolhidos = []
    for g, e in grupos_treinados.items():
        if e == 'S':
            grupos_escolhidos.append(g)

    grupos_dia_dict = {}
    for dia in dias:
        grupos_dia_dict[dia] = sample(grupos_escolhidos, 4)

    return grupos_dia_dict

def gerar_tabela_treino(grupos_musculares, treino):
    tempos = [10, 15, 20, 25]
    tabela = []
    for grupo in grupos_musculares:
        linha = []
        for dia in range(1, 31):
            if dia in treino and grupo in treino[dia]:
                tempo = choice(tempos)
                linha.append(tempo)
            else:
                linha.append('--')
        tabela.append(linha)
    return tabela

def exibir_tabela_treino(grupos_musculares, tabela):
    print(f'{"Grupo/Dia":^15}', end='')
    for dia in range(1, 31):
        print(f'{dia:^6}', end='')
    print()
    for i, grupo in enumerate(grupos_musculares):
        print(f'{grupo:^15}', end='')
        for tempo in tabela[i]:
            print(f'{str(tempo):^6}', end='')
        print()
    print()
    print(50 * '-')
    print()




exercicios_por_grupo = {
    'Peitoral': [
        'Supino reto com barra',
        'Supino inclinado com halteres',
        'Crossover na polia (ou peck deck)'
    ],
    'Costas': [
        'Puxada na frente na polia alta',
        'Remada curvada com barra',
        'Remada unilateral com halteres'
    ],
    'Ombros': [
        'Desenvolvimento com halteres ou barra',
        'Elevação lateral',
        'Elevação frontal'
    ],
    'Bíceps': [
        'Rosca direta com barra',
        'Rosca alternada com halteres',
        'Rosca no banco Scott'
    ],
    'Tríceps': [
        'Tríceps testa com barra EZ',
        'Tríceps pulley (cabo) com barra reta ou corda',
        'Mergulho entre bancos (paralelas ou banco livre)'
    ],
    'Glúteos': [
        'Agachamento livre',
        'Cadeira abdutora',
        'Avanço (passada) com halteres'
    ],
    'Panturrilha': [
        'Elevação de panturrilha em pé',
        'Elevação de panturrilha sentado',
        'Leg press com ênfase na panturrilha'
    ],
    'Posteriores': [
        'Mesa flexora',
        'Stiff com barra ou halteres',
        'Levantamento terra romeno'
    ],
    'Quadríceps': [
        'Agachamento livre',
        'Leg press',
        'Cadeira extensora'
    ],
    'Abdômen': [
        'Abdominal na máquina',
        'Prancha isométrica',
        'Elevação de pernas na barra fixa ou banco inclinado'
    ]
}

print(50 * '-')
print(f'{'|'}{'A academia':^48}{'|'}')
print(50 * '-')
print()
print(f"{'Bem vindo à A academia':^50}")
print()
print(f'{'Mensalidades:':^50}')
print(f'{'Preço / Treinos por mês':^50}')
print(f'{'-' * 30:^50}')
print(f'{'R$ 100,00 / 12 treinos':^50}')
print(f'{'R$ 110,00 / 16 treinos':^50}')
print(f'{'R$ 120,00 / 20 treinos':^50}')
print(f'{'R$ 150,00 / Livre':^50}')
print(f'{'-' * 30:^50}')
print()

nome = input('Digite o nome do aluno: ')
matricula = input('Digite o número de matrícula do aluno: ')

while True:
    mensalidade = float(input('Digite qual plano de mensalidade deseja: R$ '))
    
    if mensalidade < 100 or mensalidade > 150:
        print('Erro!! Não existe plano com esse valor!!')

    else:
        break

if mensalidade == 150:
    quant_treinos = int(input('Quantos treinos deseja fazer durante o mês? '))

else:
    quant_treinos = int(((mensalidade - 100) / 2.5) + 12)

print(50 * '-')
print()

print(f'{'Digite [S] para os grupos musculares que':^50}')
print(f'{'deseja treinar ou [N] para os que não.':^50}')
print()

grupos_musculares = ['Peitoral', 'Costas', 'Ombros', 'Bíceps', 'Tríceps', 'Glúteos', 'Panturrilha', 'Posteriores', 'Quadríceps', 'Abdômen']
grupos_treinados = {}

for g in grupos_musculares:
    grupos_treinados[g] = input(f'Deseja treinar {g}? ').upper()

print(50 * '-')
print()

dias = dias_treino(quant_treinos)
treino = grupos_dia(grupos_treinados, dias)
tabela_treino = gerar_tabela_treino(grupos_musculares, treino)

while True:
    print(f'{'O que deseja fazer agora?':^50}')
    print(f'{'[1] para visializar seu treino':^50}')
    print(f'{'[2] para sugestões de exercícios (por dia)':^50}')
    print(f'{'[3] visualizar o treino mais longo':^50}')
    print(f'{'[4] para encerrar programa':^50}')
    print()
    resposta = int(input('Digite a opção desejada: '))
    print()

    while resposta < 1 or resposta > 4:  
        print('Opção inválida! Digite novamente.')
        resposta = int(input('Digite a opção desejada: '))
        print()
    
    if resposta == 1:
        print(f'{"Visualizando seu treino...":^50}')
        print()
        sleep(2)
        exibir_tabela_treino(grupos_musculares, tabela_treino)

    elif resposta == 2:
        qualDia = int(input('Digite o dia que deseja ver os exercícios: '))

        while qualDia not in dias:
            print('Dia inválido! Digite novamente.')
            qualDia = int(input('Digite o dia o qual deseja ver os exercícios: '))

        print(f'{"Lista de sugestões de exercícios para o dia:":^50}')

        sugestao = []

        for grupo in treino[qualDia]:
            sugestao.append(exercicios_por_grupo[grupo])
        
        for i in range(len(sugestao)):
            for j in range(len(sugestao[i])):
                print(f'- {sugestao[i][j]}')

        print()
        print(50 * '-')
        print()

    elif resposta == 3:
        print(f'{"Esse é o treino mais longo":^50}')
        print()
        sleep(2)

        maior_tempo = 0
        dia_mais_longo = None

        for dia in range(1, 31):
            soma = 0
            for linha in tabela_treino:
                valor = linha[dia-1]
                if valor != '--':
                    soma += valor
            if soma > maior_tempo:
                maior_tempo = soma
                dia_mais_longo = dia

        if dia_mais_longo is not None:
            print(f'O dia com o treino mais longo foi o dia {dia_mais_longo} com {maior_tempo} minutos de treino.')
        else:
            print('Nenhum treino registrado nos dias do mês.')

        print()
        print(50 * '-')
        print()

    elif resposta == 4:
        print('Encerrando o programa...')
        sleep(2)
        print('Programa encerrado com sucesso!')
        break
