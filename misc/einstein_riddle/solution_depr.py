# solution.py

NATIONALITIES = {'brit', 'norwegian', 'german', 'dane', 'swede'}
DRINKS = {'tea', 'coffee', 'milk', 'water', 'beer'}
SMOKE = {'prince', 'blue_master', 'dunhill', 'pall_mall', 'blend'}
PET = {'dog', 'bird', 'cat', 'horse', 'fish'}
COLORS = {'red', 'yellow', 'white', 'blue', 'green'}
POSITIONS = {1, 2, 3, 4, 5}
UNKNOWNS = {
    'pos': POSITIONS,
    'nat': NATIONALITIES,
    'drink': DRINKS,
    'smoke': SMOKE,
    'pet': PET,
    'col': COLORS
}

class Einstein:

    def __init__(self):
        self.houses = [House()] * 5

    def is_solved(self):
        for h in self.houses:
            if not h.is_solved():
                return False
        return True

    def get_from_attribute(self, unknown, value):
        assert self.is_solved()

        for h in self.houses:
            if h.unknowns[unknown] == value:
                return h


class House:
    def __init__(self):
        self.unknowns = UNKNOWNS

    def remove_option(self, which, value):
        self.unknowns[which].remove(value)

    def set_value(self, which, value):
        assert which in UNKNOWNS
        assert value in UNKNOWNS[which]

        self.unknowns[which] = {value}

    def is_solved(self):
        for u in self.unknowns.values():
            if len(u) > 1:
                return False

        return True

    def print_is_solved(self):
        print 'Not solved yet' if not self.is_solved() else 'Bravo!'
