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
original1 = 'Australia'
#Informação original#
ciphered1 = caesar(original1, key, MODE_ENCRYPT)
#Informação criptografada#
plain1 = caesar(ciphered1, key, MODE_DECRYPT)
#informação descriptografada#

key = 6
original2 = 'Italia'
ciphered2 = caesar(original2, key, MODE_ENCRYPT)
plain2 = caesar(ciphered2, key, MODE_DECRYPT)
#mesmas informaçães da chave 9 (key 9)#
firstChoice = True
#firstChoice variavel de controle para verificar os IF e ELIF#

while 'esc' != '4':
    sleepTime = 2.500
    while time.time():
        time.sleep(sleepTime) 
        #while para ter um tempo para aparecer as opções para o usuario, e caso ele digite o numero 4 ele encerre \
        # o programa, sleepTime é o tempo para a seleção aparecer#
        if firstChoice:
            esc = input(print('De qual setor gostaria de entrar?\n1 - navios\n2 - rotas\n3 - funcionarios\n4 - sair '))
        #Menu de opções para o usuario
        if esc == '1':
            print('Atena - Ativo\nMeniac - Em rota\nSafira - Manutenção\nJade - Ativo\nJasmin - Ativo\nKatrina - Em rota')
            firstChoice = True
        elif esc == '2':
            print('Meniac\nEm rota para',ciphered1,'\nKatrina\nEm rota para',ciphered2)
            firstChoice = True
        elif esc == '3':
            print('\n',ins1,'\n',ins2,'\n',ins3,'\n',ins4,'\n',ins5,'\n',ins6,'\n')
            firstChoice = True
        elif esc == '4':
            exit()        
        elif esc == 'sd':
            cod = input(print('Qual dados descriptografados voce quer ver?\n5 - rotas\n6 - funcionarios'))
            esc = " "
            firstChoice = False
        elif cod == '5':
            print('Meniac\nEm rota para',plain1,'\nKatrina\nEm rota para',plain2)
            firstChoice = True
        elif cod == '6':
            print('\n',ins1,'ID: 80.954.652-12','\n',ins2,'ID: 45.154.365-78','\n',ins3,'ID: 25.658.963-12','\n',ins4,'ID: 14.214.985-35','\n',ins5,'ID: 23.123.958-74','\n',ins6,'ID: 12.145.325-96\n')
            firstChoice = True
        else:
            print('Obrigado!')
            exit()
#Operadores IF e ELSE, esc = 1: Mostra todos os navios e o status deles. esc = 2: mostra as rotas deles (criptografadas).\
# esc = 3: mostra todos os funcionarios (*** ideia para mostrar identidades criptografadas ***) \
# esc = 4: finaliza o programa. #
