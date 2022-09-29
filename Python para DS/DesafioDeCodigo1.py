# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário,
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Exemplos de Entrada	Exemplos de Saída
# 100 2 2               25.00

# Abaixo segue um exemplo de código que você pode ou não utilizar
entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

# TODO: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman,
# com 2 casas decimais no espaço #em branco abaixo:

# icm = round(distancia / (diametro1 + diametro2),2)  # desafio barrava dessa forma

icm = distancia / (diametro1 + diametro2)
icm = f"{icm:.2f}"
print(icm)


# Dados o número total de cachorros-quentes consumidos e o número total de participantes na competição,
# você deve escrever um programa para determinar o número médio de cachorros-quentes consumidos pelos participantes.

valores = input().split()

quantidade = int(valores[0])
participantes = int(valores[1])

# media = round(quantidade/participantes, 2)  # desafio barrava dessa forma

media = quantidade/participantes
media = f'{media:.2f}'
print(media)

# Rubens quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem de carro, sendo que seu
# carro faz 12 KM/L. Como ele não sabe fazer um programa que o auxilie nessa missão, ele te pede ajuda. Para efetuar
# o cálculo, deve-se fornecer o tempo gasto em horas na viagem e a velocidade média durante a mesma em km/h. Assim,
# você conseguirá passar para Rubens qual a distância percorrida e, em seguida, calcular quantos litros serão necessários
# para a viagem que ele quer fazer. Mostre o valor com 3 casas decimais após o ponto.


valores = input().split()

CARRO = 12  # km/L
tempo_viagem = int(valores[0])  # h
velocidade_media = int(valores[1])  # km/h
distancia_percorrida = tempo_viagem * velocidade_media  # km

# litros = round(distancia_percorrida / CARRO,3)  # desafio barrava dessa forma

litros = distancia_percorrida / CARRO
litros = f'{litros:.3f}'
print(litros)
