from src.livro import Livro
from src.solicitante import Solicitante
import pytest 

@pytest.fixture
def livro ():
    return Livro("harry poter","ficcao",True)

@pytest.fixture
def solicitante ():
    return Solicitante("Leonardo")
#testes unitarios
class TestLivro:
    def test_tipo_livro(self,livro):
        if livro is type(Livro):
            assert True
            assert livro.disponivel == True
            
    def test_livro_disp(self,livro):
        assert livro.categoria == livro.categoria
        
class TestSolicitante:
    def test_valida_solicitante(self,solicitante):
        assert solicitante.nome == "Leonardo"
    
    