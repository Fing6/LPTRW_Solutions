# Solutions of Chapter 7. (without q11, q12 and q17)
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
    # sum_up_no_first_even
    test(sum_up_no_first_even([5, 2, 7, 8, 3, 4]) == 27)
    test(sum_up_no_first_even([]) == 0)
    test(sum_up_no_first_even([2, 4, 6, 8]) == 18)
    test(sum_up_no_first_even([1, 3, 5, 7]) == 16) 

    # count_up_to_sam
    test(count_up_to_sam([]) == 0)
    test(count_up_to_sam(["sam", "alice", "bob"]) == 1)
    test(count_up_to_sam(["alice", "bob", "sam"]) == 3)
    test(count_up_to_sam(["alice", "bob"]) == 2) # "sam" doesn't occur.

    sqrt(25)

    print_triangular_numbers(5)
    
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))

    test(num_digits(0) == 1)
    test(num_digits(-12345) == 5)

    test(num_even_digits(123456) == 3)
    test(num_even_digits(2468) == 4)
    test(num_even_digits(1357) == 0)
    test(num_even_digits(0) == 1)

    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([ ]) == 0)
    test(sum_of_squares([2, -3, 4]) == 29)

def count_odd(list):
    """ 1. Write a function to count how many odd numbers are in a list. """
    count = 0
    for i in list:
        if i % 2 == 1:
            count += 1
    return count

def sum_up_even(list):
    """ 2. Sum up all the even numbers in a list. """
    sum = 0
    for i in list:
        if i % 2 == 0:
            sum += i
    return sum

def sum_up_negative(list):
    """ 3. Sum up all the negative numbers in a list. """
    sum = 0
    for i in list:
        if i < 0:
            sum += i
    return sum
    
def count_word_5(list):
    """ 4. Count how many words in a list have length 5. """
    count = 0
    for i in list:
        if len(i) == 5:
            count += 1
    return count

def sum_up_no_first_even(list):
    """ 5. Sum all the elements in a list up to but not including the first even number. """
    sum = 0
    flag = 0
    for i in list:
        if flag == 0 and i % 2 == 0:
            flag = 1
            continue
        sum += i
    return sum

def count_up_to_sam(list):
    """ 6. Count how many words occur in a list up to 
    and including the first occurrence of the word “sam”. """
    count = 0
    for i in list:
        count += 1
        if i == "sam":
            break
    return count

def sqrt(n):
    """ 7. Add a print function to Newton’s sqrt function 
    that prints out better each time it is calculated. """
    approx = n/2.0 # Start with some or other guess at the answer
    while True: 
        better = (approx + n/approx)/2.0
        # print(better)
        if abs(approx - better) < 0.001: 
            return better
        approx = better

def print_triangular_numbers(n):
    """ 9. Print out the first n triangular numbers. """ 
    # The nth triangular number is the number of dots in the triangular arrangement with n dots on a side, 
    # and is equal to the sum of the n natural numbers from 1 to n. (from Wikipedia)
    sum = 0
    for i in range(1, n + 1):
        sum += i
        print(str(i) + "\t" + str(sum))

def is_prime(n):
    """ 10. Take a single integer argument and returns True when the argument is a prime number 
    and False otherwise. """
    end = int(sqrt(n))
    for i in range(2, end + 1):
        if n % i == 0:
            return False
    return True

def num_digits(n):
    """ 14. Modify it to return 1 for num_digits(0). 
        Modify num_digits so that it works correctly with any integer value. """
    # return 1 for num_digits(0)
    if n == 0:
        return 1
    
    # work with negative integer value
    n = abs(n)

    count = 0
    while n != 0:
        count = count + 1
        n = n // 10
    return count

def num_even_digits(n):
    """ 15. Count the number of even digits in n. """
    if n == 0:
        return 1

    n = abs(n)

    count = 0
    while n != 0:
        if (n % 10) % 2 == 0:
            count += 1
        n = n // 10

    return count

def sum_of_squares(xs):
    """ 16. Compute the sum of the squares of the numbers in the list xs. """
    sum = 0
    for n in xs:
        sum += n ** 2
    return sum

test_suite()