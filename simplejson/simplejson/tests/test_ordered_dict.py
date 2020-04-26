# Name: test_ordered_dict.py
# Since: April 13th, 2020
# Author: Christen Ford
# Purpose: Performs unit testing on the simplejson.ordered_dict
#	module.

from unittest import TestCase

import simplejson.ordered_dict as ordered_dict


class TestOrderedDict(TestCase):
    """Implements unit tests on the simplejson.ordered_dict
    module. The tests performed by this module make sane
    attempts at being as thorough as possible, but they are
    not exhaustive.
    """

    std_input = dict()
    std_input["abc"] = 0
    std_input["def"] = 1
    std_input["ghi"] = 2

    @classmethod
    def get_test_dict(cls):
        return ordered_dict.OrderedDict(TestOrderedDict.std_input)

    def test_create(self):
        """
        Description: Tests that the OrderedDict:__init__()
        function returns an OrderedDict created from a mapping
        containing the following key-value pairs:
        {"abc": 0, "def": 1, "ghi": 2}.

        Input:
            (mapping): {"abc": 0, "def": 1, "ghi": 2}

        Output:
            (OrderedDict): An instance of an OrderedDict
            containing the following mappings:
            {"abc": 0, "def": 1, "ghi": 2}.

        Test Case: Corresponds to test case TEST-0068.
        """
        od = TestOrderedDict.get_test_dict()

    # TODO: Test that the od was constructed correctly

    def test_clear(self):
        """
        Description: Test that the OrderedDict:clear()
        function correctly empties an OrderedDict containing the
        following mappings: {"abc": 0, "def": 1, "ghi": 2}.

        Input: This function accepts no input.

        Output: This function produces no output.

        Test Case: Corresponds to test case TEST-0069.
        """
        od = TestOrderedDict.get_test_dict()
        self.assertNotEqual(len(od), 0)
        od.clear()
        self.assertEqual(len(od), 0)

    def test_set_item(self):
        """
        Description: Tests that the OrderedDict:__setitem__()
        magic method correctly inserts a key-value pair into
        an empty ordered dictionary.

        Input:
            (str, int): ("test-0070", -1)

        Output: This function produces no output.

        Test Case: Corresponds to test case TEST-0070.
        """
        od = ordered_dict.OrderedDict()
        self.assertNotIn("test-0070", od.keys())
        self.assertNotIn(-1, od.values())
        od["test-0070"] = -1
        self.assertIn("test-0070", od.keys())
        self.assertIn(-1, od.values())

    def test_del_item(self):
        """
        Description: Tests that the OrderedDict:__delitem__()
        magic method correctly removes a key-value pair from
        an OrderedDict containing the following mappings:
        {"test-0070": 0, "test-0071": 1, "test-0072": 2}.

        Input:
            (str): "test-0070"

        Output: This function produces no output.

        Test Case: Corresponds to test case TEST-0071.
        """
        od = ordered_dict.OrderedDict()
        od["test-0070"] = -1
        self.assertIn("test-0070", od.keys())
        self.assertIn(-1, od.values())
        del od["test-0070"]
        self.assertNotIn("test-0070", od.keys())
        self.assertNotIn(-1, od.values())

    def test_iter(self):
        """
        Description: Tests that the OrderedDict:__iter__()
        magic method returns a generator function that yields
        keys from an ordered dictionary containing
        the following mappings:
        {"abc": 0, "def": 1, "ghi": 2}.

        Input: This function accepts no input.

        Output:
            (generator): A generator function that yields
            keys pairs in the following order:
            0, 1, 2.

        Test Case: Corresponds to test case TEST-0072.
        """
        test_output = ["abc", "def", "ghi"]
        od = TestOrderedDict.get_test_dict()
        index = 0
        for key in od.__iter__():
            k = test_output[index]
            self.assertEqual(k, key)
            index += 1

    def test_reversed(self):
        """
        Description: Tests that the OrderedDict:__reversed__()
        magic method returns a generator function that yields
        keys in reverse order from an ordered dictionary
        containing the following mappings:
        {"abc": 0, "def": 1, "ghi": 2}.

        Input: This function accepts no input.

        Output:
            (generator): A generator function that yields
            keys in the following order:
            2, 1, 0.

        Test Case: Corresponds to test case TEST-0073.
        """
        test_output = ["ghi", "def", "abc"]
        od = TestOrderedDict.get_test_dict()
        index = 0
        for key in od.__reversed__():
            k = test_output[index]
            self.assertEqual(k, key)
            index += 1


    def test_pop_item_rear(self):
        """Description: Tests that the OrderedDict:popitem()
        function returns the last key-value pair in an OrderedDict
        consisting of the following mappings:
        {"abc": 0, "def": 1, "ghi": 2}.

        Input:
            (boolean): True

        Output:
            (str, int): ("ghi", 2)

        Test Case: Corresponds to test case TEST-0074.
        """
        test_output = ("ghi", 2)
        od = TestOrderedDict.get_test_dict()
        self.assertEqual(od.popitem(True), test_output)

    def test_pop_item_front(self):
        """
        Description: Tests that the OrderedDict:popitem()
        function returns the first key-value pair in an
        OrderedDict consisting of the following key-value
        mappings: {"abc": 0, "def": 1, "ghi": 2}.

        Input:
            (boolean): False

        Output:
            (str, int): ("abc", 0)

        Test Case: Corresponds to test case TEST-0075.
        """
        test_output = ("abc", 0)
        od = TestOrderedDict.get_test_dict()
        self.assertEqual(od.popitem(False), test_output)

    def test_reduce(self):
        """
        Description: Tests that the OrderedDict:__reduce__()
        function works correctly.

        Input: This function accepts no input.

        Output:
            (OrderedDict, list): A Tuple consisting of a class
            reference to an OrderedDict containing the following
            mappings: {"abc": 0, "def": 1, "ghi": 2}, as well
            as a list of all key-value entries in the ordered
            dictionary.

        Test Case: Corresponds to test case TEST-0076.
        """
        test_output = (ordered_dict.OrderedDict, ([['abc', 0], ['def', 1], ['ghi', 2]],))
        od = TestOrderedDict.get_test_dict()
        self.assertEqual(od.__reduce__(), test_output)


    def test_keys(self):
        """
        Description: Tests that the OrderedDict:keys() function
        returns athe correct list of keys from an ordered
        dictionary via a generator function.

        Input: This function accepts no input.

        Output:
            (generator): A generator that yields the following
            keys in this order: "abc", "def", "ghi".

        Test Case: Corresponds to test case TEST-0077.
        """
        test_output = ["abc", "def", "ghi"]

        od = TestOrderedDict.get_test_dict()
        index = 0
        for key in od.keys():
            self.assertEqual(key, test_output[index])
            index += 1


    def test_repr(self):
        """
        Description: Tests that __repr__() returns the
        correct string representation of an OrderedDict.

        Input: This function accepts no input.

        Output:
            (str): A string representation of an OrderedDict
            containing the following mappings:
            {"abc": 0, "def": 1, "ghi": 2}.

        Test Case: Corresponds to test case TEST-0078.
        """
        od = TestOrderedDict.get_test_dict()
        rep = str(od)
        # TODO: Testing needs performed here as well


    def test_copy(self):
        """
        Description: Tests that the OrderedDict:copy() function
        returns a copy of an ordered dictionary.

        Input:
            (OrderedDict): An OrderedDict containing the
            following mappings: {"abc": 0, "def": 1, "ghi": 2}.

        Output:
            (OrderedDict): An identical OrderedDict to the
            input OrderedDict containing the following mappings:
            {"abc": 0, "def": 1, "ghi": 2}.

        Test Case: Corresponds to test case TEST-0079.
        """
        od = TestOrderedDict.get_test_dict()
        self.assertEqual(od, od.copy())


    def test_fromkeys_correct(self):
        """
        Description: Tests that the OrderedDict:fromkeys()
        function correctly constructs an ordered dictionary
        from a list of keys.

        Input:
            (list): ["abc", "def", "ghi"]

        Output:
            (OrderedDict): An OrderedDict containing the
            keys "abc", "def", "ghi".


        Test Case: Corresponds to test case TEST-0080.
        """
        test_input = ["abc", "def", "ghi"]
        od = ordered_dict.OrderedDict.fromkeys(test_input)
        index = 0
        for key in od.keys():
            self.assertEqual(key, test_input[index])
            index += 1

    def test_fromkeys_empty_list(self):
        """
        Description: Tests that the OrderedDict:fromkeys()
        function correctly constructs an ordered dictionary
        from an empty list of keys.

        Input:
            (list): An empty list.

        Output:
            (OrderedDict): An OrderedDict containing no
            key-value pairs.

        Test Case: Corresponds to test case TEST-0081.
        """
        od = ordered_dict.OrderedDict.fromkeys([])
        self.assertEqual(len(od), 0)

    def test_equals_true(self):
        """
        Description: Tests that the OrderedDict:__eq__() function
        correctly identifies an equal ordered dictionary.

        Input:
            (OrderedDict, OrderedDict): The first OrderedDict
            should have identical key-value pairs to the
            second OrderedDict.

        Output:
            (boolean): True

        Test Case: Corresponds to test case TEST-0082.
        """
        od = TestOrderedDict.get_test_dict()
        other = TestOrderedDict.get_test_dict()
        self.assertEqual(od.__eq__(other), True)

    def test_equals_false(self):
        """
        Description: Tests that the OrderedDict:__eq__() function
        correctly identifies a non-equal ordered dictionary.

        Input:
            (OrderedDict, OrderedDict): The first OrderedDict
            should have different key-value pairs from the
            second OrderedDict.

        Output:
            (boolean): False

        Test Case: Corresponds to test case TEST-0083.
        """
        od = TestOrderedDict.get_test_dict()
        other = ordered_dict.OrderedDict()
        self.assertEqual(od.__eq__(other), False)

    def test_not_equals_false(self):
        """
        Description: Tests that the OrderedDict:__ne__() function
        correctly identifies an equal ordered dictionary.

        Input:
            (OrderedDict, OrderedDict): The first OrderedDict
            should have identical key-value pairs to the
            second OrderedDict.

        Output:
            (boolean): False

        Test Case: Corresponds to test case TEST-0084.
        """
        od = TestOrderedDict.get_test_dict()
        other = TestOrderedDict.get_test_dict()
        self.assertEqual(od.__ne__(other), False)

    def test_not_equals_true(self):
        """
        Description: Tests that the OrderedDict:__ne__() function
        correctly identifies a non-equal ordered dictionary.

        Input:
            (OrderedDict, OrderedDict): The first OrderedDict
            should have different key-value pairs from the
            second OrderedDict.

        Output:
            (boolean): True

        Test Case: Corresponds to test case TEST-0085.
        """
        od = TestOrderedDict.get_test_dict()
        other = ordered_dict.OrderedDict()
        self.assertEqual(od.__ne__(other), True)
