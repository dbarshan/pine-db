import os
import json
from storage.base import StorageEngine
from models.table_schema import TableSchema
from models.result_set import ResultSet

DATA_DIR = "./data"

class TextStorageEngine(StorageEngine):
    def create_table(self, query: str) -> ResultSet:
        # This is a simplified example parser, just for demo
        # CREATE TABLE employees (id INT, name TEXT)
        table_name = query.split()[2]
        columns = query.split("(")[1].split(")")[0].split(",")
        cols = [col.strip().split() for col in columns]
        schema = TableSchema(table_name, cols)

        os.makedirs(os.path.join(DATA_DIR, table_name), exist_ok=True)
        with open(os.path.join(DATA_DIR, table_name, "meta.json"), "w") as f:
            json.dump(schema.to_dict(), f)
        return ResultSet(f"Table '{table_name}' created.")

    def insert(self, query: str) -> ResultSet:
        # INSERT INTO employees VALUES (1, 'Alice')
        table_name = query.split()[2]
        values = query.split("VALUES")[1].strip(" ()\n").split(",")
        table_path = os.path.join(DATA_DIR, table_name)
        with open(os.path.join(table_path, "meta.json")) as f:
            schema = json.load(f)
        for i, col in enumerate(schema['columns']):
            col_path = os.path.join(table_path, f"{col[0]}.txt")
            with open(col_path, "a") as f:                
                f.write(values[i].strip(" '\"") + "\n")
        return ResultSet("Row inserted.")

    def select(self, query: str) -> ResultSet:
        # SELECT id, name FROM employees
        tokens = query.split()
        cols = tokens[1].split(",")
        table_name = tokens[3]
        table_path = os.path.join(DATA_DIR, table_name)
        data = {}
        for col in cols:
            with open(os.path.join(table_path, f"{col}.txt")) as f:
                data[col] = f.read().splitlines()
        result = []
        for i in range(len(data[cols[0]])):
            row = [data[col][i] for col in cols]
            result.append(row)
        return ResultSet(result)