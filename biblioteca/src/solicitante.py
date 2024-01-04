class Solicitante:
    def __init__(self,nome, nome_livro=None, livro_pend = False):
        self.nome=nome
        self.livro_pend = livro_pend
        self.nome_livro = nome_livro
        
    def __str__(self) -> str:
        disponivel = {'Possui pendencia' if self.livro_pend == True else 'Nao possui pendencia'}
        return f'Solicicitante {self.nome}. livro pendente: {disponivel}'
    
        