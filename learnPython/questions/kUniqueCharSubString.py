'''
Given a string and a number k return the maximum substring which has no more than k unique digits.
'''

# Python program to find the longest substring with k unique
# characters in a given string
MAX_CHARS = 26


# This function calculates number of unique characters
# using a associative array count[]. Returns true if
# no. of characters are less than required else returns
# false.
def valid_number_of_unique_chars(chars_count: list, max_num_of_unique_chars: int) -> bool:
    num_chars = 0
    for i in range(MAX_CHARS):
        if chars_count[i] > 0:
            num_chars += 1

    # Return true if there are more that the "max" number of chars
    return max_num_of_unique_chars >= num_chars


# Finds the maximum substring with exactly k unique characters
def kUniques(string: str, k: int) -> str:
    u = 0  # number of unique characters
    n = len(s)

    # Associative array to store the count
    count = [0] * MAX_CHARS

    # Traverse the string, fills the associative array
    # count[] and count number of unique characters
    for i in range(n):
        if count[ord(s[i]) - ord('a')] == 0:
            u += 1

        count[ord(s[i]) - ord('a')] += 1

    # If there are not enough unique characters, show
    # an error message.
    if u < k:
        print("Not enough unique characters")
        return ""

    # Otherwise take a window with first element in it.
    # start and end variables.
    curr_start = 0
    curr_end = 0

    # Also initialize values for result longest window
    max_window_size = 1
    max_window_start = 0

    # Initialize associative array count[] with zero
    count = [0] * len(count)

    count[ord(s[0]) - ord('a')] += 1  # put the first character

    # Start from the second character and add
    # characters in window according to above
    # explanation
    for i in range(1, n):

        # Add the character 's[i]' to current window
        count[ord(s[i]) - ord('a')] += 1
        curr_end += 1

        # If there are more than k unique characters in
        # current window, remove from left side
        while not valid_number_of_unique_chars(count, k):
            count[ord(s[curr_start]) - ord('a')] -= 1
            curr_start += 1

        # Update the max window size if required
        if curr_end - curr_start + 1 > max_window_size:
            max_window_size = curr_end - curr_start + 1
            max_window_start = curr_start

    print("Max substring is : " + s[max_window_start:max_window_start + max_window_size]
          + " with length " + str(max_window_size))
    return s[max_window_start:max_window_start + max_window_size]


# Driver function 
s = "aabacbebebe"
k = 3
print("for the string:" + s + " and k:" + str(k) + ", the returned sub string is:" + kUniques(s, k))

