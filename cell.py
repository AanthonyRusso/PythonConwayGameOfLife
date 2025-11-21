class Cell:
    def __init__(self, is_alive=False):
        self.is_alive = is_alive
    def __str__(self):
        return f"Cell({self.is_alive})"
    def __repr__(self):
        return f"Cell({self.is_alive})"