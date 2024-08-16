# funçao para diagnosticar diabetes com base nos valores da glicemia
def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial):
    # Verifica se os valores indicam Diabetes
    if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200:
        return "Diabetes"
    # verifica se os valores indicam Pré diabetes
    elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200:
        return "Pré-diabetes"
    # se for o contrário, o diagnóstico é Normal
    else:
        return "Normal"

# Solicita a pessoa o valor da glicemia em jejum e converte para float
glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): "))
# Solicita a pessoa o valor da glicemia pos prandial e converte para float
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): "))

# chama a função para diagnosticar diabetes e armazena o resultado
resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial)

# Exibe o de acordo com os nos valores fornecidos
print(f"O diagnóstico é: {resultado}")
