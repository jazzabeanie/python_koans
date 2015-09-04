#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutStringManipulation(Koan): # Koan refers to some object of which AboutStringManipulation is a child.

    def test_use_format_to_interpolate_variables(self): # self refers to whichever object calls this method, eg, example.test_use_format_to_interpolate_variables(). In this case, example is the self. See here for more info: https://stackoverflow.com/questions/6698030/what-does-self-do
        value1 = 'one'
        value2 = 2
        string = "The values are {0} and {1}".format(value1, value2) # this turns value1 and value2 into strings
        self.assertEqual('The values are one and 2', string)

    def test_formatted_values_can_be_shown_in_any_order_or_be_repeated(self):
        value1 = 'doh'
        value2 = 'DOH'
        string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
        self.assertEqual("The values are DOH, doh, doh and DOH!", string)

    def test_any_python_expression_may_be_interpolated(self):
        import math  # import a standard python module with math functions

        decimal_places = 4
        string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5), \
                # that backslash \ allows you to write stuff on the next line and python with interpret is as if it was on the one line. But you can't put a comment after it.
                decimal_places) # 0 referres to the frist argument. The colon : indicates that what follows is the format_spec. The period . indicates that what follows will specify precision, {1} is the 2nd argument which is the number of digits to display after (specified by f or F as opposed to g or G) the decimal point.
        #I could also do this using concatenation by calling math.sqrt(5) inside some rounding function.
        self.assertEqual("The square root of 5 is 2.2361", string)

    def test_you_can_get_a_substring_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual("let", string[7:10]) # this must take characters from (and including) the 7th up to (and not including) the 10th. remember that the first character is 0
    def test_you_can_get_a_single_character_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual("a", string[1])

    def test_single_characters_can_be_represented_by_integers(self):
        self.assertEqual(97, ord('a'))
        self.assertEqual(True, (ord('b') == (ord('a') + 1))) # originally I got confused her becasue the 2nd lot of parenthesis were missing. The comma make them redundant but I added them for readability.

    def test_strings_can_be_split(self):
        string = "Sausage Egg Cheese"
        words = string.split()
        self.assertEqual(["Sausage", "Egg", "Cheese"], words)

    def test_strings_can_be_split_with_different_patterns(self):
        import re  # import python regular expression library

        string = "the,rain;in,spain"
        pattern = re.compile(',|;') # re is regular expresssion. compile is a function that takes the patter in the argument, and converts it in to an object which have methods attached to them such as serach and replace. See here for more info: https://docs.python.org/2/howto/regex.html#compiling-regular-expressions. | splits the regular expression into two and either can be matched. So this says, patern is equal to , or ;.
        words = pattern.split(string) # I thought split() was a re module function, but it is used in test_strings_can_be_split(self) method before re is imported.

        self.assertEqual(["the", 'rain', 'in', 'spain'], words)

        # `pattern` is a Python regular expression pattern which matches
        # ',' or ';'
       
        # this is my own test. I think this works because all strings have a split() method, and all re.compiled patterns have a split() method and they are defined differently so it depends on which object calls the method. So string.split() is different to patter.split()
        pattern2 = re.compile(':')
        string = 'some:words'
        self.assertEqual(string.split(':'), pattern2.split('some:words'))

    def test_raw_strings_do_not_interpret_escape_characters(self):
        string = r'\n' # r indicate that it's raw string literal. see more here: https://stackoverflow.com/questions/2081640/what-exactly-do-u-and-r-string-flags-do-in-python-and-what-are-raw-string-l
        self.assertNotEqual('\n', string) # this is a regualr string and \n is a newline.
        self.assertEqual(r'\n', string) # this is a raw string (designated by r, and there are no escape characters. \ means just a backslash, except when followed by a parenthesis character that would otherwise terminat the string.
        self.assertEqual(2, len(string)) # the two characters must be \ and n.
        # Useful in regular expressions, file paths, URLs, etc. This must mean useful for printing regular expressions, filepaths, etc.

        #my test
        import re
        string = """the
rain
in
spain"""
        pattern = re.compile(r'\n') # in this case it doesn't matter whether you use a regular or raw string. Is this because it is being compiled?? or because whether the split function uses an actual newline, or the raw \n form, it will still find the same thing??
        words = pattern.split(string) 
        self.assertEqual(["the", 'rain', 'in', 'spain'], words)

    def test_strings_can_be_joined(self):
        words = ["Now", "is", "the", "time"]
        self.assertEqual('Now is the time', ' '.join(words)) #Can it also be words.join(' '), no becuase 'list' object has no attribute 'join'. All string objects have a join method that take a list, and joing the items into a single string with the original string placed between.

    def test_strings_can_change_case(self):
        self.assertEqual('Guido sanchez', 'guido sanchez'.capitalize())
        self.assertEqual('GUIDO', 'guido'.upper())
        self.assertEqual('timbot', "TimBot".lower())
        self.assertEqual('Guido Van Rossum', 'guido van rossum'.title())
        self.assertEqual('tOtAlLy AwEsOmE', 'ToTaLlY aWeSoMe'.swapcase())
