# solution.py

NATIONALITIES = {'brit', 'norwegian', 'german', 'dane', 'swede'}
DRINKS = {'tea', 'coffee', 'milk', 'water', 'beer'}
SMOKE = {'prince', 'blue_master', 'dunhill', 'pall_mall', 'blend'}
PET = {'dog', 'bird', 'cat', 'horse', 'fish'}
COLORS = {'red', 'yellow', 'white', 'blue', 'green'}
POSITIONS = [1, 2, 3, 4, 5]
UNKNOWNS = {
    'pos': POSITIONS,
    'nat': NATIONALITIES,
    'drink': DRINKS,
    'smoke': SMOKE,
    'pet': PET,
    'col': COLORS
}

def rfs(s, x):
    s.remove(x)
    return s

class Einstein:
    def __init__(self):
        self.all_solutions = self.get_all_solutions()

    def get_all_solutions(self):
        all_solutions = []

        combinations_first_house = self.get_houses(NATIONALITIES, DRINKS, SMOKE, PET, COLORS, 1)

        for first_house in combinations_first_house:  # this is the first house
            nats_2 = rfs(NATIONALITIES, first_house.nat)
            drinks_2 = rfs(DRINKS, first_house.drink)
            smoked_2 = rfs(SMOKE, first_house.smoke)
            pet_2 = rfs(PET, first_house.pet)
            col_2 = rfs(COLORS, first_house.col)
            combinations_second_house = self.get_houses(nats_2, drinks_2, smoked_2, pet_2, col_2, 2)
            for second_house in combinations_second_house:
                nats_3 = rfs(nats_2, second_house.nat)
                drinks_3 = rfs(drinks_2, second_house.drink)
                smoked_3 = rfs(smoked_2, second_house.smoke)
                pet_3 = rfs(pet_2, second_house.pet)
                col_3 = rfs(col_2, second_house.col)
                combinations_third_house = self.get_houses(nats_3, drinks_3, smoked_3, pet_3, col_3, 3)
                for third_house in combinations_second_house:
                    nats_4 = rfs(nats_3, second_house.nat)
                    drinks_4 = rfs(drinks_3, second_house.drink)
                    smoked_4 = rfs(smoked_3, second_house.smoke)
                    pet_4 = rfs(pet_3, second_house.pet)
                    col_4 = rfs(col_3, second_house.col)
                    combinations_third_house = self.get_houses(nats_4, drinks_4, smoked_4, pet_4, col_4, 4)
                    for fourth_house in combinations_second_house:
                        nats_4 = rfs(nats_3, second_house.nat)
                        drinks_4 = rfs(drinks_3, second_house.drink)
                        smoked_4 = rfs(smoked_3, second_house.smoke)
                        pet_4 = rfs(pet_3, second_house.pet)
                        col_4 = rfs(col_3, second_house.col)
                        combinations_third_house = self.get_houses(nats_4, drinks_4, smoked_4, pet_4, col_4, 4)





        return all_solutions

    def get_houses(self, nats, drinks, smokes, pets, cols, pos):
        combinations = []
        for nat in nats:
            for drink in drinks:
                for smoke in smokes:
                    for pet in pets:
                        for col in cols:
                            combinations.append(
                                House(pos, nat, drink, smoke, pet, col)
                            )
        return combinations

class House:
    def __init__(self, pos, nat, drink, smoke, pet, col):
        self.pos = pos
        self.nat = nat
        self.drink = drink
        self.smoke = smoke
        self.pet = pet
        self.col = col

class Houses:
    def __init__(self, houses):
        self.houses = houses


    def test(self):
        pass
