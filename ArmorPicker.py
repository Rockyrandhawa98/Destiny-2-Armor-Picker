from ArmorSettings import Settings
import numpy as np
import heapq
import csv


class ArmorPicker(Settings):
    def __init__(self):
        # Dictionaries to store "armor names" : [values]
        super().__init__()
        self.Helmets = {}
        self.Gauntlets = {}
        self.Chests = {}
        self.Boots = {}

        indexer = {
            "Mobility": 0,
            "Resilience": 1,
            "Recovery": 2,
            "Discipline": 3,
            "Intellect": 4,
            "Strength": 5
        }

        self.primary_index = indexer[self.primary_stat.title()]
        self.secondary_index = indexer[self.secondary_stat.title()]

        # Assuming class item is Masterwork Quality
        self.class_item = np.array([2, 2, 2, 2, 2, 2])
        self.base = np.array([self.extra_mobility, self.extra_resilience, self.extra_recovery,
                              self.extra_discipline, self.extra_intellect, self.extra_strength])
        self.base_stats = self.class_item + self.base

        self.heap = []
        self.results = []

    def populate_dictionaries(self):
        # Accounting for multiple armor pieces of the same name
        h = 1
        g = 1
        c = 1
        b = 1

        with open(self.file_name, "r") as file:
            reader = csv.reader(file)
            for line in reader:
                if (line[4] == "Legendary" and line[7].lower() == self.character_class.lower()) or \
                        line[0].lower() == self.exotic.lower():

                    # Assuming Masterwork Qualities
                    mobility = int(line[23]) + 2
                    resilience = int(line[24]) + 2
                    recovery = int(line[25]) + 2
                    discipline = int(line[26]) + 2
                    intellect = int(line[27]) + 2
                    strength = int(line[28]) + 2

                    if line[5] == "Helmet":
                        arr = np.array([mobility, resilience, recovery, discipline, intellect, strength])
                        self.Helmets[line[0] + "_" + str(h)] = arr
                        h += 1
                    elif line[5] == "Gauntlets":
                        arr = np.array([mobility, resilience, recovery, discipline, intellect, strength])
                        self.Gauntlets[line[0] + "_" + str(g)] = arr
                        g += 1
                    elif line[5] == "Chest Armor":
                        arr = np.array([mobility, resilience, recovery, discipline, intellect, strength])
                        self.Chests[line[0] + "_" + str(c)] = arr
                        c += 1
                    elif line[5] == "Leg Armor":
                        arr = np.array([mobility, resilience, recovery, discipline, intellect, strength])
                        self.Boots[line[0] + "_" + str(b)] = arr
                        b += 1

    def build_sets(self):
        # while loops are used to reformat each armor piece's name
        for helmet, value in self.Helmets.items():
            while helmet[-1].isnumeric() or helmet[-1] == "_":
                helmet = helmet[:-1]

            for gauntlet, value2 in self.Gauntlets.items():
                while gauntlet[-1].isnumeric() or gauntlet[-1] == "_":
                    gauntlet = gauntlet[:-1]

                for chest, value3 in self.Chests.items():
                    while chest[-1].isnumeric() or chest[-1] == "_":
                        chest = chest[:-1]

                    for boot, value4 in self.Boots.items():
                        while boot[-1].isnumeric() or boot[-1] == "_":
                            boot = boot[:-1]

                        cumulative = self.base_stats + value + value2 + value3 + value4
                        if ((self.primary_minimum <= cumulative[self.primary_index] <= self.primary_maximum)
                                and
                                (self.secondary_minimum <= cumulative[self.secondary_index] <= self.secondary_maximum)):

                            mob_tier = cumulative[0] // 10
                            res_tier = cumulative[1] // 10
                            rec_tier = cumulative[2] // 10
                            dis_tier = cumulative[3] // 10
                            int_tier = cumulative[4] // 10
                            str_tier = cumulative[5] // 10

                            total_tier = mob_tier + res_tier + rec_tier + dis_tier + int_tier + str_tier
                            if self.exotic:
                                if (self.exotic.lower() == helmet.lower() or
                                        self.exotic.lower() == gauntlet.lower() or
                                        self.exotic.lower() == chest.lower() or
                                        self.exotic.lower() == boot.lower()):
                                    heapq.heappush(self.heap, [-total_tier, list(cumulative),
                                                               [helmet, list(value)],
                                                               [gauntlet, list(value2)],
                                                               [chest, list(value3)],
                                                               [boot, list(value4)]])
                            else:
                                heapq.heappush(self.heap, [-total_tier, list(cumulative),
                                                           [helmet, list(value)],
                                                           [gauntlet, list(value2)],
                                                           [chest, list(value3)],
                                                           [boot, list(value4)]])
        return self.heap

    def output_results(self):
        for _ in range(self.max_results):
            try:
                result = heapq.heappop(self.heap)
                result[0] *= -1
                self.results.append(result)
            except IndexError:
                break

        for i in range(len(self.results)):
            print()
            print(f"Build {i + 1}:")
            print("--------------------------------------------------------")
            print(f"Helmet: {self.results[i][2][0]} - {self.results[i][2][1]}")
            print(f"Gauntlets: {self.results[i][3][0]} - {self.results[i][3][1]}")
            print(f"Chest Piece: {self.results[i][4][0]} - {self.results[i][4][1]}")
            print(f"Boots: {self.results[i][5][0]} - {self.results[i][5][1]}")
            print(f"Class Item: Any Masterwork Class Item - {list(self.class_item)}")
            print("--------------------------------------------------------")
            print(f"Cumulative Stats: {self.results[i][1]}")
            print(f"Total Tiers: {self.results[i][0]}")
            print("--------------------------------------------------------")


res = ArmorPicker()
res.populate_dictionaries()
res.build_sets()
res.output_results()
