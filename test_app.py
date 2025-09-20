from app import generar_password

def test_longitud_password():
    pwd = generar_password(12)
    assert len(pwd) == 12

def test_password_minima():
    pwd = generar_password(4)
    assert len(pwd) == 4

def test_error_password_corta():
    try:
        generar_password(2)
    except ValueError as e:
        assert str(e) == "La longitud mínima es 4 caracteres"
