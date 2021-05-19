'''

'''

class solution:

    def __init__(self, file_object):
        self.file_object = file_object
        self.list_of_numbers = []
        self.index = 0
        self.__parse_file()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.list_of_numbers):
            raise StopIteration

        ret_num = self.list_of_numbers[self.index]
        self.index += 1
        return ret_num

    # private/utilities function:
    @staticmethod
    def __represents_int(s: str) -> bool:
        try:
            int(s)
            return True
        except ValueError:
            return False

    def __is_valid_line(self, line: str) -> bool:
        if ' ' in line:
            print("there is a space in the line (which is not leading or trailing)")
            return False

        if not self.__represents_int(line):
            print("line:" + line + " is not a legitimate int")
            return False

        return True

    def __parse_file(self):
        lines = self.file_object.readlines()
        num_line = 1
        for line in lines:
            print("line[" + str(num_line) + "]:" + line)
            line = line.strip()
            # print("after strip - line[" + str(num_line) + "]:" + line)
            if not self.__is_valid_line(line):
                print("line:" + line + " is INVALID")
            else:
                print("line:" + line + " is OK")
                self.list_of_numbers.append(line)
            num_line += 1

###########################################################################
###########################################################################



file_name = "/auto/dev_users/gavraha/Desktop/sampleFile"
with open(file_name) as file_object:
    for i in solution(file_object):
        print(i)

'''
expected_val = None
ret_val = None
if expected_val != ret_val:
    print("expected to get val " + str(expected_val) + " but instead got:" + str(ret_val))
    exit(1)
'''






