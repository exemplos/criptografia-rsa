

tabela = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
tabela_inv = dict((v,k) for k,v in tabela.items())

def converter(palavra):
    resposta = []
    for letra in palavra:
        resposta.append(tabela.get(letra))
    return resposta

def desconverter(palavra):
    resposta = []
    for letra in palavra:
        resposta.append(tabela_inv.get(letra))
    return resposta

def calcular(convertido, e, n):
    resposta = []
    for letra in convertido:
        resposta.append((letra ** e) % n)
    return resposta

def encriptar(palavra, e, n):
    convertido = converter(palavra)
    return calcular(convertido, e, n)

def decriptar(palavra, n, d):
    resposta = []
    for letra in palavra:
        resposta.append((letra ** d) % n)
    return resposta

palavra1 = ['c', 'h', 'i', 'c', 'o']

palavra2 = ['t', 'u', 'r', 'i', 'n', 'g']

encriptado1 = encriptar(palavra1, 13, 697)
encriptado2 = encriptar(palavra2, 13, 697)

print(encriptado1)
print(encriptado2)

decriptado1 = decriptar(encriptado1, 697, 197)
decriptado2 = decriptar(encriptado2, 697, 197)

print(decriptado1)
print(decriptado2)

original1 = desconverter(decriptado1)
original2 = desconverter(decriptado2)

print(original1)
print(original2)

