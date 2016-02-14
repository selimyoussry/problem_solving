# solution.py

# Linear time solution, cannot do better

def is_twice(arr):
    s = set()
    for elt in arr:
        if elt not in s:
            s.add(elt)
        else:
            return elt
