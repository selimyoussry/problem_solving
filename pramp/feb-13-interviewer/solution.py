# solution.py

class ShiftedArraySearch:

    def __init__(self):
        pass

    def find_sorted(self, arr, num, idx_start):
        len_arr = len(arr)

        if len_arr == 1:
            return idx_start if arr[0] == num else -1

        mid_arr = len_arr / 2
        if num == arr[mid_arr]:
            return mid_arr + idx_start
        elif num < arr[mid_arr]:
            return self.find_sorted(arr[0:mid_arr], num, idx_start)
        else:
            return self.find_sorted(arr[mid_arr:], num, idx_start + mid_arr)

    def find_sorted_linear(self, arr, num):
        for i in range(len(arr)):
            if arr[i] == num:
                return i

        return -1

    def find_sorted_shifted(self, arr, num, idx_start):

        len_arr = len(arr)

        if len_arr == 1:
            return idx_start if arr[0] == num else -1

        a = arr[0]
        b = arr[-1]
        mid_pos = len_arr / 2
        x = arr[mid_pos]

        if a < b:  # Then no shift
            return self.find_sorted(arr, num, idx_start)

        if num == x:
            return idx_start + mid_pos

        if x >= a:
            if a <= num <= x:
                return self.find_sorted_shifted(arr[:mid_pos], num, idx_start)
            else:
                return self.find_sorted_shifted(arr[mid_pos:], num, idx_start + mid_pos)
        else:
            if x <= num <= b:
                return self.find_sorted_shifted(arr[mid_pos:], num, idx_start + mid_pos)
            else:
                return self.find_sorted_shifted(arr[:mid_pos], num, idx_start)