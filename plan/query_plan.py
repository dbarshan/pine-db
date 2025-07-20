import json

class QueryPlan:
    def __init__(self, statement_type: str, raw: str):
        self.statement_type = statement_type
        self.raw_query = raw

    def __str__(self):
        return json.dumps(self.__dict__, indent=2)