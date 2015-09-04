#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutNil in the Ruby Koans
#

from runner.koan import *


class AboutNone(Koan):

    def test_none_is_an_object(self):
        "Unlike NULL in a lot of languages"
        self.assertEqual(True, isinstance(None, object)) # so isinstance(1, 2) checks whether 1 is an type of 2, so what else can 2 be?? Does it also check if 1 is a child of 2?

    def test_none_is_universal(self):
        "There is only one None"
        self.assertEqual(True, None is None) #"is" is an operator, see here for more info: https://docs.python.org/2/reference/expressions.html#not-in. Apparently you use == when comparing values and is when comparing identities. An identitiy is something that is unique to every object.

    def test_what_exception_do_you_get_when_calling_nonexistent_methods(self):
        """
        What is the Exception that is thrown when you call a method that does
        not exist?

        Hint: launch python command console and try the code in the
        block below.

        Don't worry about what 'try' and 'except' do, we'll talk about
        this later
        """
        try:
            None.some_method_none_does_not_know_about()
        except Exception as ex:
            # What exception has been caught?
            #
            # Need a recap on how to evaluate __class__ attributes?
            #   https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute
            
            # start my experiment
            try:
                blah
            except Exception as excep:
                self.assertEqual(NameError, excep.__class__) # this is me testing my ability to produce a NameError. Python knows that I'm finished with the except section because of the indentation. Indentation and newlines matter in python.
            # end my experiment
            self.assertEqual(AttributeError, ex.__class__) # When I originally tried this I got a name error because I tried it in a separate Python session where ex had not been definied. Here it's been defined with the "except Exceptions as ex:" line.
            # What message was attached to the exception?
            # (HINT: replace __ with part of the error message.)
            self.assertMatch("NoneType", ex.args[0]) # Assert match takes the first argument and does a search through the second argument for a match. ex.args[] take the first argument of ex, which is the message of the exceptions.
            #What I gather from all this is that when you call an unknown method, you get an AttributeError that says "'__' object has not attribute '__'".

    def test_none_is_distinct(self):
        """
        None is distinct from other things which are False.
        """
        self.assertEqual(True, None is not 0)
        self.assertEqual(True, None is not False)
        # None is a NULL value. It is not equal to true or false or zero.
