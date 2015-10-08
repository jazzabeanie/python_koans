#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutTuples(Koan):
    def test_creating_a_tuple(self):
        count_of_three = (1, 2, 5) # so far the same a list, but () instead of []
        self.assertEqual(5, count_of_three[2])

    def test_tuples_are_immutable_so_item_assignment_is_not_possible(self):
        count_of_three = (1, 2, 5)
        try:
            count_of_three[2] = "three"
        except TypeError as ex:
            self.assertMatch('item', ex[0])

    def test_tuples_are_immutable_so_appending_is_not_possible(self):
        count_of_three = (1, 2, 5)
        try:
            count_of_three.append("boom")
        except Exception as ex:
            self.assertEqual(AttributeError, type(ex))

            # Note, assertMatch() uses regular expression pattern matching,
            # so you don't have to copy the whole message.
            self.assertMatch("attribute", ex[0])

        # Tuples are less flexible than lists, but faster.

    def test_tuples_can_only_be_changed_through_replacement(self):
        count_of_three = (1, 2, 5)

        list_count = list(count_of_three)
        list_count.append("boom")
        count_of_three = tuple(list_count) #this is how you turn a list into a tuple
        #so the value of the variable can be changed but the tuple itself cannot??

        self.assertEqual((1, 2, 5, "boom"), count_of_three)

    def test_tuples_of_one_look_peculiar(self):
        #self.assertEqual(type((1)), (1).__class__) #just testing what .__class__ does
        self.assertEqual(int, (1).__class__) # this is an integer
        self.assertEqual(tuple, (1,).__class__)
        self.assertEqual(("Hello comma!", ), ("Hello comma!", )) #what does this line show??

    def test_tuple_constructor_can_be_surprising(self):
        self.assertEqual(('S', 'u', 'r', 'p', 'r', 'i', 's', 'e', '!'), tuple("Surprise!")) # creating a tuppel with a string (what if there were commas inside the string??) will do the above. Better to get the syntax right. But this only applies to the tuple() funtion. just doing ("abc") will create a string.
        #when I try this in a python terminal, "variable = tuple("blah", )", it doesn't work. why??
    def test_creating_empty_tuples(self):
        self.assertEqual((), ())
        self.assertEqual((), tuple())  # Sometimes less confusing
        # Why would you create an empty tuple??

    def test_tuples_can_be_embedded(self):
        lat = (37, 14, 6, 'N')
        lon = (115, 48, 40, 'W')
        place = ('Area 51', lat, lon)
        self.assertEqual(('Area 51', (37, 14, 6, 'N'), (115, 48, 40, 'W')), place)

    def test_tuples_are_good_for_representing_records(self):
        locations = [
            ("Illuminati HQ", (38, 52, 15.56, 'N'), (77, 3, 21.46, 'W')),
            ("Stargate B", (41, 10, 43.92, 'N'), (1, 49, 34.29, 'W')),
        ]

        locations.append(
            ("Cthulhu", (26, 40, 1, 'N'), (70, 45, 7, 'W'))
        )

        self.assertEqual('Cthulhu', locations[2][0]) # this is the position 0 element within the position 2 element. so each subsequent number is the position within the tuple found at the current location. Each subsequent number essentially runs the __getitem__ method on the item before it. How does this __getitem__ work??
        self.assertEqual(15.56, locations[0][1][2])
