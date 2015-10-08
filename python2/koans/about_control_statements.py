#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutControlStatements(Koan):

    def test_if_then_else_statements(self):
        if True: #this translates to "if ____ == True", so this line says if True == True, then do this.
            result = 'true value'
        else:
            result = 'false value'
        self.assertEqual('true value', result)

    def test_if_then_statements(self):
        result = 'default value'
        if True: 
            result = 'true value'
        self.assertEqual('true value', result)
        
    def test_if_then_elif_else_statements(self):
        if False:
            result = 'first value'
        elif True: 
            result = 'true value'
        else:
            result = 'default value'
        self.assertEqual('true value', result) 
    
    def test_my_understanding_of_if_statements(self):
        x = True
        if x:
            result =  "you might actually understand this"
        else:
            result = "you lose!"
        self.assertEqual("you might actually understand this", result)
        

    def test_while_statement(self):
        i = 1
        result = 1
        while i <= 10:
            result = result * i
            i += 1
        self.assertEqual(3628800, result)

    def test_break_statement(self):
        i = 1
        result = 1
        while True: 
            if i > 10: break #break stopes the while statement and skips the else statement if there is one.
            result = result * i
            i += 1
        self.assertEqual(3628800, result)

    def test_continue_statement(self):
        i = 0
        result = []
        while i < 10:
            i += 1
            if (i % 2) == 0: continue #continues means repeat the loop. break means stop the loop. So this if statement will only continue to result.append if "if" statement is false. "else" is implied.
            result.append(i)
        self.assertEqual([1, 3, 5, 7, 9], result)

    def test_for_statement(self):
        phrase = ["fish", "and", "chips"]
        result = []
        for item in phrase: #translates to "for each item in the phrase"
            result.append(item.upper())
        self.assertEqual(["FISH", "AND", "CHIPS"], result)

    def test_for_statement_with_tuples(self):
        round_table = [
            ("Lancelot", "Blue"),
            ("Galahad", "I don't know!"),
            ("Robin", "Blue! I mean Green!"),
            ("Arthur", "Is that an African Swallow or Amazonian Swallow?")
        ]
        result = []
        for knight, answer in round_table: #does this line declare the variables as the first and second items of the tuples?
            result.append("Contestant: '" + knight + \
            "'   Answer: '" + answer + "'")

        text = "Contestant: 'Robin'   Answer: 'Blue! I mean Green!'"

        self.assertMatch(text, result[2])

        self.assertNoMatch(text, result[0])
        self.assertNoMatch(text, result[1])
        self.assertNoMatch(text, result[3])
