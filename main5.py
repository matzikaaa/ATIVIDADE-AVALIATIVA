# função para calcular o indice de massa Corporal (IMC)
def calcular_imc(peso, altura):
    # Calcula o IMC como peso dividido pelo quadrado da altura
    imc = peso / (altura ** 2)
    # Retorna o valor do IMC
    return imc

# função para classificar o IMC em categorias
def classificar_imc(imc):
    # Classificar o IMC de acordo com os intervalos padrão
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

# função para sugerir atividades físicas com base na classificação do IMC
def sugestao_atividade_fisica(classificacao_imc):
    # fornece sugestões de atividades físicas e dieta baseadas na classificação do IMC
    if classificacao_imc == "Abaixo do peso":
        return "sugere  atividades de fortalecimento muscular."
    elif classificacao_imc == "Peso normal":
        return "sugere a manutenção com atividades aerobicas regulares."
    elif classificacao_imc == "Sobrepeso":
        return "sugere atividades aeróbicas moderadas."
    elif classificacao_imc == "Obesidade grau 1":
        return "sugere-se atividades de baixo impacto."
    elif classificacao_imc == "Obesidade grau 2":
        return "sugere-se exercícios de baixo impacto com supervisão."



# Solicita a pessoa o peso e a altura
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Calcula o IMC
imc = calcular_imc(peso, altura)

# Classifica o IMC
classificacao = classificar_imc(imc)

# obtem a sugestão de atividade física com base na classificação
sugestao = sugestao_atividade_fisica(classificacao)

# Exibe o resultado
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação do IMC: {classificacao}")
print(f"Sugestão de atividade física: {sugestao}")
