import os.path

class Livro():
    
    def __init__(self, titulo: str, autor: str, estado: str, emprestado: bool, assunto: str, arq: str):
        self.titulo = titulo
        self.autor = autor
        self.assunto = assunto
        self.estado =  estado
        self.emprestado = emprestado
        self.arq = arq

class CadastroLivro():

    def __init__(self):
        self.lista = []

    def cadastrar_livros(self, titulo: Livro, autor: Livro, estado: Livro, emprestado: Livro, assunto: Livro, arq: Livro):
        livros = Livro(titulo, autor, assunto, estado, emprestado, arq)
        self.lista.append(livros)

        if(os.path.isfile(arq)):
            print("O arquivo existe")
        else:
            print("O arquivo não existe")

        try:
            arquivo = open(arq, 'a')
            arquivo.write(self.lista)
            arquivo.close()
        except:
            print('O arquivo não existe!')

class SistemaLivros():
    def mostrar_alternativas(self):
        print("1 - Cadastrar livro.")
        print("2 - Remover livro.")
        print("3 - Atualizar informações de um livro.")
        print("4 - Buscar livros por autor.")

    def main(self, titulo: Livro, autor: Livro, estado: Livro, emprestado: Livro, assunto: Livro, arq: Livro):
        self.mostrar_alternativas()
        alternativa = int(input("Digite a opção desejada: "))
        while alternativa in [1, 2, 3, 4]:
            if alternativa == 1:
                titulo = input("Titulo: ")
                autor = input("Autor ")
                estado = input("Estado de consevação? (bom/ruim) ")
                emprestado = input("Está sendo emprestado? (s/n) ")
                assunto =   input("Assunto: ")
                arq = input("Digite o nome do arquivo: ")
            self.mostrar_alternativas()
            alternativa = int(input("Digite a opção desejada: "))

if __name__ == "__main__":
    g = SistemaLivros()
    g.main()