class Item:

    def __init__(self, nome: str, codigo: int, quantidade: int):
        self.nome = nome
        self.codigo = codigo
        self.quantidade = 0
        self.alterar_quantidade(quantidade)

    def alterar_quantidade(self, quantidade_modificada):
        if self.quantidade > quantidade_modificada*-1:
            self.quantidade += quantidade_modificada
            return True 
        return False

class Estoque:

    def __init__(self):
      pass  

    def cadastrar_item(self, nome: str, codigo: int, quantidade: int):
        for item in self.lista_itens:
            if item.codigo == codigo:
                return  False
            
            novo_item = Item(nome, codigo, quantidade)
            self.lista_itens.append(novo_item)
            return True

    def remover_item(self, codigo: int):
        for item in self.lista_itens:
            if item.codigo == codigo:
                self.lista_itens.remove(item)
                return True
        return False

    def alterar_quantidade_intem(self, codigo, quantidade_alterada: int):
        for item in self.lista_itens:
           if item.codigo == codigo:
               return item.alterar_quantidade(quantidade_alterada)
        return False

class GerenciadorEstoque:

    def __init__(self):
        self.estoque = Estoque()

    def imprimir_commandos(self):
#        os.system("cls")
        print("1 - Cadastrar item")
        print("2 - Remover item")
        print("3 - Alterar quantidade do item")
        print("")

    def main(self):
        self.imprimir_commandos()
        opcao = int(input("Digite uma opção acima"))
        while opcao in [1, 2, 3]:
            if opcao == 1:
                nome = input("Digite um nome")
                codigo = input("Digite um código")
                quantidade = input("Digite uma quantidade")
                resultado = self.estoque.cadastrar_item(nome, codigo, quantidade)
                if resultado:
                    print("O código digitado já está em uso")
                else:
                    print("Produto cadastrado com sucesso")
            elif opcao == 2:
                pass
            elif opcao == 3:
                pass

            self.imprimir_commandos()
            opcao = int(input("Digite uma opção acima"))

if __name__ == "__main__":
    g = GerenciadorEstoque()
    g.main()