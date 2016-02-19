__author__ = 'somedude'

from solution import *

UNKNOWNS = {
    'pos': POSITIONS,
    'nat': NATIONALITIES,
    'drink': DRINKS,
    'smoke': SMOKE,
    'pet': PET,
    'col': COLORS
}


e = Einstein()

# The Brit lives in the red house
e.houses[0].set_value('col', 'red')
e.houses[0].set_value('nat', 'brit')

# The Swede keeps dogs as pets
e.houses[1].set_value('pet', 'dog')
e.houses[1].set_value('nat', 'swede')

# The Dane drinks tea
e.houses[2].set_value('drink', 'tea')
e.houses[2].set_value('nat', 'dane')

# The green house is on the left of the white house
# ?

# The green homeowner drinks coffee
# ?

# The person who smokes Pall mall rears birds
# ?

# The owner of the yellow house smokes Dunhill
# ?

