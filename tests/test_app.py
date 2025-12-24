import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    activity = list(client.get("/activities").json().keys())[0]
    email = "testuser@mergington.edu"
    # Sign up
    signup = client.post(f"/activities/{activity}/signup?email={email}")
    assert signup.status_code == 200
    # Unregister
    unregister = client.post(f"/activities/{activity}/unregister?email={email}")
    assert unregister.status_code == 200
