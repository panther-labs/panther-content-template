from typing import List

from panther_detections.providers import okta
from panther_sdk import detection

from panther_content.custom import filters as custom_filters


def use_panther_rules() -> List[detection.Rule]:
    return [
        okta.rules.admin_disabled_mfa(),
        okta.rules.api_key_created(
            overrides=detection.RuleOverrides(name="Api Keys Override"),
        ),
        okta.rules.brute_force_logins(
            overrides=detection.RuleOverrides(description="A new description."),
            extensions=detection.RuleExtensions(filters=[custom_filters.always_true()]),
        ),
    ]
