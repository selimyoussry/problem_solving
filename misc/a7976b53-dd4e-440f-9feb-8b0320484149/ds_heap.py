__author__ = 'somedude'

class MinHeap:

    def __init__(self):
        self.heap_list = []
        self.current_size = 0

    def insert(self, x):
        self.heap_list.append(x)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_up(self, i):
        if i == 0:
            return True

        parent = (i - 1) // 2
        if self.heap_list[parent] > self.heap_list[i]:
            self.swap(self.heap_list, i, parent)
            self.perc_up(parent)

    def del_min(self):
        ret = self.heap_list[0]
        self.heap_list[0] = self.heap_list[-1]
        del self.heap_list[-1]
        self.current_size -= 1

        self.perc_down(0)

        return ret

    def perc_down(self, i):
        while 2*i+1 < self.current_size:

            check_idx = self.min_child(i)

            if self.heap_list[check_idx] < self.heap_list[i]:
                self.swap(self.heap_list, i, check_idx)
                i = check_idx
            else:
                i = self.current_size

    def min_child(self, i):
        if i * 2 + 2 >= self.current_size:
            return i * 2 + 1
        else:
            return i * 2 + 1 if self.heap_list[i * 2 + 1] < self.heap_list[i * 2 + 2] else i * 2 + 2

    @staticmethod
    def swap(a, i, j):
        tmp_i = a[i]
        a[i] = a[j]
        a[j] = tmp_i
