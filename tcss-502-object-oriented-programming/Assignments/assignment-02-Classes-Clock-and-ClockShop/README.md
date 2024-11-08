# Purpose

The purpose of this assignment is to give you practice writing classes in Python. You will work with constructors, instance variables/fields, common class methods (__str__, __eq__, __lt__, __gt__), and other class basics. You will also get to write code for searching and sorting. Finally, you will get some practice with problem solving!

## Course Objectives this assignment meets

This assignment satisfies the following course objectives
C1: Use fundamental concepts of object-oriented design to write modular, extensible code
C3: Apply skills to systematically test and debug applications
C8: Design and implement unit tests for a medium complexity program with an object hierarchy that includes
interfaces and/or abstract classes.
C9: Utilize modern software engineering tools (e.g., IDEs, static checkers, unit testing frameworks, revision control systems) during the implementation of a medium complexity program.
C10: Correctly employ programming language features by reading and interpreting the associated published API documentation.
Basic Details
For this assignment you will write two classes Clock and ClockShop. The ClockShop class will be composed of a list of Clocks. This means you get to work with the OO concept of composition.

When you have completed your code for the two classes, you will use clock_tests and clockshop_tests provided to test your solution.

## Clock and ClockShop Information

This assignment will introduce you to writing a class to represent a specific topic (a clock) and then work with instances (objects) of that class. You then utilize your Clock class (clock.py) in a ClockShop class.

Your first task is to create a class called Clock.  A clock represents time in hours, minutes, and seconds.  The type of time it represents is military time (hours are from 0 to 23, with 0 representing midnight and 23 representing 11pm).  Here are the things a user of a Clock object should be able to do:

* Clock Constructor __init__(self, hour, minute, second): create a Clock object and specify the starting hour, minute, and second via parameters (we will use integer values for our data)
it defaults to 00:00:00 (hours, minutes, seconds) (12am) if no values are specified at creation
* __str__(self): get the current time in String format -- the object will return a String with the hours, minutes and seconds as follows: hh:mm:ss (ex: 9:49:59)
* __repr__(self): (same as __str__ for what we are doing) get the current time in String format -- the object will return a String with the hours, minutes and seconds as follows: hh:mm:ss (ex: 9:49:59)
* hour(self): -- the object will report as follows: hh (ex: 18 -- which means it is 6pm) -- the value returned should be the hour
* minute(self): -- the object will report as follows: mm (ex: 56) -- the value returned should be the minute
* second(self): -- the object will report as follows: ss (ex: 6) -- the value returned should be the second
* set_hour(self, new_hour): set the current hour (a number from 0 through 23 will be passed in to the object from outside) (any value outside this range should raise an exception with an appropriate error message)
* set_minute(self, new_minute): set the current minute (a number from 0 through 59 will be passed in to the object from outside) (any value outside this range should raise an exception with an appropriate message)
* set_second(self, new_second): set the current second (a number from 0 through 59 will be passed in to the object from outside) (any value outside this range should raise an exception with an appropriate message)
advance_hour(self, amount_to_advance): advance the current hour (a number 0 or greater will be passed in to the object from outside -- the resulting hour should be represented in the range of 0 to 23) (HINT: % is your friend) (any value less than 0 should raise an exception with an appropriate message)
* advance_minute(self, amount_to_advance): advance the current minute (a number 0 or greater will be passed in to the object from outside -- the resulting minute should be represented in the range of 0 to 59 *AND* the hour should be updated accordingly) (any value less than 0 should raise an exception with an appropriate message)
* set_to_current_time(self): set the time to the current time (hours, minutes, and seconds) based on what your computer reports.
* __eq__(self, other): compare against another Clock object for equality (an equals method) o Make sure the data passed as a parameter is a Clock (isinstance helps with this) then check that the hour, minute, and second of the clocks are the same for equality
* __lt__(self, other): compare against another Clock to see if current clock’s time is before other clock – make sure the parameter is a Clock then check hour, minute, and second as necessary to determine if the current Clock (self) is less than the other Clock
* __gt__(self, other): compare against another Clock to see if current clock’s time is after other clock with the same rules as eq and lt
NOTE: See the student.py code example posted to Canvas for an idea of how to write eq, lt, and gt (as well as some of the other methods!)
You are free to add more functionality to your Clock class as you see fit.

