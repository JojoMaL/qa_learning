import pytest


def login(username, password):
    if username == "admin" and password == "1234":
        return True
    return False


usuarios = []


@pytest.fixture
def usuario_password():
    return ("admin", "1234")


@pytest.fixture
def usuario():
    print("Preparando usuario")
    usuarios.append("admin")
    yield "admin"
    print("Eliminando usuario")
    usuarios.remove("admin")


def test_usuario(usuario):
    print("Ejecutando test")
    assert usuario == "admin"
    print(usuarios)


def test_usuario_password(usuario_password):
    usuario, password = usuario_password
    assert login(usuario, password) == True


@pytest.mark.login
@pytest.mark.parametrize("username, password, expected", [
    ("admin", "1234", True),
    ("admin", "01234", False),
    ("pepe", "1234", False),
    ("", "1234", False),
    ("admin", "", False)
])
def test_login(username, password, expected):
    assert login(username, password) == expected


