class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Erica", 1)
aluno_2 = Estudante("Gustavo", 2)
aluno_3 = Estudante("Ana", 3)

# Atributo de Instância: único para cada Instância da classe, varia a cada nova inclusão. A alteração desses atributos não influenciam 
# na alteração das outras instâncias. 

# mostrar_valores(aluno_1, aluno_2, aluno_3)

# Altera apenas a instância -> Instancia.variavel
aluno_1.matricula = 4

# Alterando para todas as instâncias -> Classe.variavel
Estudante.escola = "Python"

# Altera apenas a instância -> Instancia.variavel
aluno_1.escola = "Python"

# mostrar_valores(aluno_1, aluno_2, aluno_3)


############################################################################################################################################

# Métodos de Classe e Métodos Estáticos


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def calcular_idade(cls, ano, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod
    def maior_idade(idade):
        return idade >= 18

p1 = Pessoa("Erica", 21)
p = Pessoa.calcular_idade(2001, "Erica")

print(Pessoa.maior_idade(p1.idade))
print(p.nome, p.idade)

############################################################################################################################################




