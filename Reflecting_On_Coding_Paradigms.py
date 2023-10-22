def functional_prompt(list):
    print(sorted(list, reverse=False))


functional_prompt([2, 5, 55, 22, 333, 12, 41, 89])


# Object Oriented Prompt
class Podracer:
    def __init__(self, max_speed, condition, price, name):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
        self.name = name

    def repair(self):
        for item in self.condition:
            if item == "trashed":
                new_str = self.name + "'s" + " " + "pod" + " " "is" + " " + "repaired"
                return new_str
            else:
                return item

    def win(self):
        return self.name + " " + "wins the race"


class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price, name):
        super().__init__(max_speed, condition, price, name)
        self.max_speed = max_speed

    def boost(self):
        special_ability = "Anakin's max_speed is now" + " " + str(self.max_speed * 2)
        return special_ability


class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price, name):
        super().__init__(max_speed, condition, price, name)
        self.condition

    def flame_jet(self):
        for item in self.condition:
            if item == "perfect" or item == "repaired":
                AnakinsPod.condition = "trashed"
                text = (
                    "Anakins Pod is"
                    + " "
                    + AnakinsPod.condition
                    + " "
                    + "by"
                    + " "
                    + self.name
                )
                return text


contestant1 = AnakinsPod(2, ["trashed"], 20, "Anakin")
contestant2 = SebulbasPod(1, ["perfect"], 30, "Sebulba")
print(contestant1.repair())
print(contestant1.boost())
print(contestant2.flame_jet())
print(contestant1.repair())
print(contestant1.win())
