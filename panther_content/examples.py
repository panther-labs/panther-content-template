from panther_config import detection
from panther_utils import match_filters

# create a single rule
inbound_ssh_attempts = detection.Rule(
    rule_id="Content.Example.AWS.ALB.SSH.Incoming",
    name="[Example] AWS ALB Incoming SSH",
    severity=detection.SeverityInfo,
    log_types=["AWS.ALB"],
    filters=[match_filters.deep_equal("targetPort", 22)],
)


# dynamically generate rules off config data
vulnerable_ports = {
    "FTP": [20, 21],
    "SMB": [139, 137, 445],
    "DNS": [53],
}

for key in vulnerable_ports:
    ports = vulnerable_ports[key]

    detection.Rule(
        rule_id=f"Content.Example.AWS.ALB.f{key}.Incoming",
        name="[Example] AWS ALB Incoming SSH",
        severity=detection.SeverityInfo,
        log_types=["AWS.ALB"],
        filters=[match_filters.deep_in("targetPort", ports)],
    )


# install a Panther provided detection with optional overrides
import panther_okta as okta

okta.rules.api_key_created(
    detection.RuleOptions(
        reference="https://example.com/wiki/How_to_respond_to_okta_rules_created"
    )
)
