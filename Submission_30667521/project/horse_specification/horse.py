from abc import abstractmethod, ABC


class Horse(ABC):
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "" or len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if self.__class__.__name__ == "Appaloosa" and value > 120:
            raise ValueError("Horse speed is too high!")
        elif self.__class__.__name__ == "Thoroughbred" and value > 140:
            raise ValueError(f"Horse speed is too high!")
        self.__speed = value

    @abstractmethod
    def train(self):
        pass

