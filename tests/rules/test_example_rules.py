import unittest

from panther_sdk import detection

from panther_content import custom


class TestExampleRules(unittest.TestCase):
    def test_inbound_ssh_attempts(self) -> None:
        ssh_attempts_rule = custom.rules.inbound_ssh_attempts()
        self.assertEqual(
            ssh_attempts_rule.rule_id, "Content.Example.AWS.ALB.SSH.Incoming"
        )

    def test_for_vulnerable_ports(self) -> None:
        rules = custom.rules.for_vulnerable_ports(
            {
                "x": [1, 2],
                "y": [3],
            }
        )

        self.assertEqual(len(rules), 2)

        self.assertEqual(rules[0].rule_id, "Content.Example.AWS.ALB.x.Incoming")
        self.assertEqual(rules[1].rule_id, "Content.Example.AWS.ALB.y.Incoming")
