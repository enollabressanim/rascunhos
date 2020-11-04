class Torneira():
    def __init__(self, vazao: float, nome: str):
        self.vazao = vazao
        self.nome = nome

    def modificar_vazao(self, torneira_nome, torneira_vazao):
        pass

class Tanque(Torneira):
  
    def __init__(self, capacidade_maxima: float, capacidade: float):
        self.capacidade_max = capacidade_maxima
        self.capacidade_atual = capacidade
        self.historioco = []
        self.torneiras_saida = []
        self.torneiras_entrada = []
        
    def instalar_torneira(self, nova_torneira, saida):
        if saida == False:
            for torneira in self.torneiras_saida:
                if torneira == nova_torneira:
                    print("Torneira já instalada!")
                    return False
            self.torneiras_saida.append(nova_torneira)
            print('Nova torneira adicionada com sucesso!')
            print(self.torneiras_saida)
        else:
            for torneira in self.torneiras_entrada:
                if torneira == nova_torneira:
                    print("Torneira já instalada!")
                    return False
            self.torneiras_entrada.append(nova_torneira)
            print('Nova torneira instalada com sucesso!')
        return True

    def abrir_torneira(self, nome_torneira, tempo_segundos):
        for torneira in self.torneiras_saida:
            if torneira.nome == torneira.nome:
                if self.capacidade_atual >= float(torneira.vazao)*tempo_segundos:
                    self.capacidade_atual -= float(torneira.vazao)*tempo_segundos
                    print("Água retirada do reservatório :)")
                    print("Quantidade de água:", self.capacidade_atual)
                    return True
                else:
                    self.capacidade_atual = 0
                    print("A água acabou antes do tempo :(")
                    print("Quantidade de água:", self.capacidade_atual)
                    return True

        for torneira in self.torneiras_entrada:
            if torneira.nome == torneira.nome:
                if self.capacidade_atual + float(torneira.vazao)*tempo_segundos <= self.capacidade_max:
                    self.capacidade_atual += float(torneira.vazao)*tempo_segundos
                    print("Água adicionada ao reservatório :)")
                    print("Quantidade de água:", self.capacidade_atual)
                    return True
                else:
                    self.capacidade_atual = self.capacidade_max
                    print("A água acabou transbordando, você desperdiçou água!")
                    print("Quantidade de água:", self.capacidade_atual)
                    return True
        return False

    def recarregar_reservatorio(self):
        self.capacidade_atual = self.capacidade_max
        print("O tanque possui", self.capacidade_atual,"litros.")

    def imprimir_nome_torneiras(self):                   
        print("Torneiras de entrada:")
        for torneira in self.torneiras_entrada:
            print(torneira.nome)
        print("Torneiras de saida:")
        for torneira in self.torneiras_saida:
            print(torneira.nome)

    def remover_torneira(self, nome_torneira, saida):
        if saida == True:
            for torneira in self.torneiras_entrada:
                if torneira.nome == nome_torneira:
                    self.torneiras_entrada.remove(torneira)
                    return True
        else:
            for torneira in self.torneiras_saida:
                if torneira.nome == nome_torneira:
                    self.torneiras_saida.remove(torneira)
                    return True
        return False

    def calcular_tempo_esvaziamento(self):
        contador = 0
        vazao_total = 0
        for torneira in self.torneiras_saida:
            vazao_total += float(torneira.vazao)
        while True:
            self.capacidade_atual -= vazao_total
            contador += 1
            print(vazao_total)
            if self.capacidade_atual <= 0:
                print("Tanque vazio.")
                print(f"Demorou {contador} segundos para esvaziar.")
                break

    def atualizar_torneira(self):
        torneira_nome = input("Digite o nome da torneira que deseja modificar: ")
        torneira_vazao = float(input("Digite a nova vazao da torneira: "))
        for torneira in self.torneiras_entrada:
            if torneira.nome == torneira_nome:
                torneira.vazao = torneira_vazao
        for torneira in self.torneiras_saida:
            if torneira.nome == torneira_nome:
                torneira.vazao = torneira_vazao

print("Informações básicas:")
tamanho_tanque = float(input("Quantos litros cabem no tanque:"))
quantidade_atual = float(input("Quantos litros estão no tanque: "))

caixa = Tanque(tamanho_tanque, quantidade_atual)
                
def inputs_especiais():
    while True:

        print("################################################")
        print("Escolha uma das opções:")
        print("1 - Adicionar torneiras;")
        print("2 - Encher/Esvaziar o tanque;")
        print("3 - Encher o tanque por completo;")
        print("4 - Nomes das torneiras;")
        print("5 - Remover torneira;")
        print("6 - Calcular tempo de esvaziamento;")
        print("7 - Modificar a torneira;")
        print("8 - Sair.")
        func = int(input("Digite a opção: "))
        if func == 1:
            torneira_posicao = input("A torneira irá encher ou esvaziar? (True/False): ")
            if torneira_posicao == "False":
                torneira_posicao = False
            elif torneira_posicao == "True":
                torneira_posicao = True
            torneira_nome = input("Digite o nome da torneira: ")
            torneira_vazao = input("Digite a vazao da torneira: ")
            caixa.instalar_torneira(Torneira(torneira_vazao, torneira_nome), torneira_posicao)

        elif func == 2:
            torneira_nome = input("Digite o nome da torneira: ")
            torneira_tempo = int(input("Digite o tempo que a torneira ficará ligada: "))
            caixa.abrir_torneira(torneira_nome, torneira_tempo)

        elif func == 3:
            caixa.recarregar_reservatorio()

        elif func == 4:
            caixa.imprimir_nome_torneiras()

        elif func == 5:
            torneira_posicao = bool(input("A torneira irá encher ou esvaziar? (True/False): "))
            torneira_nome = input("Digite o nome da torneira: ")
            caixa.remover_torneira(torneira_nome, torneira_posicao)

        elif func == 6:
            caixa.calcular_tempo_esvaziamento()

        elif func == 7:
            caixa.atualizar_torneira()

        elif func == 8:
            exit()

while True:
    inputs_especiais()