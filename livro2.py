'''class Livros:
    def __init__(self, titulo: str, autor: str, estado: str, emprestado: bool, assunto: str):
        self.titulo = titulo
        self.autor = autor
        self.estado =  estado
        self.emprestado = emprestado
        self.assunto = assunto'''
        
class GerenciadorLivrosInterfaceTexto:
    def __init__(self, titulo: str, autor: str, estado: str, emprestado: bool, assunto: str):
        titulo = input("Informe o título do livro: ")
        autor = input("Autor: ")
        estado = input("Estado de conservação?(bom/ruim) ")
        espretado = input("Está emprestado?(s/n) ")
        assunto = input("Qual o assunto o livro? ")
        if buscar_titulo(titulo) is None:
            if situacao == "s":
                situacao = True
            else:
                situacao = False
            livro = {
                #self.titulo = titulo
                self.autor = autor
                self.estado =  estado
                self.emprestado = emprestado
                self.assunto = assunto}
            __init__.append(livro)
    
    def buscar_titulo(titulo: str):
        for livro in __init__:
                if livro["nome"] == nome:
                    return livro
        return None
'''        
    def cadastrar_livro(titulo:str, autor:str, estado:str, emprestado:bool, assunto:str ):
    pass
'''
    def remover_livro():
    pass

    def atualizar_livro(titulo:str, autor:str, estado:str, emprestado:bool, assunto:str):
    pass

    def buscar_autor(autor:str):
    pass

    def gravar_dados(arquivo:str):
    pass

    def recuperar_dados(arquivo:str):
    pass

    def imprimir_menu():
    