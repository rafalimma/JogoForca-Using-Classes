# ideia: o Menu contem ou faz uma asoociação com Jogadores que são outra classe

nomes = []

print('__BEM VINDO AO JOJO DA FORCA__')
print()
while True:
    nome = input('Digite seu nickname: ')
    print()
    
    if nome not in nomes:
        print(f'Olá {nome}, o jogo da forca se basea em uma palavra secreta e aleatória'
            'você deve descobrir a palavra secreta chutando uma letra ou fazer um palpite de qual é a palavra secreta.')
        print(f'A cada letra ou palpite errado um membro do jogador é exposto na forca'
            '(cabeça, torso, pernas e braços) quando todos os membros estiverem na forca você perde.')
        
    else:
        print(f'Bem vindo de volta {nome} seu histórico de partidas esta aqui:')
        print('score')
        print('hank')
        
    print()
    opc = input('Começar jogo? s:sim n:não ')

    if opc == 's':
        dificulade = input('Escolha a dificuldade: '
               'fácil(1), difícil(2), extremo(3)')
        if dificulade == '1':
            print('jogo na dificulade 1')
        elif dificulade == '2':
            print('jogo na dificulade 2')
        elif dificulade == '3':
            print('jogo na dificulade 3')
        else:
            print('digite uma dificuldade')
        print('começar jojo')
        continue
    if opc == 'n':
        continue
    else:
        print('digite a opção corretamente')

