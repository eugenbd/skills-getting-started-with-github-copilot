class TestSignup:
    def test_signup_valid_student(self, client, reset_activities):
        # Arrange
        activity = "Chess%20Club"
        email = "newstudent@mergington.edu"

        # Act
        response = client.post(f"/activities/{activity}/signup?email={email}")

        # Assert
        assert response.status_code == 200
        assert "Signed up" in response.json()["message"]

    def test_signup_duplicate_registration(self, client, reset_activities):
        # Arrange
        activity = "Chess%20Club"
        email = "michael@mergington.edu"

        # Act
        response_first = client.post(f"/activities/{activity}/signup?email={email}")
        response_second = client.post(f"/activities/{activity}/signup?email={email}")

        # Assert
        assert response_first.status_code == 200
        assert response_second.status_code == 400
        assert "already signed up" in response_second.json()["detail"]

    def test_signup_nonexistent_activity(self, client, reset_activities):
        # Arrange
        activity = "Fake%20Activity"
        email = "student@mergington.edu"

        # Act
        response = client.post(f"/activities/{activity}/signup?email={email}")

        # Assert
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]


class TestUnregister:
    def test_unregister_valid_participant(self, client, reset_activities):
        # Arrange
        activity = "Chess%20Club"
        email = "michael@mergington.edu"

        # Act
        response = client.delete(f"/activities/{activity}/unregister?email={email}")

        # Assert
        assert response.status_code == 200
        assert "Unregistered" in response.json()["message"]

    def test_unregister_nonexistent_participant(self, client, reset_activities):
        # Arrange
        activity = "Chess%20Club"
        email = "notregistered@mergington.edu"

        # Act
        response = client.delete(f"/activities/{activity}/unregister?email={email}")

        # Assert
        assert response.status_code == 400
        assert "not signed up" in response.json()["detail"]

    def test_unregister_nonexistent_activity(self, client, reset_activities):
        # Arrange
        activity = "Fake%20Activity"
        email = "student@mergington.edu"

        # Act
        response = client.delete(f"/activities/{activity}/unregister?email={email}")

        # Assert
        assert response.status_code == 404
        assert "not found" in response.json()["detail"]
