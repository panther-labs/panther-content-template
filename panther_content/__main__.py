import panther_okta as okta
from panther_config import detection

from . import filters as local_filters

# install a Panther provided detection with optional overrides
okta_api_key_created = okta.rules.api_key_created(
    pre_filters=[
        local_filters.always_true(),
    ],
    overrides=detection.RuleOptions(
        reference="https://example.com/wiki/How_to_respond_to_okta_rules_created"
    ),
)
