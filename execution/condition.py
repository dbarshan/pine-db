class Condition:
    def __init__(self, col: str, op: str, val: str):
        self.col = col
        self.op = op
        self.val = val

    def evaluate(self, row: dict[str, any]) -> bool:
        left = row[self.col]
        right = self.val
        return eval(f"{left} {self.op} {right}")