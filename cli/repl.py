from parser.parser import SQLParser
from execution.executor import ExecutionEngine
from models.result_set import ResultSet
import os

class SQLShell:
    def __init__(self):
        self.parser = SQLParser()
        self.executor = ExecutionEngine()

    def start(self):
        print("Welcome to PineDB. Type your SQL commands below.")
        while True:
            try:
                query = input("pine> ")
                plan = self.parser.parse(query)
                if plan.statement_type == "CLEAR":
                    os.system('cls' if os.name == 'nt' else 'clear')
                elif plan.statement_type == "EXIT":
                    break
                else:
                    result: ResultSet = self.executor.execute(plan)
                    print(result)

            except Exception as e:
                print(f"Error: {e}")