from panther_sdk import detection, PantherEvent
import panther_okta as okta

# a python method that always returns True
def always_true(_: PantherEvent) -> bool:
    return True


# Example Rule, My.Example.Rule
always_true_detection = detection.Rule(
    rule_id="My.Example.Rule",
    enabled=False,
    severity=detection.SeverityInfo,
    log_types=["AWS.CloudTrail"],
    filters=[detection.PythonFilter(func=always_true)],
)

# Step 4: Write Your Rule Here


# Example rule that relies on panther-provided content, but with a custom reference
okta_api_key_created = okta.rules.api_key_created(
    overrides=detection.RuleOptions(
        reference="https://example.com/wiki/How_to_respond_to_okta_rules_created"
    ),
)

# Step 6: Write customized okta detection
