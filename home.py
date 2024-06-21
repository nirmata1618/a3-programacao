def adicionar_notas(aluno, quantidade_notas=3):
    for i in range(1, quantidade_notas + 1):
        while True:
            try:
                nota = float(input(f"Insira a nota {i}: "))
                if 0 <= nota <= 10:
                    aluno.append(nota)
                    break
                else:
                    print("Nota inválida. A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
    return aluno

def calcular_media_e_resultado(aluno):
    if not aluno:
        return 0.0, "Reprovado"

    media = sum(aluno) / len(aluno)
    if media >= 7.0:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"

    return media, resultado

notas_aluno = []
notas_aluno = adicionar_notas(notas_aluno)
media, resultado = calcular_media_e_resultado(notas_aluno)
print(f"Média: {media:.2f}")
print(f"Resultado: {resultado}")
