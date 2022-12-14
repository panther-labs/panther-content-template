from panther_sdk import detection
import unittest

from panther_content.rules import examples


class TestExampleRules(unittest.TestCase):
    def test_inbound_ssh_attempts(self) -> None:
        self.assertIsInstance(examples.inbound_ssh_attempts(), detection.Rule)

    def test_for_vulnerable_ports(self) -> None:
        rules = examples.for_vulnerable_ports(
            {
                "x": [1, 2],
                "y": [3],
            }
        )

        self.assertEqual(len(rules), 2)

        self.assertEqual(rules[0].rule_id, "Content.Example.AWS.ALB.x.Incoming")
        self.assertEqual(rules[1].rule_id, "Content.Example.AWS.ALB.y.Incoming")
