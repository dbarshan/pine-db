from plan.query_plan import QueryPlan
from storage.text_engine import TextStorageEngine
from models.result_set import ResultSet

class ExecutionEngine:
    def __init__(self):
        self.engine = TextStorageEngine()

    def execute(self, plan: QueryPlan) -> ResultSet:
        if plan.statement_type == "CREATE":
            return self.engine.create_table(plan.table_name, plan.columns)
        elif plan.statement_type == "INSERT":
            return self.engine.insert(plan.table_name, plan.values)
        elif plan.statement_type == "SELECT":
            return self.engine.select(plan.table_name, plan.columns, plan.conditions)
        else:
            raise NotImplementedError(f"Unsupported SQL statement: {plan.statement_type}")