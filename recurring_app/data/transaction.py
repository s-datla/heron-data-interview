from datetime import datetime

class Transaction():
    def __init__(self, amount: float, description: str, timestamp: str) -> None:
        self.amount = amount
        self.description = description
        self.timestamp = datetime.fromisoformat(timestamp)