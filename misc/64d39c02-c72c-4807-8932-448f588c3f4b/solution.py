# solution.py

class LongestSeq:

    def __init__(self):
        pass

    def run_consecutive(self, l):
        len_l = len(l)

        # Initialisation
        prev = l[0]
        max_seq_size = 1
        curr_seq_size = 1

        # Loop trough elements
        for i in range(1, len_l):
            curr = l[i]
            if curr > prev:
                curr_seq_size += 1
            else:
                max_seq_size = max(curr_seq_size, max_seq_size)
                curr_seq_size = 1
            prev = curr

        max_seq_size = max(curr_seq_size, max_seq_size)
        return max_seq_size

    def run(self, l):

        # Initialize
        len_l = len(l)
        max_sub = dict()
        for i in range(len_l):
            max_sub[i] = 1
        max_subsequence = 1

        for i in range(len_l):
            for j in range(i):
                if l[j] < l[i]:
                    max_sub[i] = max(max_sub[i], max_sub[j] + 1)
            max_subsequence = max(max_subsequence, max_sub[i])

        return max_subsequence
