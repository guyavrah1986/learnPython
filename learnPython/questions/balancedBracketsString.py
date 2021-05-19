
def check_balanced_brackets_string(s: str) -> bool:
    print("the given string is:" + s)
    brackets_stack = []
    open_curly_braces_counter = 0
    open_brackets_counter = 0
    open_parentheses_counter = 0
    # optimization: check if the length of the string is even (if not return 0)
    if len(s) % 2 != 0:
        return False

    for c in s:
        if c == "{":
            open_curly_braces_counter += 1
            brackets_stack.insert(0, c)
            print("adding open bracket:" + c  + ", list is now:" + str(brackets_stack))
        elif c == "[":
            open_brackets_counter += 1
            brackets_stack.insert(0, c)
            print("adding open bracket:" + c  + ", list is now:" + str(brackets_stack))
        elif c == "(":
            open_parentheses_counter += 1
            brackets_stack.insert(0, c)
            print("adding open bracket:" + c  + ", list is now:" + str(brackets_stack))
        else:
            if not brackets_stack:
                print("not enough open brackets - error")
                return 0

            last_open_bracket = brackets_stack.pop(0)
            print("poped bracket:" + last_open_bracket + " compare it with:" + c)
            if c == ")":
                if last_open_bracket == "(":
                    open_parentheses_counter -= 1
                    continue
                else:
                    return False
            if c == "}":
                if last_open_bracket == "{":
                    open_curly_braces_counter -= 1
                    continue
                else:
                    return False
            if c == "]":
                if last_open_bracket == "[":
                    open_brackets_counter -= 1
                    continue
                else:
                    return False

            print("list is:" + str(brackets_stack))
    print("done iterating on the list - success")
    if open_brackets_counter != 0 or open_curly_braces_counter != 0 or open_parentheses_counter != 0:
        print("at the end of the loop over the string not all open counters are zero - error")
        return False

    return True


s = "{[]}"
print("return value for s:" + str(check_balanced_brackets_string(s)))
