class Livro:
    def __init__(self,nome,categoria, disponivel):
        self.nome = nome 
        self.categoria = categoria
        self.disponivel = disponivel
        
    def __str__(self) -> str:
        return f'{self.nome} - {self.categoria} -({'Disponível' if self.disponivel else 'Indisponível'})'