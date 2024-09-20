class Settings:
    def __init__(self):
        # name of .csv file in the program's directory, along with the max # of builds you want to output
        self.file_name = "destiny-armor.csv"
        self.max_results = 5

        # Double check spelling, not case-sensitive
        self.exotic = "Sunbracers"
        self.character_class = "Warlock"
        self.primary_stat = "Resilience"
        self.secondary_stat = "Discipline"

        # minimum and maximum values for both primary and secondary stats are inclusive
        self.primary_minimum = 100
        self.primary_maximum = 105
        self.secondary_minimum = 80
        self.secondary_maximum = 85

        # Adjust based on your mods, fragments, and aspects
        self.extra_mobility = 0
        self.extra_resilience = 40
        self.extra_recovery = 3
        self.extra_discipline = 10
        self.extra_intellect = 0
        self.extra_strength = 0
