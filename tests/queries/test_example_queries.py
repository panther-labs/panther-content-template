import unittest

from panther_content.queries import examples


class TestExampleQueries(unittest.TestCase):
    def test_select_one(self) -> None:
        my_query = examples.select_one()
        self.assertEqual(my_query.name, "Example Query")
