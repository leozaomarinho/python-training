class Livro:
    def __init__(self,nome,categoria, disponivel):
        self.nome = nome 
        self.categoria = categoria
        self.disponivel = disponivel
        
    def __str__(self) -> str:
        disponibilidade = {'Disponível' if self.disponivel else 'Indisponível'}
        return f'Nome : {self.nome} - Categoria: {self.categoria} - Disponibilidade: {disponibilidade}'