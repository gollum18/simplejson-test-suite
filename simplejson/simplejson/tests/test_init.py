#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Name: test_init.py
# Since: April 13th, 2020
# Author: Christen Ford
# Purpose: Performs unit testing on the simplejson.__init__
#	module.

# TODO:
"""
	-- Figure out an invalid Python object for TEST-0057/0060.
"""

import os, pathlib
from unittest import TestCase

import simplejson
import simplejson.errors as errors


class StubClass(object):

    def __init__(self):
        pass


class TestInit(TestCase):
    load_test_file = "load.json"
    dump_test_file = "dump.json"

    def test_dump_correct(self):
        """
        Description: Tests that dump() functions correctly
        when given a valid Python object and file pointer.

        Input: A valid Python object and an open file pointer
        to an output file. Assume default values for the remainder
        of the optional parameters for the dump().

        Output: This function produces no output.

        Test Case: Corresponds to test case TEST-0056.
        """
        filepath = os.path.join("", TestInit.load_test_file)
        fp = open(filepath, "w")
        test_input = [1, 2, 3, 4, 5, {'a': 0, 'b': 1}]
        test_output = "[1, 2, 3, 4, 5, {'a': 0, 'b': 1}]"
        fp.write(str(test_input))
        fp.flush()
        fp.close()
        fp = open(filepath, "r")
        self.assertEqual(fp.readline(), test_output)
        fp.close()
        os.remove(filepath)


    def test_dump_invalid(self):
        """
        Description: Tests that dump() raises an error
        when given an invalid Python object.

        Input:

        Output:

        Test Case: Corresponds to test case TEST-0057.
        """
        filepath = os.path.join("", TestInit.load_test_file)
        fp = open(filepath, "w+")
        test_input = StubClass()
        test_input.abc = 1
        test_input.ghi = 2
        test_input.jkl = 3
        self.assertRaises(
            BaseException,
            simplejson.dump,
            test_input,
            fp
        )
        fp.close()
        os.remove(filepath)


    def test_dump_none(self):
        """
        Description: Tests that dump() raises an error
        when given the None type as the file pointer.

        Input: A valid Python object and None as the file
        pointer. Assume default values for the remainder of
        the optional parameters for dump().

        Output:
            (BaseError): An error.

        Test Case: Corresponds to test case TEST-0058.
        """
        self.assertRaises(
            BaseException,
            simplejson.dump,
            {}, None
        )


    def test_dumps_correct(self):
        """
        Description: Tests that dumps() returns a properly
        encoded JSON string given the following valid Python
        object: [1, 2, 3, 4, 5, {"a": 0, "b": 1}].

        Input:
            (list): A Python list consisting of the following
            elements: [1, 2, 3, 4, 5, {"a": 0, "b": 1}].

        Output:
            (str): A JSON string representing the input object.

        Test Case: Corresponds to test case TEST-0059.
        """
        test_input = [1, 2, 3, 4, 5, {"a": 0, "b": 1}]
        self.assertEqual(
            simplejson.dumps(test_input),
            '[1, 2, 3, 4, 5, {"a": 0, "b": 1}]'
        )


    def test_dumps_invalid(self):
        """
        Description: Tests that dumps() raises an error
        when given an invalid invalid Python object.

        Input:
            (Object): A Python object.

        Output:

        Test Case: Corresponds to test case TEST-0060.
        """
        # This should raise an error
        test_input = StubClass()
        test_input.abc = 1
        test_input.ghi = 2
        test_input.jkl = 3
        self.assertRaises(
            BaseException,
            simplejson.dumps,
            test_input
        )


    def test_dumps_none(self):
        """
        Description: Tests that dumps() raises an error
        when given the Python None type.

        Input:
            (None): None. Assume default parameters for the
            remaining optional parameters of the method.

        Output:
            (BaseError): An error.

        Test Case: Corresponds to test case TEST-0061.
        """
        self.assertRaises(
            BaseException,
            simplejson.dumps,
            None
        )


    def test_load_correct(self):
        """
        Description: Tests that load() can correctly
        parse a JSON document from a file. This test case should
        create the file on the fly from the following invalid
        JSON: “[0, 1, {'id': '0x1', 'test': 'test-0065'}]”.
        Also, make sure to delete the file when the test case
        is done using it.

        Input:
            (FILE*) A pointer to a file containing valid JSON.
            Assume default values for the rest of the optional
            parameters of the method.

        Output:
            (list): A list containing the following elements:
            [0, 1, {'id': '0x1', 'test': 'test-0065'}].

        Test Case: Corresponds to test case TEST-0062.
        """
        test_path = os.path.join("", TestInit.load_test_file)
        test_input = "[0, 1, {\"id\": \"0x1\", \"test\": \"test-0065\"}]"
        test_output = [0, 1, {"id": "0x1", "test": "test-0065"}]
        fp = open(test_path, "w")
        fp.write(test_input)
        fp.flush()
        fp.close()
        fp = open(test_path, "r")
        self.assertEqual(simplejson.load(fp), test_output)
        fp.close()
        os.remove(test_path)


    def test_load_invalid(self):
        """
        Description: Tests that load() raises an error
        when parsing a JSON document from a file containing
        invalid JSON. This test case should create the file
        on the fly from the following invalid JSON:
        “[0, 1, {'id': '0x1', 'test': 'test-0065'}}”. Also,
        make sure to delete the file when the test case is
        done using it.

        Input:
            (FILE*): A pointer to a file containing invalid JSON.
            Assume default values for the rest of the optional
            parameters of the method.

        Output:
            (JSONDecodeError)

        Test Case: Corresponds to test case TEST-0063.
        """
        test_input = "[0, 1, {\"id\": \"0x1\", \"test\": \"test-0065\"}}"
        test_path = os.path.join(".", TestInit.load_test_file)

        fp = open(test_path, "w")
        fp.write(test_input)
        fp.flush()
        fp.close()
        fp = open(test_path, "r")
        self.assertRaises(
            errors.JSONDecodeError,
            simplejson.load,
            fp
        )
        fp.close()
        os.remove(test_path)


    def test_load_empty(self):
        """
        Description: Tests that load() raises an error
        when attempting to parse a JSON document from
        an empty file.

        Input:

        Output:

        Test Case: Corresponds to test case TEST-0064.
        """
        test_path = os.path.join(".", TestInit.load_test_file)
        pathlib.Path(test_path).touch()
        fp = open(test_path)
        self.assertRaises(
            errors.JSONDecodeError,
            simplejson.load,
            fp
        )
        fp.close()
        os.remove(test_path)


    def test_loads_correct(self):
        """
        Description: Tests that loads() can correctly
        parse a JSON document from a string containing
        valid JSON.

        Input:
            (str): “[0, 1, {'id': '0x1', 'test': 'test-0065'}]”

        Output:
            (list): A list containing the following elements:
            [0, 1, {'id': '0x1', 'test': 'test-0065'}].

        Test Case: Corresponds to test case TEST-0065.
        """
        test_input = '[0, 1, {"id": "0x1", "test": "test-0065"}]'
        test_output = [0, 1, {'id': '0x1', 'test':'test-0065'}]
        self.assertEqual(
            simplejson.loads(test_input),
            test_output
        )


    def test_loads_invalid(self):
        """
        Description: Tests that loads() raises an error
        when attempting to parse a JSON document from a
        string containing invalid JSON.

        Input:
            (str): “[0, 1, {'id': '0x1', 'test': 'test-0065'}}”

        Output:
            (JSONDecodeError).

        Test Case: Corresponds to test case TEST-0066.
        """
        self.assertRaises(
            errors.JSONDecodeError,
            simplejson.loads,
            s='[0, 1, {"id": "0x1", "test": "test-0065"}}'
        )


    def test_loads_empty(self):
        """
        Description: Tests that loads() raises an error
        when attempting to parse a JSON document from an
        empty string.

        Input:
            (str): ""

        Output:
            (JSONDecodeError)

        Test Case: Corresponds to test case TEST-0067.
        """
        self.assertRaises(
            errors.JSONDecodeError,
            simplejson.loads,
            s=""
        )
