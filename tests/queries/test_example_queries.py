import unittest

from panther_sdk import query

from panther_content import custom


class TestExampleQueries(unittest.TestCase):
    def test_select_one(self) -> None:
        self.assertIsInstance(custom.queries.select_one(), query.Query)
