MODE_ENCRYPT = 1
MODE_DECRYPT = 0

def caesar(data, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data
import time

print('snngc - sistema nacional de navegação da guarda costeira'.upper())

ins1 = 'bruno'
ins2 = 'carlos'
ins3 = 'natalia'
ins4 = 'cesar'
ins5 = 'caio'
ins6 = 'sofia'

usuario = input(print('Digite seu usuario: '))
senha = input(print('Digite sua senha: '))

if usuario == 'bruno' and senha == '123':
    print('acesso permitido')
else: 
    print('acesso negado')
    exit()

key = 5
original = 'Australia'
ciphered = caesar(original, key, MODE_ENCRYPT)
plain = caesar(ciphered, key, MODE_DECRYPT)

key = 6
original2 = 'Italia'
ciphered2 = caesar(original, key, MODE_ENCRYPT)
plain2 = caesar(ciphered, key, MODE_DECRYPT)

while 'esc' != '4':
    sleepTime = 3.500
    while time.time():
        time.sleep(sleepTime) 
        esc = input(print('De qual setor gostaria de entrar?\n1 - navios\n2 - rotas\n3 - funcionarios\n4 - sair '))

        if esc == '1':
            print('Atena - Ativo\nMeniac - Em rota\nSafira - Manutenção\nJade - Ativo\nJasmin - Ativo\nKatrina - Em rota')
        elif esc == '2':
            print('Meniac\nEm rota para',ciphered,'\nKatrina\nEm rota para',ciphered2)
        elif esc == '3':
            print('\n',ins1,'\n',ins2,'\n',ins3,'\n',ins4,'\n',ins5,'\n',ins6,'\n')
        else:
            print('Obrigado!')
            exit()

