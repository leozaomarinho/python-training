from src.livro import Livro
import pytest 

@pytest.fixture
def livro ():
    return Livro("harry poter","ficcao",True)

def test_livro(livro):
    if livro is type(Livro):
        assert True