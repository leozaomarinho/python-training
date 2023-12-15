class solicitante:
    def __init__(self,nome):
        self.nome=nome
        self.livro_pend = None
        
    def __str__(self) -> str:
        return f'Solicicitante {self.nome}. livro pendente: ({'Possui pendencia' if self.livro_pend == True else 'Nao possui pendencia'})'
        