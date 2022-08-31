from . import rules
from panther_config import detection
import panther_okta as okta

# install a Panther provided detection with optional overrides
okta.rules.api_key_created(
    detection.RuleOptions(
        reference="https://example.com/wiki/How_to_respond_to_okta_rules_created"
    )
)


# create rules using port name -> numbers mapping
rules.for_vulnerable_ports(
    {
        "FTP": [20, 21],
        "SMB": [139, 137, 445],
        "DNS": [53],
    }
)
