from panther_detections.providers import crowdstrike


def use_panther_rules() -> None:
    crowdstrike.use_all_with_defaults()
