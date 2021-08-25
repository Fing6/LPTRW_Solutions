# Solutions of Chapter 8.(without q1)
import sys
import string

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
    test(count_letters("University", "i") == 2)
    test(count_letters("University", "a") == 0)
    test(count_letters("", "i") == 0)

    test(count_letters_2("University", "i") == 2)
    test(count_letters_2("University", "a") == 0)
    test(count_letters_2("", "i") == 0)

    test(reverse("happy") == "yppah")
    test(reverse("Python") == "nohtyP")
    test(reverse("") == "")
    test(reverse("a") == "a")

    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")

    test(remove_letter("a", "apple") == "pple")
    test(remove_letter("a", "banana") == "bnn")
    test(remove_letter("z", "banana") == "banana")
    test(remove_letter("i", "Mississippi") == "Msssspp")
    test(remove_letter("b", "") == "")
    test(remove_letter("b", "c") == "c")

    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome(""))    # Is an empty string a palindrome?  ---Yes.

    test(count("is", "Mississippi") == 2)
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2)
    test(count("nana", "banana") == 1)
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)

    test(remove("an", "banana") == "bana")
    test(remove("cyc", "bicycle") == "bile")
    test(remove("iss", "Mississippi") == "Missippi")
    test(remove("eggs", "bicycle") == "bicycle")

    test(remove_all("an", "banana") == "ba")
    test(remove_all("cyc", "bicycle") == "bile")
    test(remove_all("iss", "Mississippi") == "Mippi")
    test(remove_all("eggs", "bicycle") == "bicycle")

# Question 2:
# Modify the original function so that Ouack and Quack are spelled correctly.
def q2():
    prefixes = "JKLMNOPQ"
    suffix = "ack"
    for letter in prefixes:
        # modified part
        if letter == "O" or letter == "Q":
            print(letter + "u" + suffix)

        print(letter + suffix)

q2()

# Question 3:
# Generalize it so that it accepts the string and the letter as arguments.
# Make the function return the number of characters, rather than print the answer. 
# The caller should do the printing.
def count_letters(str, letter):
    count = 0 
    for char in str:
        if char == letter: 
            count += 1 
    return count

# Question 4:
# Rewrite the count_letters function so that instead of traversing the string,
# it repeatedly calls the find method, 
# with the optional third parameter to locate new occurrences of the letter being counted.
def find(strng, ch, start=0, end=None):
    ix = start
    if end is None:
       end = len(strng)
    while ix < end:
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

def count_letters_2(str, letter):
    count = 0
    # find the index of first appearing letter in str
    loc = find(str, letter)
    while True:
        # letter is not in str, break the loop
        if loc == -1:
            break
        count += 1
        # new start from str[loc + 1]
        loc = find(str, letter, loc + 1)
    return count

# Question 5:
# 1. Remove all punctuation from the string 
# 2. Break the string into a list of words 
# 3. Count the number of words in your text that contain the letter “e”. 
mytext = """
    Do not go gentle into that good night,
    Old age should burn and rave at close of day;
    Rage, rage against the dying of the light.

    Though wise men at their end know dark is right,
    Because their words had forked no lightning they
    Do not go gentle into that good night.

    Good men, the last wave by, crying how bright
    Their frail deeds might have danced in a green bay,
    Rage, rage against the dying of the light.

    Wild men who caught and sang the sun in flight,
    And learn, too late, they grieved it on its way,
    Do not go gentle into that good night.

    Grave men, near death, who see with blinding sight
    Blind eyes could blaze like meteors and be gay,
    Rage, rage against the dying of the light.

    And you, my father, there on the sad height,
    Curse, bless, me now with your fierce tears, I pray.
    Do not go gentle into that good night.
    Rage, rage against the dying of the light.
"""

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

def q5(text, letter):
    new_text = remove_punctuation(text)

    word_list = new_text.split()

    count = 0
    total_len = len(word_list)
    for word in word_list:
        count += count_letters_2(word, letter)
    percentage = count / total_len * 100.0

    analysis = 'Your text contains {0} words, of which {1} ({2:.1f}%) contain an "{3}".'
    print(analysis.format(total_len, count, percentage, letter))

q5(mytext, "e")

# *Question 6:
# Print a neat looking multiplication table.
def print_row(base, n):
    """ Print a row of the multiplication table. """
    for i in range(1, n + 1):
        print("{0:>4}".format(base * i), end="")
    print("")
        
def q6(n):
    # header
    print("     ", end="")
    print_row(1, n)
    # line
    print("    :" + "----" * n)
    # body
    for i in range(1, n + 1):
        print("{0:>4}:".format(i), end="")
        print_row(i, n)
        
q6(12)

# Question 7：
# Write a function that reverses its string argument.
def reverse(str):
    reversed_str = ""
    for char in str:
        reversed_str = char + reversed_str
    return reversed_str

# Question 8:
# Write a function that mirrors its argument.
def mirror(str):
    return str + reverse(str)

# Question 9:
# Write a function that removes all occurrences of a given letter from a string.
def remove_letter(letter, str):
    new_str = ""
    for char in str:
        if not char == letter:
            new_str += char
    return new_str

# Question 10:
# Write a function that recognizes palindromes.
def is_palindrome(str):
    return str == reverse(str)

# *Question 11:
# Write a function that counts how many times a substring occurs in a string.
def count(substr, str):
    count = 0
    segment = len(substr)
    for i in range(len(str) - segment + 1):
        if substr == str[i:i + segment]:
            count += 1
    return count
    
# *Question 12:
# Write a function that removes the first occurrence of a string from another string.
def remove(substr, str):   
    segment = len(substr)
    for i in range(len(str) - segment + 1):
        if substr == str[i:i + segment]:
            str = str[:i] + str[i + segment:]
            break
    return str

# *Question 13:
# Write a function that removes all occurrences of a string from another string.
def remove_all(substr, str):
    while True:
        temp = str
        str = remove(substr, str)
        if temp == str:
            break 
    return str

test_suite()