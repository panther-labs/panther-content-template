from panther_core import PantherEvent
from panther_config import detection
import panther_okta as okta

# a python method that always returns True
def always_true(_: PantherEvent) -> bool:
    return True

# Creates a Rule, My.Example.Rule
always_true_detection = detection.Rule(
    rule_id="My.Example.Rule",
    enabled=False,
    severity=detection.SeverityInfo,
    log_types=["AWS.CloudTrail"],
    filters=[detection.PythonFilter(func=always_true)],
)

# Create another Rule that detects when an AWS.CloudTrail event's field, eventName, is DisassociateWebACL


# Create a rule that relies on panther-provided content, but with a custom reference
okta_api_key_created = okta.rules.api_key_created(
    overrides=detection.RuleOptions(
        reference="https://example.com/wiki/How_to_respond_to_okta_rules_created"
    ),
)

# Explore the available detections in the panther_okta package
#
# Create another rule for the okta api key revoked detection with a custom severity

