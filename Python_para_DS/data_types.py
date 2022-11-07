# %%
# LISTAS EM PYTHON

from calendar import c


lista = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]

print(lista)

# 0 2 4 6 8
# retornar o quadrado do número apenas se ele for maior que 6, se não for, retorna ele próprio.
# output: [0, 2, 4, 6, 64]


# índice e objeto
carros = ['gol', 'celta', 'palio']
for i, carro in enumerate(carros):
    print(f"{i} : {carro}")

# ordenando pelo tamanho de cada item da lista em ordem crescente (default)
carros.sort(key=lambda x: len(x))
print(carros)

# ordenando pelo tamanho de cada item da lista em ordem decrescente
carros.sort(key=lambda x: len(x), reverse=True)
print(carros)


# %%
# TUPLAS EM PYTHON


# %%
# CONJUNTOS EM PYTHON

set('abacaxi')  # não suporta indexação

# necessário repassar para list() para acessar cada objeto
list(set({'python', 'java', 'python'}))[0]

a = {1, 2}
b = {3, 4}

a.union(b)  # {1, 2, 3, 4}

c = {1, 2, 3}
d = {2, 3, 4}

c.intersection(d)  # {2, 3}
c.difference(d)  # {1}
d.difference(c)  # {4}

# todos os elementos que não estão na intersecção
c.symmetric_difference(d)  # {1, 4}

e = {1, 2, 3}
f = {4, 1, 2, 5, 6, 3}

e.issubset(f)  # True --> conjunto e é um subconjunto de f
e.issuperset(f)  # False --> todos os elementos de f não estão contidos em e
f.issuperset(e)   # True --> todos os elementos de e estão contidos em f

# para conjuntos disjuntos:

a = {1, 2, 3, 4, 5}
b = {6, 7, 8, 9}
c = {1, 0}

a.isdisjoint(b)  # True
a.isdisjoint(c)  # False --> pois há 1 em ambos os conjuntos


# adicionar elementos:
s = {1, 23}

s.add(25)
s.add(42)
s.add(25)  # elemento ignorado, pois já existe

print(s)  # {1, 42, 25, 23}

s.discard(25)

print(s)  # {1, 42, 23}

s2 = s.copy()
s.clear()
s.pop()  # primeiro valor
s.remove(25)  # ocorre erro se não conter elemento
s.discard(25)  # não ocorre erro se não conter elemento

# %%
# DICIONÁRIOS EM PYTHON


# %%
# FUNÇÕES
