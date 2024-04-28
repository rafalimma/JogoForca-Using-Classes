import random
from jogadores import Jogadores, Ranking
#desenho da forca
desenhos_forca = [
    "  __\n |    |\n |\n |\n |\n |\n|",
    "  __\n |    |\n |    O\n |\n |\n |\n|",
    "  __\n |    |\n |    O\n |    |\n |\n |\n|",
    "  __\n |    |\n |    O\n |   /|\n |\n |\n|",
    "  __\n |    |\n |    O\n |   /|\\\n |\n |\n|",
    "  __\n |    |\n |    O\n |   /|\\\n |   /\n |\n|"
]


#função pra captar palavra 1 (faceis)
def choose_word1():
    with open("palavras1.txt", "r") as file:
        lines = file.readlines()
    word_info = random.choice(lines).strip().split(",")
    #palavra
    word = word_info[0].lower()
    #dica
    hint = word_info[1].strip()
    return word, hint

#função para captar palavra 2 (medias)
def choose_word2():
    with open("palavras2.txt", "r") as file:
        lines = file.readlines()
    word_info = random.choice(lines).strip().split(",")
    word = word_info[0].lower()
    hint = word_info[1].strip()
    return word, hint


#função para captar palavras 3 (impossiveis)
def choose_word3():
    with open("palavras3.txt", "r") as file:
        lines = file.readlines()
    word_info = random.choice(lines).strip().split(",")
    word = word_info[0].lower()
    hint = word_info[1].strip()
    return word, hint

#função da linha do jogo antes de escrever a palavra ex: "_ _ _ _ _"
def display_word(word, guesses):
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "_ "
    return display

#linkagem para aparecer o desenho da forca toda vez q o player erra alguma levra
def display_forca(erros):
    print(desenhos_forca[erros])

print('----------------------------------------------')
print('BEM VINDO AO JOGO DA FORCA')
print('----------------------------------------------')
print()

while True:
    #aqui é construida a classe Jogador com os valores de resultados nulos
    nome = Jogadores(
        input('Digite seu nickname: '), 0, 0, 0)
    print()
    # aqui há uma verificação (), compara o self.nome com os nomes dos jogadores já jogaram
    # se é um jogador novo os dados são salvos como nulos pois ele ainda não terminou sua jogada
    if not nome.cheka_nickname():
        nome.salva_nickname()

    print()
    # aqui é chamado o método ranking que mostra o ranking dos jogadores
    ranking = Ranking(None, None, None, None)
    ranking.ranking()


    print()
    #aqui é chamado o método para mostrar o tutorial
    nome.mostrar_info()

    print()
    opc = input('Começar jogo? (s:sim, n:não): ')

    if opc == 's':
        dificuldade = input('Escolha a dificuldade: fácil(1), difícil(2), IMPOSSIVEL(3): ')

        print('Começar jogo...')

        if dificuldade == '1':
            print('Jogo na dificuldade 1')
            # Cada dificuldade tem pontos de vitória diferentes
            pontos_de_vitoria = 500
            word, hint = choose_word1()
            print("Dica:", hint)
        elif dificuldade == '2':
            pontos_de_vitoria = 1000
            print('Jogo na dificuldade 2')
            word, hint = choose_word2()
            print("Dica:", hint)
        elif dificuldade == '3':
            pontos_de_vitoria = 2000
            print('Jogo na dificuldade 3')
            print('')
            word, hint = choose_word3()
            print("Dica:", hint)
        
        guessed_letters = []
        attempts = 6
        # aqui é declarada a variável para diminuir os pontos conforme as tentativas vão dimunuindo
        diminuidor_pontos = 0
        while attempts > 0:

            print("\nPalavra: ", display_word(word, guessed_letters))
            display_forca(6 - attempts)
            guess = input("Digite uma letra: ").lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Por favor, insira apenas uma letra válida.")
                continue

            if guess in guessed_letters:
                print("Você já tentou esta letra. Tente outra.")
                continue

            guessed_letters.append(guess)
            
            #verifica se a letra esta na palavra
            if guess not in word:
                attempts -= 1
                print("Letra incorreta! Você tem {} tentativas restantes.".format(attempts))
                diminuidor_pontos += 100
            else:
                print("Letra correta!")
            # se nao existir "_" no display significa que o player acertou todas as letras
            if "_" not in display_word(word, guessed_letters):
                print("\nParabéns! Você adivinhou a palavra: ", word)
                vitorias = 1
                # aqui é o script que salva o jogo:
                while True:
                    opcao = input('DESEJA SALVAR O JOGO? (s:sim/n:não)')
                    if opcao == 's':
                        pontos_de_vitoria = pontos_de_vitoria - diminuidor_pontos
                        #aqui é chamado o método para atualizar a pontuação
                        nome.atualiza(pontos_de_vitoria, vitorias, 0)
                        break
                    elif opcao == 'n':
                        print('jogo não foi salvo')
                        break
                    else:
                        print('digite corretamente')
                        continue
                break

            if attempts == 0:
                print("\nVocê perdeu! A palavra era: ", word)
                derrotas = 1
                # aqui é o script que salva o jogo:
                while True:
                    opcao = input('DESEJA SALVAR O JOGO? (s:sim/n:não)')
                    if opcao == 's':
                        #aqui é chamado o método para atualizar a pontuação
                        nome.atualiza(0, 0, derrotas)
                        break
                    elif opcao == 'n':
                        print('jogo não foi salvo')
                        break
                    else:
                        print('digite corretamente')
                        continue
                break
        continue

    elif opc == 'n':
        print('Jogo encerrado.')
        break

    else:
        print('Digite uma opção válida.')
        continue
