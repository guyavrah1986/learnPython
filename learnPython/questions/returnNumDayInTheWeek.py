

def get_day_of_the_week_num(day_str: str) -> int:
    days_dict = \
        {
            "Sunday": 1,
            "Monday": 2,
            "Tuesday": 3,
            "Wednesday": 4,
            "Thursday": 5,
            "Friday": 6,
            "Saturday": 7
        }

    ret_day_int = days_dict.get(day_str, None)
    if ret_day_int is None:
        return 0

    return ret_day_int


day = "Monday"
expected_day_int = 2
ret_day = get_day_of_the_week_num(day)
if ret_day != expected_day_int:
    print("expected day int:" + str(expected_day_int) + ", BUT go instead:" + str(ret_day))
    exit(1)

day = "ert"
expected_day_int = 0
ret_day = get_day_of_the_week_num(day)
if ret_day != expected_day_int:
    print("expected day int:" + str(expected_day_int) + ", BUT go instead:" + str(ret_day))
    exit(1)
