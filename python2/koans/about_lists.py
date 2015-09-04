#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrays in the Ruby Koans
#

from runner.koan import *


class AboutLists(Koan): # Koan is the parent class that AboutLists is a child of.
    def test_creating_lists(self): # self is wih ever object calls the test_creating_lists() method.
        empty_list = list()
        self.assertEqual(list, type(empty_list))
        self.assertEqual(0, len(empty_list))

    def test_list_literals(self):
        nums = list() # creates empty list
        self.assertEqual([], nums) # checks that nums is empty. Is this check redundant in real coding??
        # This is how you would print a cusom message in the case of an error.
        #try:
        #    self.assertEqual([1], nums)
        #except Exception:
        #    print "this no work because I smart and you stupid, and nums is an empty list"
        nums[0:] = [1] # lets the 0 position of the list equal 1
        self.assertEqual([1], nums) #check the content of nums

        nums[1:] = [2] # lets the 1 position (or the second position) of numbs be 2.
        self.assertEqual([1, 2], nums) # checks the value of nums.

        nums.append(333) # adds 333 on to the end of nums.
        self.assertEqual([1, 2, 333], nums) # checks the value of nums.
        # my just mucking around:
        #nums.append(444) 
        #lastpos =  len(nums) - 1
        #print nums[lastpos:]

    def test_accessing_list_elements(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual('peanut', noms[0])
        self.assertEqual('jelly', noms[3])
        self.assertEqual('jelly', noms[-1])
        self.assertEqual('butter', noms[-3])
        # print noms[-2] # just testing my understanding
    def test_slicing_lists(self):
        noms = ['peanut', 'butter', 'and', 'jelly']
         
        # in the following, [start:end+1], see https://stackoverflow.com/questions/509211/explain-pythons-slice-notation
        self.assertEqual(['peanut'], noms[0:1]) # starts at position 0, everything at position 1 and after is sliced off.
        self.assertEqual(['peanut', 'butter'], noms[0:2])
        self.assertEqual([], noms[2:2])
        self.assertEqual(['and', 'jelly'], noms[2:20])
        self.assertEqual([], noms[4:0])
        self.assertEqual([], noms[4:100])
        self.assertEqual([], noms[5:0])

    def test_slicing_to_the_edge(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(['and', 'jelly'], noms[2:])
        self.assertEqual(['peanut', 'butter'], noms[:2])

    def test_lists_and_ranges(self): # confused about range()?, see http://pythoncentral.io/pythons-range-function-explained/
        self.assertEqual(list, type(range(5)))
        self.assertEqual([0, 1, 2, 3, 4], range(5))
        self.assertEqual([5, 6, 7, 8], range(5, 9))

    def test_ranges_with_steps(self):
        self.assertEqual([0, 2, 4, 6], range(0, 8, 2))
        self.assertEqual([1, 4, 7], range(1, 8, 3))
        self.assertEqual([5, 1, -3], range(5, -7, -4))
        self.assertEqual([5, 1, -3, -7], range(5, -8, -4))

    def test_insertions(self):
        knight = ['you', 'shall', 'pass']
        knight.insert(2, 'not')
        self.assertEqual(['you', 'shall', 'not', 'pass'], knight)

        knight.insert(0, 'Arthur')
        self.assertEqual(['Arthur', 'you', 'shall', 'not', 'pass'], knight)

    def test_popping_lists(self):
        stack = [10, 20, 30, 40]
        stack.append('last')

        self.assertEqual([10, 20, 30, 40, 'last'], stack)

        popped_value = stack.pop()
        self.assertEqual('last', popped_value)
        self.assertEqual([10, 20, 30, 40], stack)

        popped_value = stack.pop(1)
        self.assertEqual(20, popped_value)
        self.assertEqual([10, 30, 40], stack)

        # Notice that there is a "pop" but no "push" in python?

        # Part of the Python philosophy is that there ideally should be one and
        # only one way of doing anything. A 'push' is the same as an 'append'.

        # To learn more about this try typing "import this" from the python
        # console... ;)

    def test_use_deques_for_making_queues(self):
        from collections import deque

        queue = deque([1, 2]) # can't use queue = [1, 2] because this is a list and lists don't support popleft(). popleft() is part of the deque module and only applies to deque.
        queue.append('last')

        self.assertEqual([1, 2, 'last'], list(queue)) # checks the contents of queue. list(queue), turn the deque stored in queue into a list.
        
        testlist = list(queue)

        popped_value = queue.popleft() # removed the left most value and stores it to popped_value. normall lists don't support popleft().        
        self.assertEqual(1, popped_value)
        self.assertEqual([2, 'last'], list(queue))
        
        # my experiment to do the functions of popleft without using deque.
        # testpopped_value = testlist[0]
        # testlist = testlist[1:]
        # print testpopped_value
        # print testlist
