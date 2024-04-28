
import json

class Jogadores:
    def __init__(self, nickname, pontos, vitorias, derrotas):
        self.nickname = nickname
        self.pontos = pontos
        self.vitorias = vitorias
        self.derrotas = derrotas
    #método que salva/cria o nome do jogador em jogadores.json
    def salva_nickname(self):
        with open("jogadores.json", "r+") as arquivo:
            jogadores = json.load(arquivo)
        #aqui é feito um dicionário com os atributos da classe que será adicionado a lista do json
        novo_jogador = {"nickname": self.nickname,
                            "historico": {
                                "pontuacao": self.pontos,
                                "vitorias": self.vitorias,
                                "derrotas": self.derrotas
                                }
                            }
        jogadores.append(novo_jogador)
        # faz o dump em jogadores
        with open("jogadores.json", 'w') as arquivo:
            json.dump(jogadores, arquivo, indent=4)
    
    # método para atualizar os dados se o jogador escolheu salvar o jogo
    def atualiza(self, pontos, vitorias, derrotas):
        with open("jogadores.json", "r+") as arquivo:
            jogadores = json.load(arquivo)
            #itera sobre a lista de jogadore no json
            for jogador in jogadores:
                # se o nome da classe for igual ao do que esta no dicionário
                # é alterado os dados com os argumentos passados
                if self.nickname == jogador['nickname']:
                    jogador["historico"]["pontuacao"] += pontos
                    jogador["historico"]["vitorias"] += vitorias
                    jogador["historico"]["derrotas"] += derrotas
                arquivo.seek(0)
                json.dump(jogadores, arquivo, indent=4)
                #truncara o arquivo para o numero de bytes
                arquivo.truncate()

    # Método que verifica se o atributo (self.nome) ja existe na lista de jogadores
    def cheka_nickname(self):
        with open("jogadores.json", "r") as arquivo:
            jogadores = json.load(arquivo)
        # itera sobre a lista de jogadores
        for jogador in jogadores:
            # se o nickname da iteração for igual ao atributo
            # retorna o histórico do jogador
            if jogador["nickname"] == self.nickname:
                print("Bem vindo de volta jogador:", self.nickname)
                print('___HISTÓRICO_DE_PONTUAÇÃO___')
                print("Pontuação -> ", jogador["historico"]["pontuacao"])
                print("Vitórias -> ", jogador["historico"]["vitorias"])
                print("Derrotas -> ", jogador["historico"]["derrotas"])
                return True
        else:
            return False
        # com os retornos True ou False é validado para o menu se o cliente existe ou não
        # caso não exista e o retorno seja False é criado um novo jogador pelo método salva_nickname
    
    # Método para mostrar o tutorial do jogo
    def mostrar_info(self):
        print('__Tutorial__')
        print(f'Olá {self.nickname}, o jogo da forca se baseia em uma palavra')
        print('secreta e aleatória. Você deve descobrir a palavra')
        print('secreta chutando uma letra ou fazendo um palpite de qual')
        print('é a palavra secreta.')
        print()
        print('A cada letra ou palpite errado, um membro do jogador é')
        print('exposto na forca (cabeça, torso, pernas e braços). Quando')
        print('todos os membros estiverem na forca, você perde.')

# Aqui é uma classe que herda de Jogadores
class Ranking(Jogadores):
    def __init__(self, nickname, pontos, vitorias, derrotas):
        super().__init__(nickname, pontos, vitorias, derrotas)
    
    # Esse é o método que vai mostrar o Ranking
    def ranking(self):
        with open("jogadores.json", "r+") as arquivo:
            jogadores = json.load(arquivo)
        # Ordena a lista de jogadores com base na pontuação
        # extrai a pontuação de cada jogador x para o sorted ordenar por ordem decrescente
        ranking = sorted(jogadores, key=lambda x: x["historico"]["pontuacao"], reverse=True)
        # Exibe o ranking iterando pelos jogadores e enumerando o ranking começando por 1
        print('___RANKING_DOS_JOGADORES___')
        for i, jogador in enumerate(ranking, start=1):
            print(f"{i}. {jogador['nickname']} - Pontuação: {jogador['historico']['pontuacao']} - Vitórias: {jogador['historico']['vitorias']}")
    

