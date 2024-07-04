class Vector2:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        pass

    def get(self):
        return (self.x, self.y)
