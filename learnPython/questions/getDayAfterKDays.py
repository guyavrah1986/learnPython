'''
Given a number K and a day in the week, return the day in the week after these K days.
'''


def get_day_after_k_days(curr_day: str, k: int) -> str:
    print("got day:" + curr_day + " and k:" + str(k))
    days_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    days_dict = \
        {
            "Sunday": 0,
            "Monday": 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6
        }

    curr_day_num = days_dict.get(curr_day, None)
    if curr_day_num is None:
        print("the provided day is invalid")
        return ""

    print("the given day num is:" + str(curr_day_num))
    return days_list[(curr_day_num + k) % 7]


day = "Monday"
k = 2
expected_day_num = "Wednesday"
ret_day_num = get_day_after_k_days(day, k)
if expected_day_num != ret_day_num:
    print("expected day:" + str(expected_day_num) + ", but instead got:" + str(ret_day_num))
    exit(1)

day = "Monday"
k = 7
expected_day_num = "Monday"
ret_day_num = get_day_after_k_days(day, k)
if expected_day_num != ret_day_num:
    print("expected day:" + str(expected_day_num) + ", but instead got:" + str(ret_day_num))
    exit(1)
