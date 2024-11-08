import unittest
from clockshop import ClockShop
from clock import Clock


class MyClockShopTests(unittest.TestCase):
    def test_init(self):
        clock_shop = ClockShop()
        self.assertEqual("", clock_shop.__str__(), "ClockShop should be empty but is not")

    def test_set_clock_valid_index(self):
        clocks = ["11:11:11"]
        clock_shop = ClockShop()
        clock_shop.fill_clock_shop(clocks)
        clock_shop.set_clock(Clock(10, 10, 10), 0)
        self.assertEqual("10:10:10\n", clock_shop.__str__())

    def test_set_clock_negative_index(self):
        clock_shop = ClockShop()
        try:
            clock_shop.set_clock(Clock(10, 10, 10), -1)
            self.assertEqual(True, False, "should not have got here, set_clock took a negative index")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_set_clock_index_too_large(self):
        clock_shop = ClockShop()
        try:
            clock_shop.set_clock(Clock(10, 10, 10), 0)
            self.assertEqual(True, False, "should not have got here, set_clock took an index beyond size")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_get_clock_valid_index(self):
        clocks = ["10:10:10"]
        clock_shop = ClockShop()
        clock_shop.fill_clock_shop(clocks)
        clock = clock_shop.get_clock(0)
        self.assertEqual("10:10:10", clock.__str__(), "correct clock not returned")

    def test_get_clock_negative_index(self):
        clocks = ["10:10:10"]
        clock_shop = ClockShop()
        clock_shop.fill_clock_shop(clocks)
        try:
            index = clock_shop.get_clock(-1)
            self.assertEqual(True, False, "should not have got here, get_clock took a negative index")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_get_clock_index_too_large(self):
        clock_shop = ClockShop()
        try:
            index = clock_shop.get_clock(0)
            self.assertEqual(True, False, "should not have got here, get_clock took an index beyond size -- no clocks")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_fill_clock_shop_one_clock_time(self):
        times = ["10:10:10"]
        clock_shop = ClockShop()
        clock_shop.fill_clock_shop(times)
        self.assertEqual("10:10:10\n", clock_shop.__str__(), "one clock not added to shop properly")

    def test_fill_clock_shop_three_clock_times(self):
        times = ["10:10:10", "11:11:11", "12:12:12"]
        clock_shop = ClockShop()
        clock_shop.fill_clock_shop(times)
        self.assertEqual("10:10:10\n11:11:11\n12:12:12\n", clock_shop.__str__(), "3 clocks not added to shop properly")

    def test_fill_clock_shop_two_then_one(self):
        times = ["10:10:10", "11:11:11"]
        clock_shop = ClockShop()
        clock_shop.fill_clock_shop(times)
        times2 = ["12:12:12"]
        clock_shop.fill_clock_shop(times2)
        self.assertEqual("10:10:10\n11:11:11\n12:12:12\n", clock_shop.__str__(), "3 clocks not added to shop properly")

    def test_find_clock_clock_is_there(self):
        clock_shop = ClockShop()
        times = ["10:10:10", "11:11:11", "12:12:12"]
        clock_shop.fill_clock_shop(times)
        index = clock_shop.find_clock(Clock(12, 12, 12))
        self.assertEqual(2, index, "retrieved clock index was not at proper location")

    def test_find_clock_clock_not_there(self):
        clock_shop = ClockShop()
        times = ["10:10:10", "11:11:11", "12:12:12"]
        clock_shop.fill_clock_shop(times)
        index = clock_shop.find_clock(Clock(12, 12, 13))
        self.assertEqual(-1, index, "retrieved clock index should have been -1 since clock not there")

    def test_sort_no_clocks(self):
        clock_shop = ClockShop()
        clock_shop.sort_clocks()
        self.assertEqual("", clock_shop.__str__(), "should be empty string for clock shop")

    def test_sort_one_clock(self):
        clock_shop = ClockShop()
        time = ["10:10:10"]
        clock_shop.fill_clock_shop(time)
        clock_shop.sort_clocks()
        self.assertEqual("10:10:10\n", clock_shop.__str__(), "should be one clock at 10:10:10")

    def test_sort_three_clocks_ascending(self):
        clock_shop = ClockShop()
        times = ["10:10:10", "11:11:11", "12:12:12"]
        clock_shop.fill_clock_shop(times)
        clock_shop.sort_clocks()
        self.assertEqual("10:10:10\n11:11:11\n12:12:12\n", clock_shop.__str__(), "should be 3 clocks in order")

    def test_sort_five_clocks_descending(self):
        clock_shop = ClockShop()
        times = ["12:12:12", "11:11:11", "10:10:10", "9:9:9", "8:8:8"]
        clock_shop.fill_clock_shop(times)
        clock_shop.sort_clocks()
        self.assertEqual("8:8:8\n9:9:9\n10:10:10\n11:11:11\n12:12:12\n",
                         clock_shop.__str__(), "should be 5 clocks in order")

    def test_sort_six_clocks_random(self):
        clock_shop = ClockShop()
        times = ["10:10:10", "0:0:0", "12:12:12", "9:9:9", "11:11:11", "8:8:8"]
        clock_shop.fill_clock_shop(times)
        clock_shop.sort_clocks()
        self.assertEqual("0:0:0\n8:8:8\n9:9:9\n10:10:10\n11:11:11\n12:12:12\n",
                         clock_shop.__str__(), "should be 5 clocks in order")

    def test_str_one_item(self):
        """yes, this is the same test as way above, just formalizing that we are testing __str__()"""
        times = ["11:11:11"]
        clock_shop = ClockShop()
        clock_shop.fill_clock_shop(times)
        clock_shop.set_clock(Clock(10, 10, 10), 0)
        self.assertEqual("10:10:10\n", clock_shop.__str__())


if __name__ == '__main__':
    unittest.main()
