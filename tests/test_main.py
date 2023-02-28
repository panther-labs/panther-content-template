import typing
import unittest

from panther_content.__main__ import vulnerable_port_rules


class TestMain(unittest.TestCase):
    def test_vulnerable_port_rules(self) -> None:
        self.assertIsInstance(vulnerable_port_rules, typing.List)
        self.assertEqual(len(vulnerable_port_rules), 3)
