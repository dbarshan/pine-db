from plan.query_plan import QueryPlan

class SQLParser:
    def parse(self, query: str) -> QueryPlan:
        tokens = query.strip().split()
        command = tokens[0].upper()

        if command in ('EXIT', 'QUIT', '\Q'):
            command = 'EXIT'
        
        if command in ('CLEAR', 'CLS', '\C'):
            command = 'CLEAR'

        return QueryPlan(statement_type=command, raw=query)