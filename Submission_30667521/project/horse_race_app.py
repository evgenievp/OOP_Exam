from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        h = self.__find_horse(horse_name)
        if h is not None:
            raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type == "Appaloosa":
            horse = Appaloosa(horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."
        elif horse_type == "Thoroughbred":
            horse = Thoroughbred(horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jo = self.__find_jockey(jockey_name)
        if jo is not None:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        r = self.__find_race(race_type)
        if r is not None:
            raise Exception(f"Race {race_type} has been already created!")
        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jo = self.__find_jockey(jockey_name)
        if jo is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        ho = self.__find_last_horse_of_given_type(horse_type)
        if ho is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jo.horse is not None:
            return f"Jockey {jockey_name} already has a horse."
        jo.horse = ho
        return f"Jockey {jockey_name} will ride the horse {ho.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__find_race(race_type)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")
        jockey = self.__find_jockey(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey is not None and jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if self.__find_jockey_in_race(jockey_name, race):
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__find_race(race_type)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = self.__find_winner(race)
        speed = winner.horse.speed
        return f"The winner of the {race_type} race, with a speed of \
{speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."

    def __find_horse(self, horse_name):
        for horse in self.horses:
            if horse.name == horse_name:
                return horse
        return None

    def __find_jockey(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        return None

    def __find_race(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        return None

    def __find_last_horse_of_given_type(self, horse_type):
        for horse in self.horses:
            if horse.__class__.__name__ == horse_type:
                return horse
        return None

    def __find_jockey_in_race(self, jockey_name, race):
        for jockey in race.jockeys:
            if jockey.name == jockey_name:
                return jockey
        return None

    def __find_winner(self, race):
        top_speed = 0
        jo = ''
        for jockey in race.jockeys:
            if jockey.horse.speed > top_speed:
                jo = jockey
                top_speed = jockey.horse.speed
        return jo


horseRaceApp = HorseRaceApp()
print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
print(horseRaceApp.add_jockey("Peter", 19))
print(horseRaceApp.add_jockey("Mariya", 21))
print(horseRaceApp.create_horse_race("Summer"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.start_horse_race("Summer"))

