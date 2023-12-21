from fastapi.testclient import TestClient
from CloudApi import app

allow_redirects=False
client = TestClient(app)


# Тест для api и проверка результата модели
def test_read_CloudApi():
    response = client.post("/answer/", json={"question": "Вопрос", "search_topic": "Контекст"})
    assert response.status_code == 200
    result = response.json()
    assert result['answer'] == "Контекст"
