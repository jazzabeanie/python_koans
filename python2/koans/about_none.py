#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutNil in the Ruby Koans
#

from runner.koan import *


class AboutNone(Koan):

    def test_none_is_an_object(self):
        "Unlike NULL in a lot of languages"
        self.assertEqual(True, isinstance(None, object)) # so isinstance(1, 2) checks whether 1 is an type of 2, so what else can 2 be??

    def test_none_is_universal(self):
        "There is only one None"
        self.assertEqual(True, None is None) #is "is" a function?? what do you call it?apparently you use == when comparing values and is when comparing identities. An identitiy is something that is unique to every object.

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
            # self.assertEqual(AttributeError, labh) #should this be a NameError?? need to see if I can test for a NameError, might need a new try except statement. How do I end the current one I am in??
            # end my experiment
            self.assertEqual(AttributeError, ex.__class__) # When I originally tried this I got a name error because I tried it in a separate Python session where ex had not been definied. Here it's been defined with the "except Exceptions as ex:" line.

            # What message was attached to the exception?
            # (HINT: replace __ with part of the error message.)
            self.assertMatch(__, ex.args[0]) #what does assertMatch do? I can't tell rom the /runner/koan.py file. I think self.args[] does someting about regular expressions.

    def test_none_is_distinct(self):
        """
        None is distinct from other things which are False.
        """
        self.assertEqual(____, None is not 0)
        self.assertEqual(____, None is not False)
