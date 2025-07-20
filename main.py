### main.py
from cli.repl import SQLShell

if __name__ == '__main__':
    shell = SQLShell()
    shell.start()

# ### models/table_schema.py
# class TableSchema:
#     def __init__(self, table_name: str, columns: list[list[str]]):
#         self.table_name = table_name
#         self.columns = columns

#     def to_dict(self):
#         return {"table_name": self.table_name, "columns": self.columns}


# ### models/result_set.py
# class ResultSet:
#     def __init__(self, rows):
#         self.rows = rows

#     def __str__(self):
#         if isinstance(self.rows, str):
#             return self.rows
#         return "\n".join([" | ".join(row) for row in self.rows])


# ### execution/condition.py
# class Condition:
#     def __init__(self, col: str, op: str, val: str):
#         self.col = col
#         self.op = op
#         self.val = val

#     def evaluate(self, row: dict[str, any]) -> bool:
#         left = row[self.col]
#         right = self.val
#         return eval(f"{left} {self.op} {right}")
