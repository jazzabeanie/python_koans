#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutExceptions(Koan):

    class MySpecialError(RuntimeError): #this creates an empty class called MySpecialError, which is a subclass of RuntimeError.
        pass

    def test_exceptions_inherit_from_exception(self):
        mro = self.MySpecialError.__mro__ #__mro__ is built in. for more info on __mro__, see python docs. __mro__ is a list (every class has one), which contains the data about what the parent classes are of the object. So basically this line says mro = __mro__ for this object.
        self.assertEqual('RuntimeError', mro[1].__name__) #mro[1] is the first parent
        self.assertEqual('StandardError', mro[2].__name__) #mro[2] is the grandparent 
        self.assertEqual('Exception', mro[3].__name__) #mro[3] is the great grandparent
        self.assertEqual('BaseException', mro[4].__name__) #mro[4] is the great great grandparnet, so esentially everything above is a subclass of BaseException. See "BaseException" in python docs for more info.

    def test_try_clause(self):
        result = None
        try:
            self.fail("Oops") #I originaly though that this generated an error because the method hadn't been defined. But when I tried to pass in two arguments, I got an AssertionError: 'Oops' != 'fail() takes at most 2 arguments (3 given)' I think self is counted.
        except StandardError as ex: #not sure why there is an error because I don't understand the funtction. Maybe the fail() method is designs to throw a standard Error.
            result = 'exception handled'

        self.assertEqual('exception handled', result)

        self.assertEqual(True, isinstance(ex, StandardError)) #must be true, otherwise line 26 would not have passed
        self.assertEqual(False, isinstance(ex, RuntimeError)) #RuntumeError is an instance of StandardError, not the other way around.

        self.assertTrue(issubclass(RuntimeError, StandardError), \
            "RuntimeError is a subclass of StandardError")
        self.assertEqual("Oops", ex[0]) #I tried to see what ex[1] does it I got an IndexError: typle index out of range. I think that whatever this error is, it stores the arguments passed into the fail method as a tuple.

    def test_raising_a_specific_error(self):
        result = None
        try:
            raise self.MySpecialError, "My Message" #what is my message? will this display something like "MySpecialError: My Message"??
        except self.MySpecialError as ex:
            result = 'exception handled'

        self.assertEqual('exception handled', result)
        self.assertEqual("My Message", ex[0])

    def test_else_clause(self):
        result = None
        try:
            pass
        except RuntimeError:
            result = 'it broke'
            pass
        else:
            result = 'no damage done'

        self.assertEqual('no damage done', result)

    def test_finally_clause(self):
        result = None
        try:
            self.fail("Oops")
        except:
            # no code here
            pass
        finally:
            result = 'always run'

        self.assertEqual('always run', result)
