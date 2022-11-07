from panther_sdk import query
import unittest

from panther_content.queries import examples


class TestExampleQueries(unittest.TestCase):
    def test_select_one(self) -> None:
        self.assertIsInstance(examples.select_one(), query.Query)
