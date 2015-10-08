#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutSets(Koan):
    def test_sets_make_keep_lists_unique(self): #what does this mean??
        highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas',
            'MacLeod', 'Malcolm', 'MacLeod']

        there_can_only_be_only_one = set(highlanders)

        self.assertEqual(set(['MacLeod', 'Ramirez', 'MacLeod', 'Matunas', 'MacLeod', 'Malcolm', 'MacLeod']), there_can_only_be_only_one)

    def test_sets_are_unordered(self):
        self.assertEqual(set(['5', '4', '3', '2', '1']), set('12345'))

    def test_convert_the_set_into_a_list_to_sort_it(self): #sets have no order?
        self.assertEqual(['1', '2', '3', '4', '5'], sorted(set('13245'))) #sorted alphabetially??

    # ------------------------------------------------------------------

    def test_set_have_arithmetic_operators(self):
        scotsmen = set(['MacLeod', 'Wallace', 'Willie'])
        warriors = set(['MacLeod', 'Wallace', 'Leonidas'])

        self.assertEqual(set(['Willie']), scotsmen - warriors) #- means elements in scotsmen that aren't in warriors (basically taking away warriors if they exist)
        self.assertEqual(set(['MacLeod', 'Wallace', 'Willie', 'Leonidas']), scotsmen | warriors) #| mean elements in either
        self.assertEqual(set(['MacLeod', 'Wallace']), scotsmen & warriors) #& mean element in both
        self.assertEqual(set(['Willie', 'Leonidas']), scotsmen ^ warriors) #^ meanss elements in either s or t but not both

    # ------------------------------------------------------------------

    def test_we_can_query_set_membership(self):
        self.assertEqual(True, 127 in set([127, 0, 0, 1]))
        self.assertEqual(True, 'cow' not in set('apocalypse now'))
        #print set('apocalypse now') # this shows how sets work (how they are constructed. The sorting appears to be alphabetically, except for the ' '. Why is that??
    def test_we_can_compare_subsets(self): #what is a subset
        self.assertEqual(True, set('cake') <= set('cherry cake')) # <= means .isasubset()
        self.assertEqual(True, set('cake').issubset(set('cherry cake')))

        self.assertEqual(False, set('cake') > set('pie'))
