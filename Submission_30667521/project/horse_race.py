class HorseRace:
    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys = []

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        if value != "Summer" and value != "Winter" and value != "Autumn" and value != "Spring":
            raise ValueError("Race type does not exist!")
        self.__race_type = value
