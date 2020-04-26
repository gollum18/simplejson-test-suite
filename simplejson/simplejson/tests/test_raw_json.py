# Name: test_raw_json.py
# Since: April 13th, 2020
# Author: Christen Ford
# Purpose: Performs unit testing on the simplejson.raw_json module.

from unittest import TestCase

import simplejson.raw_json as raw_json


class TestRAWJson(TestCase):
    """Implements unit testing on the simplejson.raw_json module.
    The unit testing performed by this module makes sane attempts
    to be as thorough as possible, but it is not exhaustive.
    """

    def test_create(self):
        """
        Description: Tests that the RawJSON:__init__() function
        correctly wraps a valid JSON string for output.

        Input:
            (str): "[0, 1, {"id": "0001", "test": "test-0065"}]"

        Output:
            (RawJSON): A RawJson object that wraps the input
            string.

        Test Case: Corresponds to test case TEST-0086.
        """
        test_input = "[0, 1, {\"id\": \"0001\", \"test\": \"test-0065\"}]"

        inst = raw_json.RawJSON(test_input)
        self.assertEqual(test_input, inst.encoded_json)
