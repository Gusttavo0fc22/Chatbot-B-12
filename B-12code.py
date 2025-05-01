import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep} Sim estou bem {nome}, obrigado por perguntar.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, meu criador se chama Gustavo, sou seu primeiro projeto, ele me criou para ajudar as pessoas.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, gosto muito de ajudar as pessoas este é o intúito pelo qual fui criado.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}Claro {nome}, com base em meu criador, filemes bons seria de super herois e séries seria de ficção científica.{os.linesep}')
    elif resposta == '5':
        print(f'{os.linesep} Claro {nome}, sei que este tipo de pergunta e meio pessoal, más um jogo que meu criador gosta muito é Stray, se der uma olhadinha o meu nome é inspirado no robo do jogo Stray.{os.linesep}')
    if resposta == '6':
        print(f'{os.linesep}{nome}. Por nada, foi um prazer em te conhecer.{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3, 4 ou 5.')

def start():
    print('Olá me chamo B-12 sou um chatbot, tudo bem?')
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    
    while True:
        resposta = input(f"""\nO que gostaria de saber?
[1] Olá Tudo bom?
[2] Quem é seu criador?
[3] O que você gosta de fazer?
[4] Me indica algum gênero de Filme ou série?
[5] Me indica algum jogo legal?
[6] Agradeço por me responder.
""")
        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()