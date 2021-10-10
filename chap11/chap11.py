# Solutions of Chapter 11
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
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

    test(dot_product([1, 1], [1, 1]) ==  2)
    test(dot_product([1, 2], [1, 4]) ==  9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)

    test(cross_product([1, 2, 3], [1, 5, 7]) == [-1, -4, 3])

    test(replace("Mississippi", "i", "I") == "MIssIssIppI")

    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    test(replace(s, "om", "am") ==
        "I love spam! Spam is my favorite food. Spam, spam, yum!")

    test(replace(s, "o", "a") ==
        "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

# Question 5
def add_vectors(u, v):
    """ Take two lists of numbers of the same length, 
    and returns a new list containing the sums of the corresponding elements of each. """
    new_list = []
    for i in range(0, len(u)):
        new_list.append(u[i] + v[i])
    return new_list

# Question 6
def scalar_mult(s, v):
    """  Take a number, s, and a list, v and returns the scalar multiple of v by s. """
    new_list = []
    for i in range(0, len(v)):
        new_list.append(s * v[i])
    return new_list

# Question 7
def dot_product(u, v):
    """ Take two lists of numbers of the same length, 
    and returns the sum of the products of the corresponding elements of each (the dot_product). """
    dot_product = 0
    for i in range(0, len(u)):
        dot_product += u[i] * v[i]
    return dot_product

# Question 8
def cross_product(u, v):
    """ Take two lists of numbers of length 3 and returns their cross product. """
    new_vector = [u[1]*v[2] - u[2]*v[1], 
                    u[2]*v[0] - u[0]*v[2], 
                    u[0]*v[1] - u[1]*v[0]]
    return new_vector

# Question 10
def replace(s, old, new):
    """ Replace all occurrences of old with new in a string s. """
    return new.join(s.split(old))


test_suite()