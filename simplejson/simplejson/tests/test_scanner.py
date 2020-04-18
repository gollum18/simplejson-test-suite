# Name: test_scanner.py
# Since: April 13th, 2020
# Author: Christen Ford
# Purpose: Performs unit testing on the simplejson.scanner module.

# NOTES:
"""
	-- Removed test cases 0089, 0090, and 0091 as they are 
	redundant since _scan_once() is called by the scan_once()
	function anyway.
"""

from unittest import TestCase

import simplejson.decoder as decoder
import simplejson.errors as errors
import simplejson.scanner as scanner


class ScannerContext(object):
	"""Defines a context object utilized by several test
	classes to configure a scanner.
	"""

	def __init__(self, parse_object=decoder.JSONObject, 
			parse_array=decoder.JSONArray, 
			parse_string=decoder.scanstring,
			match_number=scanner.NUMBER_RE.match, encoding=None,
			strict=True, parse_float=None, parse_int=None,
			parse_constant=None, object_hook=None,
			object_pairs_hook=None, memo={}):
		"""Returns an instance of a ScannerContext object.

		Args:

		Returns:
			(ScannerContext): A ScannerContext object.
		"""
		self.parse_object = parse_object
		self.parse_array = parse_array
		self.parse_string = parse_string
		self.match_number = match_number
		self.encoding = encoding
		self.strict = strict
		self.parse_float = parse_float
		self.parse_int = parse_int
		self.parse_constants = parse_constants
		self.object_hook = object_hook
		self.object_pairs_hook = object_pairs_hook
		self.memo = memo


class TestScanner(UnitTest):
	"""Implements unit testing on the simplejson.scanner module.
	The tests performed by this module make sane attempts to be
	as thorough as possible but are not exhaustive.
	"""

	def test_make_scanner_correct(self):
		"""
		Description: Ensures that the py_make_scanner() function
		correctly configures the scan_once() function with
		the correct parameters.

		Input: A context containing default values for each
		member. 

		Output: An instance of the py_make_scanner:scan_once()
		function.

		Test Case: Corresponds to test case TEST-0087.
		"""
		context = ScannerContext()
		scan_once = scanner.py_make_scanner(context)
		# NOTE: This may not be the correct test
		self.assertIsInstance(scan_once, scanner.scan_once)


	def test_make_scanner_none(self):
		"""
		Decription: Ensures that the py_make_scanner() function
		errors out when given a None type context parameter.

		Input: 
			This test case accepts no input.

		Output: 
			(Error)

		Test Case: Corresponds to test case TEST-0088.
		"""
		context = None
		self.assertRaises(
			TypeError, # should raise a TypeError
			scanner.py_make_scanner, 
			context
		)


	def test_make_scanner_scan_once_correct(self):
		"""
		Description: Tests that the py_make_scanner:scan_once()
		function properly scans a JSON token given correct
		parameters.
	
		Input:
			(str, int): ("["abc", "def", "ghi"]", 0)

		Output:
			(list): ["abc", "def", "ghi"]

		Test Case: Corresponds to test case TEST-0092.
		"""
		test_input "[\"abc\", \"def\", \"ghi\"]"
		test_output = ["abc", "def", "ghi"]

		context = ScannerContext()
		scan_once = scanner.py_make_scanner(context)
		output, _ = scan_once(test_input, 0)

		self.assertEquals(output, test_output)


	def test_make_scanner_scan_once_none(self):
		"""
		Description: Tests that the py_make_scanner:scan_once()
		function errors out when given a None type as the input
		string.

		Input:
			(None, int): (None, 0)

		Output:
			(JSONDecodeError)

		Test Case: Corresponds to test case TEST-0093.
		"""
		test_input = (None, 0)

		context = ScannerContext()
		scan_once = scanner.py_make_scanner(context)
		
		self.assertRaises(
			errors.JSONDecodeError, 
			scan_once(),
			test_input[0],
			test_input[1]
		)


	def test_make_scanner_scan_once_iindex(self):
		"""
		Description: Tests that the py_make_scanner:scan_once()
		function errors out when given a valid JSON string as the
		input string and an invalid index.

		Input:
			(str, int): ("["abc", "def", "ghi"]", -1)

		Output:
			(JSONDecodeError)

		Test Case: Corresponds to test case TEST-0094.
		"""
		test_input = ("[\"abc\", \"def\", \"ghi\"]", -1)
		
		context = ScannerContext()
		scan_once = scanner.py_make_scanner(context)

		self.assertRaises(
			errors.JSONDecodeError,
			scan_once,
			test_input[0],
			test_input[1]
		)

