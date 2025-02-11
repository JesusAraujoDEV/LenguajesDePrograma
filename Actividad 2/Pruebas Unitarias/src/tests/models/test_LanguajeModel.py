from src.models.LanguajeModel import LanguajeModel

def test_get_languajes_not_none():
    languajes = LanguajeModel.get_languajes()
    assert languajes != None

def test_get_languajes_has_elements():
    languajes = LanguajeModel.get_languajes()
    assert len(languajes) > 0

def test_get_languajes_check_elements_length():
    languajes = LanguajeModel.get_languajes()
    for languaje in languajes:
        assert len(languaje) > 0