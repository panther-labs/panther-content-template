from panther_config import detection
import unittest

from panther_content import examples


class TestExamples(unittest.TestCase):
    def test_example_detection(self) -> None:
        self.assertIsInstance(examples.inbound_ssh_attempts, detection.Rule)
