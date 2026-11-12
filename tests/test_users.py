import pytest

@pytest.mark.users
def test_usuario_nombre():
    assert "admin" == "admin"



def test_usuario_password():
    assert "1234" == "1234"


