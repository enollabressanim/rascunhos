class Livro:

    def __init__(self, titulo: str, autor: str, estado: str, emprestado: bool, assunto: str):
        self.titulo = titulo
        self.autor = autor
        self.estado =  estado
        self.emprestado = emprestado
        self.assunto = assunto

class CadastroLivro:

    def __init__(self):
        self.lista_livros = []
    
    def cadastrar_livros(self, titulo: str, autor: str, estado: str, emprestado: bool, assunto: str):
        for livro in self.lista_livros:
            if livro.titulo == titulo:
                print("entrou aqui")
                return False
            novo_livro = livro(titulo, autor, estado, emprestado, assunto)
            self.lista_livros.append(novo_livro)
            print("agora entrou aqui")
    
    def remover_livro(self, titulo: str):
        for livro in self.lista_livros:
            if livro.titulo == titulo:
                self.lista_livros.remove(livro)
                return True
            return False

    def imprimir_livros(self):
        for livro in self.lista_livros:
            print(livro)

class GerenciadorSistema:

    def __init__(self):
        self.cadastro = CadastroLivro()

    def mostrar_alternativas(self):
        print("1 - Cadastrar livro.")
        print("2 - Remover livro.")
        print("3 - Atualizar informações de um livro.")
        print("4 - Buscar livros por autor.")

    def main(self):
        self.mostrar_alternativas()
        alternativa = int(input("Digite a opção desejada: "))
        while alternativa in [1, 2, 3, 4]:
            if alternativa == 1:
                titulo = input("Titulo: ")
                autor = input("Autor ")
                estado = input("Estado de consevação? (bom/ruim) ")
                emprestado = input("Está sendo emprestado? (s/n) ")
                assunto =   input("Assunto: ")
                resultado = self.cadastro.cadastrar_livros(titulo, autor, estado, emprestado, assunto)
                a = CadastroLivro()
                a.imprimir_livros()
                if resultado is None:
                    print("Livro cadastrado com sucesso!")
                else: 
                    print("O livro já possui cadastro!")
            
            elif alternativa == 2:
                titulo = input("Digite o titulo do livro que desejas remover do sistema: ")
                resultado = self.cadastro.remover_livro(titulo)
                if resultado:
                    print("Livro removido com sucesso!")
                else: 
                    print("O livro não possui cadastro!")
            
            elif alternativa == 3:
                pass
            
            elif alternativa == 4:
                pass
            self.mostrar_alternativas()
            alternativa = int(input("Digite a opção desejada: "))
           

if __name__ == "__main__":
    g = GerenciadorSistema()
    g.main()
