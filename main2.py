# função para calcular a área total dos cômodos
def calcular_area_comodos():
    # inicializa a variavel que armazenará a area dos cômodos
    total_area = 0

    # loop que continua pedindo dados até que a pessoa decida parar
    while True:
        # solicita a pessoa a largura do comodo
        largura = float(input("Digite a largura do cômodo (em metros): "))

        # Solicita ao usuario o comprimento do cômodo
        comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

        # calcula a área do comodo multiplicando largura por comprimento
        area_comodo = largura * comprimento

        # exibe a área do cômodo feita com duas casas decimais
        print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.")

        #coloca a área do cômodo ao total acumulado
        total_area += area_comodo

        # Pergunta a pessia se deseja adicionar mais comodos
        mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower()

        # Se a resposta não for 's', sai do loop
        if mais_comodos != 's':
            break

    # retorna a área total dos comodos
    return total_area


# Chama a função para calcular a área total
area_total = calcular_area_comodos()

# Exibe a área total da casa feita com duas casas decimais
print(f"A área total da casa é: {area_total:.2f} metros quadrados.")
