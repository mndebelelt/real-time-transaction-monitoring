class InMemoryStateStore:

    def __init__(self) -> None:
        self.user_transactions = {}
        self.user_countries = {}