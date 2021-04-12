'''
Write a function that will return the minimum number of letters that needs to be removed in order to
have a string in which each character appears unique number of times
for example: given the string "ccaaffddecee" 6 characters should be removed, for instance
eee will be removed (3)
aa will be removed (2)
'''


def min_cnt_char_deletions_frequency(my_str):
    n = len(my_str)
    char_freq_mapper = {}
    char_freq_priority_queue = []
    counter = 0

    for i in range(n):
        char_freq_mapper[my_str[i]] = char_freq_mapper.get(my_str[i], 0) + 1

    for it in char_freq_mapper:
        char_freq_priority_queue.append(char_freq_mapper[it])

    # Sorting will not effect time complexity because we have at most 26 letters so it is a constant
    char_freq_priority_queue = sorted(char_freq_priority_queue)

    while len(char_freq_priority_queue) > 0:
        freq_from_pq = char_freq_priority_queue[-1]
        char_freq_priority_queue.pop()

        # If priority queue is empty return the counter
        if len(char_freq_priority_queue) == 0:
            return counter

        # Check if the last frequent in PQ is same as our freq_from_pq
        if freq_from_pq == char_freq_priority_queue[-1]:
            if freq_from_pq > 1:
                char_freq_priority_queue.append(freq_from_pq - 1)

            counter += 1
        # Sorting will not effect time complexity because we have at most 26 letters so it is a constant
        char_freq_priority_queue = sorted(char_freq_priority_queue)

    return counter


if __name__ == "__main__":
    str_list = {"aaaabbbb": 1, "ccaaffddecee": 6, "eeee": 0, "example": 4, "eeddccfftt": 7, "": 0}
    for st, ex in str_list.items():
        print("expected result:" + str(ex) + ".my func result:" + str(min_cnt_char_deletions_frequency(st)))
