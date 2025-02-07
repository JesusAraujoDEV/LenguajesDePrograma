import pytest
from src.main import es_mayor, suma, login, fibonacci


def test_suma():
    assert suma(1, 2) == 3 #assert es una palabra reservada, que se utiliza para hacer pruebas y verifica si la tendencia siguiente es correcta

def test_es_mayor():
    assert es_mayor(2, 1)


#Creamos un test parametrizado, que nos permite ejecutar el mismo test con diferentes parametros
@pytest.mark.parametrize(
        "x,y,esperado", [(1,2,3), (2,1,3), (3,3,6), (suma(1,2),3,6)]
)
def test_suma_parametros(x,y,esperado):
    assert suma(x,y) == esperado

def test_login_pass():
    login_passes = login("admin", "1234")
    assert login_passes

#Test de prueba que deberia de fallar
def test_login_fail():
    login_fails = login("adminXD", "123☠🤑")
    assert not login_fails

def test_fibonacci():
    assert fibonacci(5) == 5