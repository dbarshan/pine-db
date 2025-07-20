# PineDB
*A Modular Columnar SQL Database Engine*

---

## 📌 1. Objective

To design and implement a modular, columnar SQL-based database engine that starts with simple text-based storage and can be progressively extended to support advanced features like binary storage, indexing (B+ Trees), and optimized execution engines.

---

## 📌 2. Scope – Phase 1 (MVP)

This phase focuses on:

* A **columnar storage engine** using flat text files.
* A **basic SQL parser** to handle standard SQL commands.
* A **modular architecture** allowing easy upgrade of storage and indexing.
* Support for simple **DDL** and **DML** operations.

---

## 📌 3. Functional Requirements

### 3.1 Storage Engine

* Store each column of a table in a **separate text file**.
* File format: CSV or line-separated raw values.
* Metadata (schema, table definition) stored in a JSON or meta file.
* Tables and columns should be discoverable via metadata.
* All data is persisted in a designated **data directory**.

### 3.2 SQL Query Parser

* Custom-built SQL parser or using a parser library (like ANTLR).
* Accept basic **SQL statements**:

  * `CREATE TABLE`
  * `INSERT INTO`
  * `SELECT ... FROM ... WHERE`
  * `DELETE FROM`
  * `DROP TABLE`
* Parser should convert SQL queries into an internal AST or query plan format.

### 3.3 Execution Engine

* Executes parsed queries using in-memory or file-streamed approach.
* Simple row construction from columnar files for select queries.
* Where clause evaluation should support basic conditions (`=, >, <, AND, OR`).

### 3.4 Modularity

* All major components (Parser, Storage, Executor) should be modular interfaces:

  * Pluggable storage engines
  * Pluggable index/optimizer in future
  * Clear abstraction boundaries

### 3.5 CLI Interface

* A command-line SQL shell to input and run queries.
* Support for multi-line query input and output formatting.

---

## 📌 4. Non-Functional Requirements

| Category         | Description                                                                      |
| ---------------- | -------------------------------------------------------------------------------- |
| 🔧 Extensibility | Must be designed to allow addition of binary storage, indexing, query optimizers |
| 💾 Portability   | Must work cross-platform (Windows/Linux/Mac)                                     |
| 🧪 Testability   | Unit and integration testable modules                                            |
| 🔒 Security      | No SQL injection possible in parsing phase                                       |
| 🧠 Simplicity    | Initial codebase should be readable, well-commented, modular                     |
| 📚 Logging       | Basic logging and query audit trail should be present                            |

---

## 📌 5. Phase-Wise Evolution Plan

| Phase   | Description                                             |
| ------- | ------------------------------------------------------- |
| Phase 1 | Columnar text file storage, basic SQL, CLI              |
| Phase 2 | Binary storage format (block files, column compression) |
| Phase 3 | Indexing using B+ Trees or bitmap indexes               |
| Phase 4 | Query optimizer, statistics, cost-based plan            |
| Phase 5 | SQL joins, aggregations, GROUP BY, HAVING               |
| Phase 6 | Multi-threaded execution, cache, transaction log        |

---

## 📌 6. Module Breakdown

### 6.1 Core Modules

* `Parser` → Translates SQL to AST/QueryPlan
* `StorageEngine` → Interface for read/write columnar data
* `ExecutionEngine` → Executes SELECT, INSERT, DELETE etc.
* `MetadataManager` → Manages schema, table definitions
* `FileManager` → Manages underlying file operations

### 6.2 Interfaces & Extensibility

```python
class StorageEngine(ABC):

    @abstractmethod
    def create_table(self, schema: TableSchema) -> None:
        pass

    @abstractmethod
    def insert(self, table_name: str, values: List[str]) -> None:
        pass

    @abstractmethod
    def select(self, table_name: str, columns: List[str], condition: Condition) -> ResultSet:
        pass

```

### 6.3 Data Structures

* `TableSchema`
* `QueryPlan`
* `Row/ColumnData`
* `Condition` (for WHERE clause)

---

## 📌 7. Deliverables (Phase 1)

* ✅ `PineDB` base implementation
* ✅ SQL CLI
* ✅ Support for simple CRUD SQL
* ✅ Columnar file-based storage
* ✅ Test cases for storage, parser, execution
* ✅ Developer documentation

---

## 📌 8. Example Usage

### Input:

```sql
CREATE TABLE employees (id INT, name TEXT, salary FLOAT);

INSERT INTO employees VALUES (1, 'Alice', 85000.0);
INSERT INTO employees VALUES (2, 'Bob', 72000.5);

SELECT id, name FROM employees WHERE salary > 80000;
```

### File Structure:

```
data/
 └── employees/
     ├── id.txt       → 1\n2\n
     ├── name.txt     → Alice\nBob\n
     └── salary.txt   → 85000.0\n72000.5\n
```

---

## 📌 9. Optional Tech Stack (Flexible)

* Language: **Python**
* Parser: Custom or **ANTLR**, **JSqlParser**, **sqlglot**
* Test Framework: JUnit / PyTest
* Logging: SLF4J / Logback

---

## 📌 10. Future Enhancements

* Binary storage (columnar blocks with compression)
* B+ Tree indexes per column
* Cost-based query optimizer
* Distributed file support (S3, HDFS)
* SQL JOIN support
* ACID transactions with write-ahead logging

## Project Structure
```
pinedb/
├── cli/                     # CLI interface
│   └── repl.py              # REPL: interactive SQL shell
├── core/                    # Core orchestrators
│   ├── engine.py            # Entry point to query execution
│   └── context.py           # Query execution context manager
├── parser/                  # SQL parser components
│   ├── parser.py            # SQL to AST parser
│   └── tokenizer.py         # (Optional) SQL tokenizer/lexer
├── plan/                    # AST and logical query plans
│   ├── ast.py               # AST node classes
│   └── query_plan.py        # Logical query plan representations
├── storage/                 # Storage engine modules
│   ├── base.py              # Abstract base class for storage
│   ├── text_engine.py       # Text-based columnar storage engine
│   ├── file_manager.py      # Low-level file I/O operations
│   └── metadata.py          # Table schema & catalog manager
├── execution/               # Query execution logic
│   ├── executor.py          # Query executors for SELECT, INSERT, DELETE
│   ├── condition.py         # WHERE clause evaluation
│   └── row_builder.py       # Reconstruct rows from columnar data
├── models/                  # Shared data models
│   ├── table_schema.py      # Table and column definitions
│   ├── result_set.py        # Query result wrapper
│   └── value.py             # Data type handling
├── tests/                   # Unit and integration tests
│   └── ...
├── logs/                    # Optional runtime logs
├── data/                    # Actual columnar storage (per-table)
└── main.py                  # Application entry point
```
Future plan:
![alt text](https://github.com/dbarshan/pine-db/blob/master/doc/roadmap.png)
