def pramp():
    print "Practice Makes Perfect"

pramp()

sum(g) <= b
# so we have
b >= sum (g[0], ... g[k]) + (n - k)  * c


#
minimal_c = b / n

# my idea is
# increase c by 1 until I get a budget as close as possible to b

def budget(g, c):
    return [min(grant, c) for grant in g]


c = minimal_c
delta_increase = minimal_c * 0.1
while budget(g, c) < b:
    c += delta_increase

########
# Hey can you at least see the code?

# Other solution, sort the array of grants g
sorted_g = sorted(g, key=lambda grant:-grant)
# From there, we will navigate sorted_g from k= 0 to n-1 and cap it to sorted_g[k]
# The first time we're below g, that gives us two values for c, c_optimal will
# be betweem them
my_tot = sum(g)

def find_range(g):
    total_grants = my_tot
    previous_cap = sorted_g[0] * 2  # high number
    for grant in sorted_g:
        current_c = grant
        total_grants - grant + current_c
        if total_grants < b:
            return (previous_cap, grant)

        previous_cap = current_c

    return n / b


# Now we have a range in which we can look
previous_cap, grant = find_range(g)
tot_left_right = my_tot - grant

# New total is
tot_left_right + c = b

# So
c = b - tot_left_right

# This works only if the cap value we found appears only one time in the list.
# If it appears multiple times, say j
# We get

tot_left_right + j*c = b
c = (tot_left_right - b) / j

# If someone could review my solution this would be great !


