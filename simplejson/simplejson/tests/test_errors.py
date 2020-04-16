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
		Description: Test that linecol() returns a correct 
		tuple indicating the line and column number an 
		error occurred.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0049.
		"""
		raise NotImplementedError

	def test_linecol_none(self):
		"""
		Description: Tests that linecol() raises an error 
		when given the None type.

		Input:

		Output:
		
		Test Case: Corresponds to test case TEST-0050.
		"""
		raise NotImplementedError

	def test_errmsg_correct(self):
		"""
		Description: Tests that errmsg() returns a formatted 
		error message given correct parameters.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0051.
		"""
		raise NotImplementedError

	def test_errmsg_invalid(self):
		"""
		Description: Tests that errmsg() raises an error 
		when given an invalid starting index.

		Input:

		Output:
		
		Test Case: Corresponds to test case TEST-0052.
		"""
		raise NotImplementedError

	def test_create(self):
		"""
		Description: Tests that a JSONDecodeError can be 
		created from correct parameters.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0053.
		"""
		raise NotImplementedError

	def test_reduce(self):
		"""
		Description: Tests that __reduce__() of 
		JSONDecodeError works correctly.

		Input:

		Output:

		Tets Case: Corresponds to test case TEST-0054.
		"""
		raise NotImplementedError
