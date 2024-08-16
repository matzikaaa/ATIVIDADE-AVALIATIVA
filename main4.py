# função para calcular a média da turma e listar alunos aprovados e reprovados
def calcular_media_e_aprovacao(notas, nota_minima_aprovacao):
    # Inicia o calculo de notas e listas para alunos aprovados e reprovados
    total_notas = 0
    num_alunos = len(notas)  # numero total de alunos
    aprovados = []
    reprovados = []

    # sobre o dicionário de notas
    for aluno, nota in notas.items():
        total_notas += nota  # Acumula a nota
        # verifica se o aluno foi aprovado ou reprovado
        if nota >= nota_minima_aprovacao:
            aprovados.append(aluno)
        else:
            reprovados.append(aluno)

    # calculá a média das notas
    media_turma = total_notas / num_alunos

    # retorna a média, lista de aprovados e lista de reprovados
    return media_turma, aprovados, reprovados

# notas dos alunos
notas = {
    "Alice": 85,
    "Bruno": 72,
    "Carlos": 60,
    "Diana": 95,
    "Eduardo": 55
}

# mínimo necessário para aprovação
nota_minima_aprovacao = 70

# chama a função e guarda os resultados
media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)

# mostra a média da turma, alunos aprovados e alunos reprovados
print(f"Média da turma: {media_turma:.2f}")
print(f"Alunos aprovados: {', '.join(aprovados)}")
print(f"Alunos reprovados: {', '.join(reprovados)}")
