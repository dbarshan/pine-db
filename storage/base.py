from models.table_schema import TableSchema
from execution.condition import Condition
from models.result_set import ResultSet
from abc import ABC, abstractmethod

class StorageEngine(ABC):
    @abstractmethod
    def create_table(self, schema: TableSchema) -> None:
        pass

    @abstractmethod
    def insert(self, table_name: str, values: list[str]) -> None:
        pass

    @abstractmethod
    def select(self, table_name: str, columns: list[str], condition: Condition | None) -> ResultSet:
        pass