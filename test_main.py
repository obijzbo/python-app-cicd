from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_search_movies():
    response = client.post("/", data={"year_of_release": 2022})
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_upload_data():
    response = client.get("/upload_data")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_upload_movie_data_handler():
    data = {
        "movie_name": "Test Movie",
        "year_of_release": 2023,
        "box_office": 1000000.0,
        "director": "Test Director",
        "producer": "Test Producer",
        "cast": "Test Cast"
    }

    response = client.post("/upload_data", data=data)
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

