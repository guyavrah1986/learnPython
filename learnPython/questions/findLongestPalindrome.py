

def find_longest_palindrome(s: str) -> str:
    print("original string is:" + s)
    start_palindrome_index = 0
    end_palindrome_index = len(s) - 1
    start_index = 0
    end_index = len(s) - 1
    print("starting with start index:" + str(start_index) + " and end index:" + str(end_index))
    while end_index - start_index > 0:
        if s[start_index] == s[end_index]:
            print("s[" + str(start_index) + "] == s[" + str(end_index) + "]")
        else:
            start_palindrome_index = start_index + 1
            end_palindrome_index = end_index - 1

        start_index += 1
        end_index -= 1

    if end_palindrome_index - start_palindrome_index > 1:
        return s[start_palindrome_index:end_palindrome_index + 1]

    return ""


s = "wbccba"
print("the longest palindrome is:" + find_longest_palindrome(s))
