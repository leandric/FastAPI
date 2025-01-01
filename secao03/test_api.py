import pytest
from fastapi.testclient import TestClient
from main import app

# Inicializando o cliente de teste
client = TestClient(app)

def test_get_cursos():
    response = client.get("/cursos")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_curso_success():
    response = client.get("/cursos/1")
    assert response.status_code == 200
    assert response.json() == {"1": {
        "titulo": "Programação para leigos",
        "aulas": 112,
        "horas": 58
    }}

def test_get_curso_not_found():
    response = client.get("/cursos/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Curso não encontrado"

def test_post_curso():
    novo_curso = {
        "titulo": "Novo Curso",
        "aulas": 30,
        "horas": 15
    }
    response = client.post("/cursos", json=novo_curso)
    assert response.status_code == 201
    assert response.json() == novo_curso

def test_put_curso_success():
    curso_atualizado = {
        "titulo": "Curso Atualizado",
        "aulas": 45,
        "horas": 20
    }
    response = client.put("/cursos/1", json=curso_atualizado)
    assert response.status_code == 202
    assert response.json() == curso_atualizado

def test_put_curso_not_found():
    curso_atualizado = {
        "titulo": "Curso Inexistente",
        "aulas": 10,
        "horas": 5
    }
    response = client.put("/cursos/999", json=curso_atualizado)
    assert response.status_code == 404
    assert response.json()["detail"] == "ID de curso não existe"

def test_delete_curso_success():
    response = client.delete("/cursos/1")
    assert response.status_code == 202
    assert "1" not in response.json()

def test_delete_curso_not_found():
    response = client.delete("/cursos/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Curso não existe"

def test_calculadora():
    response = client.get("/calculadora?a=10&b=20&c=30", headers={"x-geek": "FastAPI"})
    assert response.status_code == 202
    assert response.json() == {"soma": 60}

@pytest.mark.parametrize("a,b,c,expected_status,expected_result", [
    (6, 11, 3, 202, {"soma": 20}),
    (5, 11, 3, 422, None),  # a menor que o valor mínimo
    (6, 9, 3, 422, None)    # b menor que o valor mínimo
])
def test_calculadora_parametrized(a, b, c, expected_status, expected_result):
    response = client.get(f"/calculadora?a={a}&b={b}&c={c}")
    assert response.status_code == expected_status
    if expected_status == 202:
        assert response.json() == expected_result
