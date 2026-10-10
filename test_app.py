
import unittest
from app import app

class StudentAppTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_status(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_student_data(self):
        response = self.client.get("/")
        data = response.get_json()
        self.assertIn("students", data)
        self.assertEqual(len(data["students"]), 2)

if __name__ == "__main__":
    unittest.main()