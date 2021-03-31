class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr_len = len(nums)
        curr_blue_from_end = arr_len - 1
        curr_red_from_start = 0
        index = 0
        while index < arr_len:
            if nums[index] != 0:
                # look for the first RED you encounter and switch it with
                # nums[index]
                tmp = index
                while tmp < arr_len:
                    if nums[tmp] == 0:
                        tmp_val = nums[index]
                        nums[index] = 0
                        nums[tmp] = tmp_val
                        break
                    else:
                        tmp += 1

            index += 1

        # re-order all BLUE's (2)
        index = arr_len - 1
        while index >= 0:
            if nums[index] != 2:
                # look for the first BLUE you encounter to switch with
                tmp = index
                while tmp >= 0:
                    if nums[tmp] == 2:
                        tmp_val = nums[index]
                        nums[index] = 2
                        nums[tmp] = tmp_val
                        break
                    else:
                        tmp -= 1

            index -= 1
