alunos = []
treinoSemana= {}


nomeAluno = input("Qual o nome do aluno")
matricula = int(input("Qual o número da matricula"))
mensalidade = float(input("qual o valor da mensalidade"))
i = 0
while i < 5:
    treino = input("Qual o treino do aluno")
    tempo = int(input("Qual o tempo do treino em minutos"))
    treinoSemana[treino] = tempo
    i += 1

alunos.append({"nome": nomeAluno, "matricula": matricula, "mensalidade": mensalidade})


funcaoFazer = int(input("Qual função você quer usar: 1 = tempo total semana ; 2 = identificar o treinos mais longo"))

if funcaoFazer == 1:
    tempoTotal = 0
    for treino in treinoSemana:
        tempoTotal += treinoSemana[treino]
    print(f"O tempo total de treino na semana é: {tempoTotal} minutos")
elif funcaoFazer == 2:
    treinoMaisLongo = max(treinoSemana, key=treinoSemana.get)
    print(f"O treino mais longo é: {treinoMaisLongo} com {treinoSemana[treinoMaisLongo]} minutos")
else:
    print("Função inválida. Por favor, escolha 1 ou 2.")


