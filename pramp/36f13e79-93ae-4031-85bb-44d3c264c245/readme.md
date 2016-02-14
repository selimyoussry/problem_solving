# pramp - Problem 36f13e79-93ae-4031-85bb-44d3c264c245
skype with adi


"""
A hotel manager has to process N advance bookings of rooms for the next season. 
His hotel has K rooms. Bookings contain an arrival date and a departure date. 
He wants to find out whether there are enough rooms in the hotel to satisfy the demand. 
Write a program that solves this problem in time O(N log N).
"""


# @param arrive : list of integers
# @param depart : list of integers
# @param K : integer
# @return a boolean


  
def compare(a, b):
    if a[0] < b[0]:
        return -1
    elif a[0] == b[0]:
        if a[1] > b[1]:
            return -1
        elif a[1] == b[1]:
            return 0
        else:
            return 1
    else:
        return 1

def hotel(arrive, depart, K):
    event = []
    for a in arrive :
        event.append((a, '0'))
    for d in depart :
        event.append((d, '1'))
    event.sort(cmp=compare)
    print event
    count = 0
    for i in xrange(len(event)) :
        if event[i][1] == '0' :
            count += 1
        elif event[i][1] == '1' :
            count -= 1
        if count > K :
            return 0
    return 1



def compare(a, b):
    if a[0] < b[0]:
        return -1
    elif a[0] == b[0]:
        if a[1] > b[1]:
            return -1
        elif a[1] == b[1]:
            return 0
        else:
            return 1
    else:
        return 1

def hotel(arrive, depart, K):
    event = []
    for a in arrive :
        event.append((a, '0'))
    for d in depart :
        event.append((d, '1'))
    event.sort(cmp=compare)
    count = 0
    for i in xrange(len(event)) :
        if event[i][1] == '0' :
            count += 1
        elif event[i][1] == '1' :
            count -= 1
        if count > K :
            return 0
    return 1