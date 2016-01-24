import os

class NameScore:

    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(__file__), 'data.txt')
        self.names = self.load()
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.alphabet_position = self.create_alphabet_position()

    def load(self):
        names = []
        for l in open(self.data_path, 'r'):
            names.extend(l.replace('"', '').strip().split(','))

        names = map(lambda s: s.lower(), names)
        return names

    def create_alphabet_position(self):
        pos = dict()
        for i in range(len(self.alphabet)):
            pos[self.alphabet[i]] = i + 1
        return pos

    def get_value(self, name):
        value = 0
        for letter in name:
            value += self.alphabet_position[letter]
        return value

    def process(self):

        self.names = sorted(self.names)

        names_scores = dict()
        position = 1
        for name in self.names:
            names_scores[name] = position * self.get_value(name)

            position += 1

        return sum(names_scores.values())
