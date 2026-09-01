import unittest

from src.sepsis.supervisor import classify_question


class SupervisorTests(unittest.TestCase):
    def test_certified_question_uses_certified_route(self):
        result = classify_question("Show a certified sepsis answer")

        self.assertEqual(result["route"], "CERTIFIED_QA")
        self.assertGreaterEqual(result["confidence"], 0.85)

    def test_other_question_uses_genie_fallback(self):
        result = classify_question("Show the latest sepsis trend")

        self.assertEqual(result["route"], "GENIE")


if __name__ == "__main__":
    unittest.main()