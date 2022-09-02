import typing
import unittest

from panther_config import detection
from panther_content.__main__ import okta_api_key_created, vulnerable_port_rules


class TestMain(unittest.TestCase):
    def test_okta_api_key_created(self) -> None:
        self.assertIsInstance(okta_api_key_created, detection.Rule)

    def test_vulnerable_port_rules(self) -> None:
        self.assertIsInstance(vulnerable_port_rules, typing.List[detection.Rule])
        self.assertEqual(len(vulnerable_port_rules), 3)
