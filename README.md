MODE_ENCRYPT = 1
MODE_DECRYPT = 0

def caesar(data, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    new_data = ''
#definição do alfabeto da criptografia#    
    for c in data:
        index = alphabet.find(c)
#procurando a letra C para começar a criptografia a patir dela#
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data
import time

key = 9
#chave contando da primeira letra do alfabeto, no caso contando a partir da letra A (em maiusculo)#
original1 = input(print("Digite a Rota do navio Jade: "))
#Informação original#
ciphered1 = caesar(original1, key, MODE_ENCRYPT)
#Informação criptografada#
plain1 = caesar(ciphered1, key, MODE_DECRYPT)
#informação descriptografada#

print(ciphered1)

key = 5
#chave contando da primeira letra do alfabeto, no caso contando a partir da letra A (em maiusculo)#
original2 = input(print("Digite a Rota do navio Vitoria: "))
#Informação original#
ciphered2 = caesar(original2, key, MODE_ENCRYPT)
#Informação criptografada#
plain2 = caesar(ciphered2, key, MODE_DECRYPT)
#informação descriptografada#

print(ciphered2)

us = input(print("Digite seu usuario: "))
senha = input(print("digite a senha: "))

if us == 'bruno' and senha == '123':
    print("a rota do navio jade é: ",plain1)
    print("a rota do navio Victoria é: ",plain2)
else:
    exit()
