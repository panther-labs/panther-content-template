from typing import List

from panther_detections.providers import okta
from panther_sdk import query


def use_panther_queries() -> List[query.Query]:
    return [
        okta.queries.activity_audit(
            datalake="snowflake",
            overrides=query.QueryOverrides(name="Activity Audit with Override"),
        ),
        okta.queries.session_id_audit(
            datalake="athena",
            extensions=query.QueryExtensions(tags=["another_tag"]),
        ),
    ]
