import pytest

from app import GYM_METRICS, PROGRAMS, app


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"ACEest FUNCTIONAL FITNESS" in response.data


def test_home_page_contains_all_programs(client):
    response = client.get("/")
    for name in PROGRAMS:
        assert name.encode() in response.data


def test_program_selection(client):
    response = client.get(
        "/?program=Fat%20Loss%20(FL)"
    )
    assert response.status_code == 200
    assert b"5x5 Back Squat" in response.data
    assert b"2,000 kcal" in response.data


@pytest.mark.parametrize(
    "name, workout_text, diet_text",
    [
        (
            "Fat Loss (FL)",
            "5x5 Back Squat",
            "2,000 kcal",
        ),
        (
            "Muscle Gain (MG)",
            "Deadlift 4x6",
            "3,200 kcal",
        ),
        (
            "Beginner (BG)",
            "Circuit Training",
            "120g/day",
        ),
    ],
)
def test_program_api(client, name, workout_text, diet_text):
    response = client.get(
        "/api/programs/" + name.replace(" ", "%20")
    )

    assert response.status_code == 200
    assert response.json["name"] == name
    assert workout_text in response.json["workout"]
    assert diet_text in response.json["diet"]


def test_list_programs(client):
    response = client.get("/api/programs")
    assert response.status_code == 200
    assert set(response.json) == set(PROGRAMS)


def test_unknown_program(client):
    response = client.get("/api/programs/Unknown")
    assert response.status_code == 404
    assert response.json["error"] == "Program not found"


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_gym_metrics():
    assert GYM_METRICS["capacity"] == "150 Users"
    assert GYM_METRICS["area"] == "10,000 sq ft"
    assert GYM_METRICS["break_even"] == "250 Members"
