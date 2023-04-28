from unittest import TestCase
from nlp import GPT 

class TestNLP(TestCase):

    def test_date(self):

        # This test covers text based dates in partial sentence format.
        self.assertEqual(GPT.datetime_parser("The eleventh of november at ten o'clock"), "11-11 10:00")

        # This test covers instances where the user inputs a mixture of both numbers and words. 
        self.assertEqual(GPT.datetime_parser("The 26th of aug at 11.15"), "26-08 11:15")

        # This test covers when the parser needs to assume AM or PM. 
        self.assertEqual(GPT.datetime_parser("11th of Nov at 1 o'clock"), "11-11 13:00")
 
        # Checking that it will understand AM or PM when specified.
        self.assertEqual(GPT.datetime_parser("The thirteenth of april at 1AM"), "13-04 01:00")

        # A combination of the previous tests - to make sure it can handle multiple at once.
        self.assertEqual(GPT.datetime_parser("The 13th of dec at one o'clock"), "13-12 13:00")
