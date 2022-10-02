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

print('snngc - sistema nacional de navegação da guarda costeira'.upper())
#Titulo do programa#

ins1 = 'bruno'
ins2 = 'carlos'
ins3 = 'natalia'
ins4 = 'cesar'
ins5 = 'caio'
ins6 = 'sofia'
#nome dos funcionarios#

usuario = input(print('Digite seu usuario: '))
#Login#
senha = input(print('Digite sua senha: '))
#passwor#

if usuario == 'bruno' and senha == '123':
    print('acesso permitido')
#Verificação do Login e senha do usuario#
else: 
    print('acesso negado')
    exit()
#Caso login e senha estiver errado, encerramento do programa#

key = 9
#chave contando da primeira letra do alfabeto, no caso contando a partir da letra A (em maiusculo)#
original = 'Australia'
#Informação original#
ciphered = caesar(original, key, MODE_ENCRYPT)
#Informação criptografada#
plain = caesar(ciphered, key, MODE_DECRYPT)
#informação descriptografada#

key = 6
original2 = 'Italia'
ciphered2 = caesar(original, key, MODE_ENCRYPT)
plain2 = caesar(ciphered, key, MODE_DECRYPT)
#mesmas informaçães da chave 9 (key 9)#

while 'esc' != '4':
    sleepTime = 2.500
    while time.time():
        time.sleep(sleepTime) 
        #while para ter um tempo para aparecer as opções para o usuario, e caso ele digite o numero 4 ele encerre \
        # o programa, sleepTime é o tempo para a seleção aparecer#
        esc = input(print('De qual setor gostaria de entrar?\n1 - navios\n2 - rotas\n3 - funcionarios\n4 - sair '))
        #Menu de opções para o usuario
        if esc == '1':
            print('Atena - Ativo\nMeniac - Em rota\nSafira - Manutenção\nJade - Ativo\nJasmin - Ativo\nKatrina - Em rota')
        elif esc == '2':
            print('Meniac\nEm rota para',ciphered,'\nKatrina\nEm rota para',ciphered2)
        elif esc == '3':
            print('\n',ins1,'\n',ins2,'\n',ins3,'\n',ins4,'\n',ins5,'\n',ins6,'\n')
        elif esc == '4':
            exit()        
        elif esc == 'sd':
            cod = input(print('Qual voce quer ver?\n5 - rotas\n6 - funcionarios'))
        elif cod == '5':
            print('Meniac\nEm rota para',plain2,'\nKatrina\nEm rota para', plain2)
        elif cod == '6':
            print('\n',ins1,'ID: 80.954.652-12','\n',ins2,'\n',ins3,'\n',ins4,'\n',ins5,'\n',ins6,'\n')
        else:
            print('Obrigado!')
            exit()


#Operadores IF e ELSE, esc = 1: Mostra todos os navios e o status deles. esc = 2: mostra as rotas deles (criptografadas).\
# esc = 3: mostra todos os funcionarios (*** ideia para mostrar identidades criptografadas ***) \
# esc = 4: finaliza o programa. #
print('222222222222222222222222')
