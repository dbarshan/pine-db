class ResultSet:
    def __init__(self, rows):
        self.rows = rows

    def __str__(self):
        if isinstance(self.rows, str):
            return self.rows
        return "\n".join([" | ".join(row) for row in self.rows])