from . import rules as local_rules
from . import filters as local_filters

from panther_sdk import detection
import panther_okta as okta

# install a Panther provided detection with optional overrides
okta_api_key_created = okta.rules.api_key_created(
    pre_filters=[
        local_filters.always_true(),
    ],
    overrides=detection.RuleOverrides(
        reference="https://example.com/wiki/How_to_respond_to_okta_rules_created"
    ),
)


# create rules using port name -> numbers mapping
vulnerable_port_rules = local_rules.for_vulnerable_ports(
    {
        "FTP": [20, 21],
        "SMB": [139, 137, 445],
        "DNS": [53],
    }
)
