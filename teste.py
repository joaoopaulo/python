# Primeiros Exemplos
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
