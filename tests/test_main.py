import typing
import unittest

from panther_content.__main__ import always_true, always_true_detection
from panther_sdk import detection

class TestMain(unittest.TestCase):
    def test_okta_api_key_created(self) -> None:
        self.assertIsInstance(always_true_detection, detection.Rule)

    def test_always_true(self) -> None:
        self.assertTrue(always_true({}), True)
