# Primeiros Exemplos
from string import Template
from calendar import c
import decimal
from decimal import Decimal, getcontext
from re import T, X


print('primeiro programa')
print(1 + 8 + 1)
print(5 * 10)


# Tipos Básicos
print(True)
print(False)
print(1.2 + 1)
print('Aqui eu falo na minha língua')
print("Também funciona")
print('eu sou ' + 3 * 'muito ' + 'inteligente')
# print(3 + '3') -> ambiguidade
print([1, 2, 3])
print({'nome': 'John', 'idade': 22})
print(None)


# Variáveis
a = 10
b = 5.2

print(a + b)

a = 'Agora sou uma string!'
print(a)
a
b

# print(a + b)


# Operadores Aritméticos
print(2 + 3)
print(4 - 7)
print(2 * 5.3)
print(9.4 / 3)
print(9.4 // 3)
print(2 ** 8)
print(10 % 3)

a = 12
b = a
print(a + b)


# Minhas variáveis desafio
salario = 3450.45
despesas = 2456.2

# Resposta do desafio
print(despesas / salario * 100)


# Operadores Relacionais
print(3 > 4)
print(4 >= 3)
print(1 < 2)
print(3 <= 1)
print(3 != 2)
print(3 == 3)
print(2 == '2')


# Operadores de Atribuição
a = 3
a = a + 7
print(a)

# a = 5
a += 5  # a = a + 5
print(a)

a -= 3
print(a)

a *= 2
print(a)

a /= 4
print(a)

a %= 4
print(a)

a **= 8
print(a)

a //= 256
print(a)


# Operadores Lógicos
True or False
7 != 3 and 2 > 3

# Tabela verdade do AND
True and True
True and False
False and True
False and False
True and True and False and True and True and True

# Tabela verdade do OR
True or True
True or False
False or True
False or False
False or False or True or False or False or False

# Tabela verdade do XOR
True != True
True != False
False != True
False != False

# Operador de Negação (unário)
not True
not False

not 0
not 1
not not -1
not not True

# Cuidado!
True & False
False | True
True ^ False

# AND Bit-a-bit
# 3 = 11
# 2 = 10
# _ = 11
3 & 2

# OR Bit-a-bit
# 3 = 11
# 2 = 10
# _ = 11
3 | 2

# XOR Bit-a-bit
# 3 = 11
# 2 = 10
# _ = 01
3 ^ 2

# Um pouco de realidade
saldo = 1000
salario = 4000
despesas = 3900

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario

meta = saldo_positivo and despesas_controladas
meta

# Desafio Operados Lógicos

# Os Trabalhos
trabalho_terca = True
trabalho_quinta = False

"""
- Confirmado os 2: TV 50' + Sorvete
- Confirmado apenas 1: TV 32' + Sorvete
- Nenhum confirmado: Fica em casa
"""
tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta  # xor
mais_saudavel = not sorvete

print("Tv50={} Tv32={} Sorvete={} Saudável={}"
      .format(tv_50, tv_32, sorvete, mais_saudavel))

# "{}, {} = {}".format(1, False, 'resultado')


# Operadores Unários
a = 3
# a++
# a += 1
# a
# a--
++a
++a
-a
+a

not 0
not 1
not -2
not False
not not True


# Operadores Ternários
esta_chovendo = False

print('Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chovendo])


# Mais Operadores

# Operador de Membro
lista = [1, 2, 3, 'Ana', 'Carla']
2 in lista
'Ana' not in lista

# Operador de Identidade
x = 3
y = x
z = 3
x is y
y is z
x is not z

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

lista_a is lista_b
lista_b is lista_c
lista_a is not lista_c


# Builtins

# type()
type(1)
__builtins__.type('Fala Galera!')
__builtins__.print(10 / 3)

# __builtins__.help(__builtins__.dir)

# a = 7
# import math
# dir ()
# dir(__builtins__)


name = 'João da Silva'
type(name)
__builtins__.len(name)

dir()


# Conversão de Tipos
2 + 3
'2' + '3'
# 2 + '3'
# print (2 + '3')

a = 2
b = '3'

print(type(a))
print(type(b))

print(a + iny(a))
print(str(a) + b)

type(str(a))

# print(2 + int('3.4'))


# Coerção Automática
10 / 2
type(10 / 2)
10 / 3
10 // 3
type(10 // 3)
10 // 3.3
type(10 // 3.3)
10 / 2.5
2 + True
2 + False
type(1 + 2)
type(1 + 2.5)


# Tipos Numéricos
dir(int)
dir(float)

a = 5
b = 2.5
a / b
a + b
a * b

type(a)
type(b)
type(a - b)

b.is_integer()
5.0.is_integer()

dir(int)
int.__add__(2, 3)
2 + 3

(-2).__abs__()
abs(-2)

(-3.6).__abs__()
dir(float)
abs(-3.6)


#1.1 + 2.2
Decimal(1) / Decimal(7)

getcontext().prec = 4
Decimal(1) / Decimal(7)
Decimal.max(Decimal(1), Decimal(7))
dir(Decimal)

1.1 + 2.2
getcontext().prec = 10
Decimal(1.1) + Decimal(2.2)

dir(decimal)
dir()


# Tipo String
dir(str)
nome = 'Saulo Pedro'
nome
nome[0]
# nome[0] = 'p'

# 'marca d'água'
"Dias D'Avila" == 'Dias D\'Avila'
"Teste \" funciona!"
texto = 'Texto entre apostrófos pode ter "aspas"'
texto

doc = """Texto com múltiplas
      ... linhas"""
doc
print('Texto com múltiplas\n\t... linhas')
print(doc)

doc2 = '''Também é possível
... com 3 aspas simples'''
doc2


nome = 'Ana Paula'
nome[0]
nome[6]
nome[-3]
nome[4:]
nome[-5:]
nome[:3]
nome[2:5]
nome[::-1]

numeros = '1234567890'
numeros
numeros[::]
numeros[::2]
numeros[1::2]
numeros[::-1]
numeros[::-2]


frase = 'Python é uma linguagem excelente'
'py' not in frase
'ing' in frase
len(frase)
frase.lower()
frase
frase = frase.upper()
frase

frase.split()
frase.split('E')

# dir(str)
# help(str.center)


a = '123'
b = ' de Oliveira 4'
a + b
a.__add__(b)
str.__add__(a, b)

len(a)
a.__len__()
'1' in a
a.__contains__('1')

dir(str)


# Lista
lista = []
type(lista)
dir(lista)
# help(list)
len(lista)
lista.append(1)
lista.append(5)
lista
len(lista)

nova_lista = [1, 5, 'Ana', 'Bia', 'John']
nova_lista
nova_lista.remove(5)
nova_lista
nova_lista.reverse()
nova_lista

lista = [1, 5, 'Rebeca', 'Guilherme', 3.1415]
lista.index('Guilherme')
# lista.index(42)
lista[2]
1 in lista
'Rebeca' in lista
'Pedro' not in lista
lista[0]
lista[4]
# lista[5]
lista[-1]
lista[-5]


lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
lista[1:3]
lista[1:-1]
lista[1:]
lista[:-1]
lista[:]
lista[::2]
lista[::-1]
del lista[2]
lista
del lista[1:]
lista


# Tupla
tupla = tuple()
tupla = ()
type(tupla)
dir(tupla)
# help(tuple)
type(tupla)
tupla = ('um')
type(tupla)
tupla = ('um',)
type(tupla)
tupla[0]
# tupla[0] = 'novo'
cores = ('verde', 'amarelo', 'azul', 'branco')
cores[0]
cores[-1]
cores[1:]

cores.index('amarelo')
cores.count('azul')
len(cores)


# Dicionário
pessoa = {'nome': 'Prof(a). Ana', 'idade': 38, 'cursos': [
    'Inglês', 'Português']}
type(pessoa)
dir(dict)
len(pessoa)

pessoa
pessoa['nome']
pessoa['idade']
pessoa['cursos']
pessoa['cursos'][1]
# pessoa['tags']
pessoa.keys()
pessoa.values()
pessoa.items()
pessoa.get('idade')
pessoa.get('tags')
pessoa.get('tags', [])


pessoa = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
pessoa['idade'] = 44
pessoa['cursos'].append('Angular')
pessoa
pessoa.pop('idade')
pessoa
pessoa.update({'idade': 40, 'Sexo': 'M'})
pessoa
del pessoa['cursos']
pessoa
pessoa.clear()
pessoa


# Conjunto
a = {1, 2, 3}
type(a)
# a[0]
a = set('coddddd3r')
print(a)
print('3' in a, 4 not in a)
{1, 2, 3} == {3, 2, 1, 3}

# operações
c1 = {1, 2}
c2 = {2, 3}
c1.union(c2)
c1.intersection(c2)
c1.update(c2)
c1
c2 <= c1
c1 >= c2

{1, 2, 3} - {2}
c1 - c2
c1 -= {2}
c1


# Interpolação

nome, idade = 'Ana', 30

print('Nome: %s Idade: %d' % (nome, idade))  # mais antiga
print('Nome: {0} Idade: {1}' .format(nome, idade))  # python < 3.6
print(f'Nome: {nome} Idade: {idade}')  # python >= 3.6

s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))
