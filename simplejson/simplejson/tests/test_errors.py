# Name: test_errors.py
# Since: April 13th, 2020
# Author: Christen Ford
# Purpose: Performs unit testing on the simplejson.errors module.

from unittest import TestCase

import simplejson.errors as errors


class TestErrors(TestCase):
    """Implements unit testing on the simplejson.errors module.
    The test implemented by this module make sane attempts at
    being as thorough as possible but are not exhaustive.
    """

    def test_linecol_correct(self):
        """
        Description: Tests that linecol() returns a correct
        tuple given correct parameters.

        Input:
            (str, int): ("{]", 1)

        Output:
            (int, int): A tuple consisting of the line number
            and column number.

        Test Case: Corresponds to test case TEST-0049.
        """
        test_input = ["{]", 1]
        out = errors.linecol(*test_input)
        self.assertIsInstance(out[0], int)
        self.assertIsInstance(out[1], int)
        # TODO: Test the values in out


    def test_linecol_none(self):
        """
        Description: Tests that linecol() raises an error when
        given the Python None type as the JSON document.

        Input:
            (None, int): (None, 0)

        Output:
            (BaseError): An error.

        Test Case: Corresponds to test case TEST-0050.
        """
        test_input = [None, 0]
        self.assertRaises(
            BaseException,
            errors.linecol,
            *test_input
        )


    def test_errmsg_correct(self):
        """
        Description: Tests that errmsg() properly formats an
        error message given correct parameters.

        Input:
            (str, str, int): ("Invalid closing brace!", "[}", 1)

        Output:
            (str): A formatted error message.

        Test Case: Corresponds to test case TEST-0051.
        """
        test_input = ["Invalid closing brace!", "[}", 1]
        self.assertIsInstance(errors.errmsg(*test_input), str)


    def test_errmsg_iindex(self):
        """
        Description: Tests that errmsg() fails when given an
        invalid starting index.

        Input:
            (str, str, int): ("Invalid closing brace!", "[}", -1)

        Output:
            (BaseError): An error.

        Test Case: Corresponds to test case TEST-0052.
        """
        test_input = ["Invalid closing brace!", "[}", -1]
        self.assertRaises(
            BaseException,
            errors.JSONDecodeError,
            *test_input
        )


    def test_create_correct(self):
        """
        Description: Tests that the JSONDecodeError:__init__()
        function properly formats an error message given
        correct parameters.

        input:
            (str, str, int): ("Invalid closing brace!", "[}", 1)

        Output:
            (str): A formatted error message.

        Test Case: Corresponds to test case TEST-0053.
        """
        test_input = ["Invalid closing brace!", "[}", 1]
        err = errors.JSONDecodeError(*test_input)
        self.assertIsInstance(err, errors.JSONDecodeError)


    def test_create_iindex(self):
        """
        Description: Tests that the JSONDecodeError:__init__()
        function fails when given an invalid starting index.

        Input:
            (str, str, int): ("Invalid closing brace!", "[}", -1)

        Output:
            (BaseError): An error.

        Test Case: Corresponds to test case TEST-0054.
        """
        test_input = ["Invalid closing brace!", "[}", -1]
        self.assertRaises(
            BaseException,
            errors.JSONDecodeError,
            *test_input
        )


    def test_reduce(self):
        """
        Description: Tests that the JSONDecodeError:__reduce__()
        function produces correct output.

        Input: This function does not accept input.

        Output:
            (JSONDecodeError, str, str, int, int): A Tuple
            consisting of a JSONDecodeError instance reference,
            an error message, the JSON document, the starting
            index and ending index.

        Test Case: Corresponds to test case TEST-0055.
        """
        err = errors.JSONDecodeError(
            msg="Invalid closing brace!",
            doc="[}",
            pos=1
        )
        test_output = (errors.JSONDecodeError, ('Invalid closing brace!', '[}', 1, None))
        state = err.__reduce__()
        self.assertEqual(state, test_output)
