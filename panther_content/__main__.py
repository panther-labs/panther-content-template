from panther_detections.providers import crowdstrike

from panther_content import custom, panther_managed

## CUSTOM

# create rules using port name -> numbers mapping
vulnerable_port_rules = custom.rules.for_vulnerable_ports(
    {
        "FTP": [20, 21],
        "SMB": [139, 137, 445],
        "DNS": [53],
    }
)
custom.rules.inbound_ssh_attempts()

custom.queries.select_one()

custom.data_models.aws_alb()


## PANTHER MANAGED

panther_managed.okta.use_panther_rules()
panther_managed.okta.use_panther_queries()

crowdstrike.use_all_with_defaults()
