from typing import Dict, List

from panther_detections.utils import match_filters
from panther_sdk import detection, schema


# create a single rule
def inbound_ssh_attempts() -> detection.Rule:
    return detection.Rule(
        rule_id="Content.Example.AWS.ALB.SSH.Incoming",
        name="[Example] AWS ALB Incoming SSH",
        severity=detection.SeverityInfo,
        log_types=[schema.LogTypeAWSALB],
        filters=[match_filters.deep_equal("targetPort", 22)],
    )


# dynamically generate rules off config data
def for_vulnerable_ports(config: Dict[str, List[int]]) -> List[detection.Rule]:
    rules = []

    for key in config:
        ports = config[key]

        rules.append(
            detection.Rule(
                rule_id=f"Content.Example.AWS.ALB.{key}.Incoming",
                name="[Example] AWS ALB Incoming SSH",
                severity=detection.SeverityInfo,
                log_types=[schema.LogTypeAWSALB],
                filters=[match_filters.deep_in("targetPort", ports)],
            )
        )

    return rules
