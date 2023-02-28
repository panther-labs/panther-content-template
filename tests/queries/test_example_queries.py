import unittest

from panther_sdk import query

from panther_content import custom


class TestExampleQueries(unittest.TestCase):
    def test_select_one(self) -> None:
        select_one_query = custom.queries.select_one()
        self.assertEqual(select_one_query.name, "Example Query")
