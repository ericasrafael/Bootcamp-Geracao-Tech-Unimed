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

# icm = round(distancia / (diametro1 + diametro2),2)    # desafio barrava dessa forma

icm = distancia / (diametro1 + diametro2)
icm = f"{icm:.2f}"
print(icm)


# Dados o número total de cachorros-quentes consumidos e o número total de participantes na competição,
# você deve escrever um programa para determinar o número médio de cachorros-quentes consumidos pelos participantes.

valores = input().split()

quantidade_cachorros_quentes = int(valores[0])
participantes = int(valores[1])

# media = round(quantidade/participantes, 2)            # desafio barrava dessa forma

media = quantidade_cachorros_quentes/participantes
media = f'{media:.2f}'
print(media)

# Rubens quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem de carro, sendo que seu
# carro faz 12 KM/L. Como ele não sabe fazer um programa que o auxilie nessa missão, ele te pede ajuda. Para efetuar
# o cálculo, deve-se fornecer o tempo gasto em horas na viagem e a velocidade média durante a mesma em km/h. Assim,
# você conseguirá passar para Rubens qual a distância percorrida e, em seguida, calcular quantos litros serão necessários
# para a viagem que ele quer fazer. Mostre o valor com 3 casas decimais após o ponto.


valores = input().split()

CARRO = 12                                              # km/L
tempo_viagem = int(valores[0])                          # h
velocidade_media = int(valores[1])                      # km/h
distancia_percorrida = tempo_viagem * velocidade_media  # km

# litros = round(distancia_percorrida / CARRO,3)        # desafio barrava dessa forma

litros = distancia_percorrida / CARRO
litros = f'{litros:.3f}'
print(litros)



# A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo com a tabela abaixo:
# Salário	Percentual de Reajuste
# 0 - 600.00 -- 17%
# 600.01 - 900.00 -- 13%
# 900.01 - 1500.00 -- 12%
# 1500.01 - 2000.00 -- 10%
# Acima de 2000.00 -- 5%
# Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.


percent = {
  2000 : 5,
  1500 : 10,
  900 : 12,
  600 : 13,
  0: 17
}
salario = float(input())

for key in percent.keys():
    if salario > float(key):
        percentual = percent[key]
        break

ganho = salario * (percentual / 100)
novo_salario = salario + ganho


print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {ganho:.2f}")
print(f"Em percentual: {percentual} %")

# Humberto tem um papagaio muito esperto. Quando está com as duas pernas no chão, o papagaio fala em português. 
# Quando levanta a perna esquerda, fala em inglês. Por fim, quando levanta a direita fala em francês. Nico, 
# amigo de Humberto, ficou fascinado com o animal. Em sua emoção perguntou: “E quando ele levanta as duas?”.
#  Antes que Humberto pudesse responder, o papagaio gritou: “Aí eu caio, idiota!”.
# Entrada
# A entrada consiste de diversos casos de teste. Cada caso de teste consiste uma string informando qual a situação 
# de levantamento de pernas do papagaio.
# Saída
# Para cada condição de levantamento de pernas do papagaio, imprima a linguagem que ele utilizará. Caso ele levante ambas as pernas, 
# imprima “caiu”. Quebre uma linha a cada caso de teste.

while True: 
    try: 
      perna = input()     
      
      if perna == 'esquerda':
        print('ingles\n')
      elif perna == 'direita':
        print('frances\n')
      elif perna == 'nenhuma':
        print('portugues\n')
      elif perna == 'ambas':
        print('caiu\n') 
    except EOFError: 
        break


# Desafio
# Dada a letra N do alfabeto, nos diga qual a sua posição.
# Entrada
# Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).
# Saída
# Um único inteiro, que representa a posição da letra no alfabeto.

letra = input() 
print(ord(letra) & 31)