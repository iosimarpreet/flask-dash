
class Cat:
    def __init__(self, name):
        self.name = name
        self.age = 4

    def birthday(self):
        self.age = self.age + 1

    def meow(self):
        return f"Hello world! I am {self.name} Cat."