Next create a class ClockShop (place in clockshop.py). This class will hold list of Clock objects.  It will provide behaviors (methods) that allow for sorting, searching, retrieving, and printing the Clocks it contains.  Specifics for this class are as follows:

Declare a private field that is list of type Clock as part of the constructor (__init__(self))
fill_clock_shop(self, list_of_times): the method walks through the list of times (strings formatted hh:mm:ss, guaranteed), creates Clock objects, and adds them to your list of clocks. There will be at least one clock time in the list. Clocks should be added in the order they occur in list. If there are already clocks, the new clocks should be appended to the end of the existing list of clocks. To grab the hour, minute and second from each string examine the split function from the string class. You can pass it a string that contains the delimiter you would like to split the data by. The split function will return a tuple of strings. Here is how it might look: (hour, minute, second) = time.split(":") . From there you can access hour, minute and second independently and turn them into ints.
* sort_clocks(self): sorts the Clocks in ascending (smallest time to largest time) order. You must write the code to sort the array of Clocks
* find_clock(self, a_clock): it is passed a Clock object and checks to see if it exists in the Clock If it does exist, return the index of where the first one was found.  If it does not exist, return a -1.
* __str__(self): builds a string containing each Clock object in string format (via the __str(self)__ in the Clock class) and returns that string. Each Clock object should be separated from the others by a newline (\n). The last clock in the list should also have a newline following it.
* get_clock(self, index): it is passed an integer index of which Clock to retrieve from the list of Clock If the index is outside the range of the array, raise an exception with an appropriate message.  If the index falls within the list, return the Clock object at that index.
* set_clock(self, a_clock, index): it is passed a Clock object and an index. The method places the Clock object at the specified index in the list.  If the index is outside the range of the list, raise an exception with an appropriate message.

This is a unit test file that will test your Clock class. It assumes your source file is named clock.py and your class is named Clock. To use this test file, copy it into the PyCharm project folder where your clock.py file lives. Open your PyCharm project, then open the clock_tests.py file. Read through the description carefully. To run the tests you can right click on the open clock_tester.py file then choose Run Unittests for clock_tests.py (note that some of the name may be cut off). You can also use the keyboard shortcut Ctrl+Shift+F10. NOTE: depending on how you wrote your code, some of the tests might not pass.
ClockShop Tester: clockshop_tests.pyDownload clockshop_tests.py

## Submission

Submit a zip file named with your NetID followed by assignment2 (e.g. varikmpassignment2.zip). The zip should contain the following
clock.py
clockshop.py
clock_tests.py (your clock code should pass these tests)
clockshop_tests.py (your clockshop code should pass these tests)
UML class diagram representing Clock and ClockShop (should list all fields and methods with visibility and show relationship between the two classes). Name this file assignment2UML.pdf
readme.txt (this file should have your name at the top, followed by an estimate of the time it took you to complete the assignment, followed by any problems you had, followed by any shortcomings your solution has)
Rubric

Classes in Python: Clocks in a Clockshop

| Criteria      | Rating      | Pts      |
| ------------- | ------------- | ------------- |
| Contains full and syntactically correct representations of Clock and ClockShop along with their relationship |  | 5 pts |
| Miscellaneous-files named properly, readme included, anything else not mentioned in other criteria |  | 10 pts |
| Complete and correct based on tests provided by clock_tests.py. Contains all specified methods with code following naming conventions and style. | | 30 pts
| Complete and correct based on tests provided by clockshop_tests.py. Contains all specified methods with code following naming conventions and style.| |30 pts

### Total Points: 75
