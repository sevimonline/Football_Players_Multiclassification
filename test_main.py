from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "Position Predictor" in response.text

def test_position_predict():
    payload = {
        "Positioning": 80.0,
        "Acceleration": 75.0,
        "Sprint_Speed": 78.0,
        "Finishing": 85.0,
        "Shot_Power": 88.0,
        "Long_Shots": 82.0,
        "Volleys": 79.0,
        "Penalties": 87.0,
        "Vision": 88.0,
        "Crossing": 75.0,
        "Free_Kick_Accuracy": 80.0,
        "Shot_Passing": 85.0,
        "Long_Passing": 83.0,
        "Curve": 78.0,
        "Agility": 80.0,
        "Balance": 82.0,
        "Reactions": 85.0,
        "Ball_Control": 87.0,
        "Detailed_Dribbling": 88.0,
        "Composure": 84.0,
        "Interception": 70.0,
        "Heading_Accuracy": 75.0,
        "Def_Awareness": 80.0,
        "Standing_Tackle": 77.0,
        "Sliding_Tackle": 75.0,
        "Jumping": 80.0,
        "Stamina": 82.0,
        "Strength": 84.0,
        "Aggression": 78.0,
        "Age": 28,
        "Att_Work_Rate": "Medium",
        "Def_Work_Rate": "High",
        "Foot": "Right",
    }

    response = client.post("/position_predict", data=payload)
    assert response.status_code == 200
    assert "Prediction Result" in response.text
