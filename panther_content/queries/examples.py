from panther_sdk import query


# create a saved query
def select_one(enabled: bool = True) -> query.Query:
    return query.Query(
        name="Example Query",
        sql="SELECT 1;",
        enabled=enabled,
        schedule=None,
        description="Selects the number 1",
        tags=["example"],
    )
