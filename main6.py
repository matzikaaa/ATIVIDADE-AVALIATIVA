# função para calcular o custo total da viagem
def calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios, custo_pedagio):
    # calcula o custo total com combustível
    custo_combustivel_total = (distancia / consumo_veiculo) * custo_combustivel

    # calcula o custo total com pedgios
    custo_pedagio_total = numero_pedagios * custo_pedagio

    # Calcula o custo total da viagem
    custo_total = custo_combustivel_total + custo_pedagio_total

    # retorna o custo total da viagem o custo com combustivel e o custo com pedagios
    return custo_total, custo_combustivel_total, custo_pedagio_total


# solicita ao usuario a distancia da viagem em quilometros
distancia = float(input("Digite a distância da viagem (em km): "))

# solicita ao usuário o custo do combustivel por litro
custo_combustivel = float(input("Digite o custo do combustível por litro (em R$): "))

# solicita ao usuário o consumo do veiculo em quilometros por litro
consumo_veiculo = float(input("Digite o consumo do veículo (km por litro): "))

# solicita ao usuario o número de pedagios no percurso
numero_pedagios = int(input("Digite o número de pedágios no percurso: "))

# solicita ao usuário o custo de um pedagio
custo_pedagio = float(input("Digite o custo de um pedágio (em R$): "))

# chama a função, para calcular os custos da viagem
custo_total, custo_combustivel_total, custo_pedagio_total = calcular_custo_viagem(
    distancia,
    custo_combustivel,
    consumo_veiculo,
    numero_pedagios,
    custo_pedagio
)

# mostra o custo total da viagem o custo com combustivel, e o custo com pedagios
print(f"Custo total da viagem: R${custo_total:.2f}")
print(f"Custo total com combustível: R${custo_combustivel_total:.2f}")
print(f"Custo total com pedágios: R${custo_pedagio_total:.2f}")
