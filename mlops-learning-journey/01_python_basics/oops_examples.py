# Python OOP example


class Dog:
    def __init__(self, name: str):
        self.name = name

    def bark(self) -> str:
        return f"{self.name} says woof!"


if __name__ == "__main__":
    dog = Dog("Bruno")
    print(dog.bark())
