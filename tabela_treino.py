from random import sample
from time import sleep

def treino(a, b, c):
    dias_mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    dias_treino = sample(dias_mes, a)

    grupos_escolhidos = []
    for g, e in b.items():
        if e == 'S':
            grupos_escolhidos.append(g)

    grupos_dia = {}
    for dia in dias_treino:
        grupos_dia[dia] = sample(grupos_escolhidos, 4)

    tabela = [0] * 12
    for i in range(len(tabela)):
        tabela[i] = [0] * 32

    for i in range(len(tabela)):
        for j in range(len(tabela[i])):
            if i == 0 and j == 1:
                print(f'{'Treinos ˅':^12}', end='')

            elif i == 1 and j == 0:
                print(f'{'Dias >':^6}', end='')

            elif i == 0 or j ==0:
                print(f'{'--':^6}', end='')

            elif i == 1 and j == 1:
                print(f'{'--':^12}', end='')

            elif i == 1:
                print(f'|{j - 1:^4}|', end='')

            elif j == 1:
                print(f'{c[i - 2]:^12}', end='')

            elif (j - 2) in dias_treino and c[i - 2] in grupos_dia[j - 2]:
                print(f'|{'15':^4}|', end='')

            else:
                print(f'|{'--':^4}|', end='')
        
        print()


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

sleep(1)
print(f'Esse é o seu treino {nome}:\n')

treino(quant_treinos, grupos_treinados, grupos_musculares)