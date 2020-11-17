class Filme():
    
    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor
    
    def __str__(self):
        return self.titulo + ' - ' + self.diretor
    
    def __eq__(self, outro_filme):
        return self.titulo == outro_filme.titulo

def pega_todos_os_filmes():
    ## implementação da função
    meus_filmes = pega_todos_os_filmes()
    for filme in meus_filmes:
        print(filme)

def tenho_o_filme(filme_procurado):
    meus_filmes = pega_todos_os_filmes()
    return filme_procurado in meus_filmes

filme_procurado = Filme('A Teoria de Tudo', 'James Marsh')

if tenho_o_filme(filme_procurado):
    print('Tenho o filme!')
else:
    print('Não tenho :(')


