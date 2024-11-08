import unittest
from clock import Clock
from datetime import datetime


class MyClockTests(unittest.TestCase):
    """This class tests a great deal of the functionality provided by the Clock class.
    Some assumptions were made with the tests that are specific to the instructor solution.
    Depending on how you write some of your methods, your code might not pass the tests.
    For example, these tests assume the __str__() method returns a string that has the
    hour, minute, and second separated by colons AND with no leading zeroes if a minute
    or second is single digits.
    In addition, some tests for set_hour, set_minute, advance_hour, advance_minute, __eq__()
    and __lt__() test for unexpected types (things that are not Clock objects). These
    tests look for some form of an exception to be raised. You have to look at the tests to
    see the type of exception they look for. If you want your code to pass these tests you will
    need to raise the same kind of exceptions in your code."""

    def test_init_default_and_str(self):
        """Tests to see the default values for hour, minute and second (zeroes) get assigned
        when creating a Clock and not specifying any parameters to the Clock constructor (__init__()).
        This test also indirectly tests the __str__() method as well to check the values of
        hour, minute, and second in string form"""
        clock = Clock()
        #you can change to 00 for your tests if you would like!
        self.assertEqual("0:0:0", clock.__str__(), "default clock not set to 0:0:0")

    def test_init_235959(self):
        """Does clock set properly to 1 second before midnight?"""
        clock = Clock(23, 59, 59)
        self.assertEqual("23:59:59", clock.__str__(), "clock not set to 23:59:59")

    def test_hour_minute_second(self):
        """Simple test to see the three getters (hour(), minute(), and second() return the correct values"""
        clock = Clock(10, 11, 12)
        self.assertEqual(10, clock.hour(), "hour was not 10")
        self.assertEqual(11, clock.minute(), "minute was not 11")
        self.assertEqual(12, clock.second(), "second was not 12")

    def test_set_hour_23(self):
        """Simple test to set hour to 23"""
        clock = Clock()
        clock.set_hour(23)
        self.assertEqual(23, clock.hour(), "hour not set to 23")

    def test_set_hour_negative(self):
        """Set hour to negative value which should raise an exception of type ValueError"""
        clock = Clock()
        try:
            clock.set_hour(-1)
            self.assertEqual(True, False, "exception not thrown for hour of -1")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_set_hour_24(self):
        """Set hour to 24, which is outside of range 0-23 so a ValueError should be raised"""
        clock = Clock()
        try:
            clock.set_hour(24)
            self.assertEqual(True, False, "exception not thrown for hour of 24")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_set_minute_59(self):
        """Simple test setting minute to 59"""
        clock = Clock()
        clock.set_minute(59)
        self.assertEqual(59, clock.minute(), "minute not set to 59")

    def test_set_minute_60(self):
        """Set minute to 60 which should raise a ValueError"""
        clock = Clock()
        try:
            clock.set_minute(60)
            self.assertEqual(True, False, "exception not thrown for minute of 60")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_set_minute_negative(self):
        """Test setting minute to negative value which should raise a ValueError"""
        clock = Clock()
        try:
            clock.set_minute(-1)
            self.assertEqual(True, False, "exception not thrown for minute of -1")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_set_second_59(self):
        """Simple test setting second to 59"""
        clock = Clock()
        clock.set_second(59)
        self.assertEqual(59, clock.second(), "second not set to 59")

    def test_set_second_60(self):
        """Set second to 60 which should raise a ValueError"""
        clock = Clock()
        try:
            clock.set_second(60)
            self.assertEqual(True, False, "exception not thrown for second of 60")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_set_second_negative(self):
        """Test setting second to negative value which should raise a ValueError"""
        clock = Clock()
        try:
            clock.set_second(-1)
            self.assertEqual(True, False, "exception not thrown for second of -1")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_advance_hour_negative(self):
        """Advance hour with negative value which should raise a ValueError"""
        clock = Clock()
        try:
            clock.advance_hour(-1)
            self.assertEqual(True, False, "exception not thrown for advance hour value of -1")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_advance_hour_no_rollover(self):
        """Simple advance hour test that does not roll over to new set of hours"""
        clock = Clock()
        clock.advance_hour(23)
        self.assertEqual("23:0:0", clock.__str__(), "advance hour from 0 to 23 did not work")

    def test_advance_hour_rollover_48(self):
        """Test that hour advances by 48 (2 days) which should leave it back where it started"""
        clock = Clock()
        clock.advance_hour(48)
        # you can change to 00 for your tests if you would like!
        self.assertEqual("0:0:0", clock.__str__(), "advance hour from 0 by 48 back to 0 did not work")

    def test_advance_minute_negative(self):
        """Negative value test that should raise a ValueError"""
        clock = Clock()
        try:
            clock.advance_minute(-1)
            self.assertEqual(True, False, "exception not thrown for advance minute value of -1")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_advance_minute_no_rollover(self):
        """Basic advance that will not roll over the minute or subsequently the hour"""
        clock = Clock()
        clock.advance_minute(59)
        # you can change to 00 for your tests if you would like!
        self.assertEqual("0:59:0", clock.__str__())

    def test_advance_minute_rollover(self):
        """Test advance of minute and hour due to rollover"""
        clock = Clock()
        clock.advance_minute(121)
        # you can change to 00 for your tests if you would like!
        self.assertEqual("2:1:0", clock.__str__())

    def test_eq_clocks_equal(self):
        """Test eq method on two clocks with same value"""
        clock1 = Clock()
        clock2 = Clock(0, 0, 0)
        self.assertEqual(clock1, clock2, "clocks are not equal but they should be")

    def test_eq_clocks_not_equal(self):
        """Test on two clocks that are not equal"""
        clock1 = Clock()
        clock2 = Clock(0, 0, 1)
        self.assertNotEqual(clock1, clock2, "clocks are equal but they should not be")

    def test_eq_wrong_type(self):
        """Test eq with something other than a Clock (the integer 37 in this case) which should raise a TypeError"""
        clock = Clock()
        try:
            if clock == 37:
                self.assertEqual(True, False, "somehow got past clock == 37")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_lt_first_less_than_second(self):
        """Basic test of lt (the < operator) where first Clock is less than second"""
        clock1 = Clock()
        clock2 = Clock(0, 0, 1)
        self.assertLess(clock1, clock2, "0:0:0 should be less than 0:0:1")

    def test_lt_first_same_second(self):
        """Test where clocks are same so < should return a False"""
        clock1 = Clock()
        clock2 = Clock()
        self.assertEqual(False, clock1 < clock2)

    def test_lt_wrong_type(self):
        """Use something other than a Clock with <, which should raise a TypeError"""
        clock = Clock()
        try:
            if clock < 37:
                self.assertEqual(True, False, "somehow got past clock < 37")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_gt_first_greater_than_second(self):
        """Basic test of gt (the > operator) where first Clock is greater than second"""
        clock1 = Clock(1, 1, 1)
        clock2 = Clock(1, 0, 1)
        self.assertGreater(clock1, clock2, "1:1:1 should be greater than 1:0:1")

    def test_gt_first_same_second(self):
        """Test where clocks are same so > should return a False"""
        clock1 = Clock()
        clock2 = Clock()
        self.assertEqual(False, clock1 > clock2)

    def test_gt_wrong_type(self):
        """Use something other than a Clock with >, which should raise a TypeError"""
        clock = Clock()
        try:
            if clock > 37:
                self.assertEqual(True, False, "somehow got past clock > 37")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_set_to_current_time(self):
        """Get current time from clock and actual current time, check hour, minute, and second.
        They should be same or close.
        *******WARNING: Test can fail just before top of second, minute or hour!!!"""
        clock = Clock()
        clock.set_to_current_time()
        now = datetime.now()
        self.assertLessEqual(clock.hour(), now.hour)
        self.assertLessEqual(clock.minute(), now.minute)
        self.assertLessEqual(clock.second(), now.second)
        print(clock)
        print(f"{now.hour}:{now.minute}:{now.second}")


if __name__ == '__main__':
    unittest.main()
