# Solutions of Chapter 6.
import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)

def test_suite():
    """ Run the suite of tests for code in this module (this file). """

    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)

    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)

    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)

    test(day_add("Monday", 4) ==  "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")

    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(days_in_month(1) == None)
    test(days_in_month("Month") == None)

    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433,0,0) == 8758)  

    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)  

    print("-------------")
    test(3 % 4 == 0)
    test(3 % 4 == 3)
    test(3 / 4 == 0) # 3 / 4 == 0.75 (float)
    test(3 // 4 == 0)
    test(3+4  *  2 == 14)
    test(4-2+2 == 0)
    test(len("hello, world!") == 13)
    print("-------------")

    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)

    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13)

    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)

    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)

    test(is_even(6) == True)
    test(is_even(0) == True)
    test(is_even(9) == False)

    test(is_odd(6) == False)
    test(is_odd(0) == False)
    test(is_odd(9) == True)

    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))

    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))

    test(f2c(212) == 100)     # Boiling point of water
    test(f2c(32) == 0)        # Freezing point of water
    test(f2c(-40) == -40)     # Wow, what an interesting case!
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)

    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)


def turn_clockwise(direction):
    ''' Take one of these four compass points as its parameter, 
        and returns the next compass point in the clockwise direction.
    '''
    direction_list = ["N", "E", "S", "W"]
    for d in direction_list:
        if (d == direction):
            return direction_list[(direction_list.index(direction) + 1) % 4]
    
    return None

day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
def day_name(num):
    ''' Convert an integer number 0 to 6 into the name of a day. Assume day 0 is Sunday. '''
    if num >= 0 and num <= 6:
        return day_list[num]
    
    return None

def day_num(day):
    """ Give a day name, and returns its number. """
    for d in day_list:
        if day == d:
            return day_list.index(d)

    return None

def day_add(day, delta):
    """ Take a day name and a delta and return the resulting day name. """
    num = day_num(day)
    new_num = (num + delta) % 7
    return day_name(new_num)

def days_in_month(month):
    """  Take the name of a month, and return the number of days in the month. 
        Ignore leap years. 
    """
    month_dic = {
        "Janurary": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
    }
    for k in month_dic.keys():
        if k == month:
            return month_dic[month]
    
    return None
    
def to_secs(h, m, s):
    """ Convert hours, minutes and seconds to a total number of seconds. """
    return int(h * 3600 + m * 60 + s) 

def hours_in(sec):
    """ Return the whole integer number of hours represented by a total number of seconds. """
    return sec // 3600

def minutes_in(sec):
    """ Return the whole integer number of left over minutes in a total number of seconds, 
    once the hours have been taken out. """
    return (sec % 3600) // 60

def seconds_in(sec):
    """ Return the left over seconds represented by a total number of seconds. """
    return sec % 60

def compare(a, b):
    ''' Return 1 if a > b, 0 if a == b, and -1 if a < b. '''
    # Python 没有三目表达式(x = a >= b ? 1 : -1)
    # 对应 Python 语法: x = [True result] if [Condition] else [False result]
    # Example: result = 1 if a >= b else -1
    if a == b:
        return 0
    else:
        return (a - b) / abs(a - b)

def hypotenuse(a, b): 
    """ Return the length of the hypotenuse of a right triangle 
    given the lengths of the two legs as parameters. """
    return (a ** 2 + b **2) ** 0.5

def slope(x1, y1, x2, y2):
    """  Return the slope of the line through the points (x1, y1) and (x2, y2).  """
    return (y2 - y1) / (x2 - x1) if y2 - y1 != 0 else 0.0

def intercept(x1, y1, x2, y2):
    """ Return the y-intercept of the line through the points (x1, y1) and (x2, y2). """
    k = slope(x1, y1, x2, y2)
    b = y1 - k * x1
    return b

def is_even(n):
    """ Take an integer as an argument.
    Return True if the argument is an even number and False if it is odd. """
    return n % 2 == 0

def is_odd(n):
    """ Return True when n is odd and False otherwise. Use a call to is_even(). """
    # Python uses "not" instead of "!".
    return not is_even(n) 

def is_factor(f, n):
    """ Return True if f is a factor of n and False otherwise. """
    return n % f == 0

def is_multiple(n, f):
    return is_factor(f, n)

def f2c(t):
    """ Return the integer value of the nearest degree Celsius 
    for given temperature in Fahrenheit. """
    c = (t - 32) * 5 / 9
    return round(c)

def c2f(t):
    """ Convert Celsius to Fahrenheit. """
    f = t * 9 / 5 + 32
    return round(f)


test_suite()


