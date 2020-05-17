import unittest


def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    pass


class TestFactorize(unittest.TestCase):
    """ Class for testing the function factorize """

    def test_wrong_types_raise_exception(self):
        """ Type arguments float and string will call TypeError """

        x = ('string', 1.5)
        for value in x:
            with self.subTest(x=value):
                self.assertRaises(TypeError, factorize, value)

    def test_negative(self):
        """ Numbers negative will call ValueError"""

        x = (-1, -10, -100)
        for value in x:
            with self.subTest(x=value):
                self.assertRaises(ValueError, factorize, value)

    def test_zero_and_one_cases(self):
        """ Integer numbers 1 and 0 will return of tuples (1,) and (0,)"""

        x = (0, 1)
        for value in x:
            with self.subTest(x=value):
                self.assertEqual(factorize(value), (value,))

    def test_simple_numbers(self):
        """ For prime numbers will return tuple
            that contains of one this number

        """

        x = (3, 13, 29)
        for value in x:
            with self.subTest(x=value):
                self.assertEqual(factorize(value), (value,))

    def test_two_simple_multipliers(self):
        """ Numbers for which the factorize
            function returns a tuple of size 2

        """

        x = (
            (6, (2, 3)),
            (26, (2, 13)),
            (121, (11, 11))
            )
        for value in x:
            inp_d, extended = value[0], value[1]
            with self.subTest(x=value):
                self.assertEqual(factorize(inp_d), extended)

    def test_many_multipliers(self):
        """ Numbers for which the factorize
            function returns a tuple of size >2
            
        """

        x = (
            (1001, (7, 11, 13)),
            (9699690, (2, 3, 5, 7, 11, 13, 17, 19)),
            )
        for value in x:
            inp_d, extended = value[0], value[1]
            with self.subTest(x=value):
                self.assertEqual(factorize(inp_d), extended)


if __name__ == "__main__":
    unittest.main()
