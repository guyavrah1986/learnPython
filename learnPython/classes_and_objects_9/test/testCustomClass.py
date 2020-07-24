import unittest


class TestCustomClass(unittest.TestCase):

    def test_first_test(self):
        func_name = "test_first_test - "
        print(func_name + "start")
        self.assertEqual(True, True)
        print(func_name + "end")

    def test_second_test(self):
        func_name = "test_second_test - "
        print(func_name + "start")
        self.assertEqual(True, True)
        print(func_name + "end")


if __name__ == "__main__":
    unittest.main()