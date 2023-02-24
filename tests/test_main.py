import unittest

from panther_content.__main__ import always_true


class TestMain(unittest.TestCase):
    def test_always_true(self) -> None:
        self.assertTrue(always_true({}), True)
