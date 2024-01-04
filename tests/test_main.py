from src.livro import Livro
from src.solicitante import Solicitante
import pytest 

@pytest.fixture
def livro ():
    return Livro("harry poter","ficcao",True)

@pytest.fixture
def solicitante ():
    return Solicitante("Leonardo")
class TestLivro:
    def test_tipo_livro(livro):
        if livro is type(Livro):
            assert True
            
    def test_livro_disp(livro):
        assert livro == livro
        
class TestSolicitante:
    def test_valida_solicitante(solicitante):
        soli = Solicitante("Leonardo")
        assert soli.nome == "Leonardo"