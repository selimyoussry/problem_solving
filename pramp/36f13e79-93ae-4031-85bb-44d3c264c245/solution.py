# solution.py

def hotel(arrive, depart, K):
    arr_dep = sorted(
        [(x, False) for x in depart] + [(x, True) for x in arrive)],
key=lambda u:u[0]
)

current_day = arr_dep[0][0]
i = 0
while i<len(arr_dep):
    day, arrival = arr_dep[i]
    if day != current_day and K<0:
        return False

    if arrival:
        K -= 1
    else:
        K += 1
    current_day = day
    i += 1

    return K >= 0
