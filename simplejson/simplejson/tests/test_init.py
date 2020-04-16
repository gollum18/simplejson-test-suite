# Name: test_init.py
# Since: April 13th, 2020
# Author: Christen Ford
# Purpose: Performs unit testing on the simplejson.__init__ 
#	module.

from unittest import TestCase

import simplejson

class TestInit(TestCase):

	def test_dump_correct(self):
		"""
		Description: Tests that dump() functions correctly 
		when given a valid Python object and file pointer.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0056.
		"""
		raise NotImplementedError

	def test_dump_invalid(self):
		"""
		Description: Tests that dump() raises an error 
		when given an invalid Python object.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0057.
		"""
		raise NotImplementedError

	def test_dump_none(self):
		"""
		Description: Tests that dump() raises an error 
		when given the None type as the file pointer.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0058.
		"""
		raise NotImplementedError

	def test_dumps_correct(self):
		"""
		Description: Tests that dumps() returns a properly 
		encoded JSON string given a valid Python object 
		and file pointer.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0059.
		"""
		raise NotImplementedError

	def test_dumps_invalid(self):
		"""
		Description: Tests that dumps() raises an error 
		when given an invalid invalid Python object.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0060.
		"""
		raise NotImplementedError

	def test_dumps_none(self):
		"""
		Description: Tests that dumps() raises an error 
		when given the Python None type.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0061.
		"""
		raise NotImplementedError

	def test_load_correct(self):
		"""
		Description: Tests that load() can correctly 
		parse a JSON document from a file.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0062.
		"""
		raise NotImplementedError

	def test_load_invalid(self):
		"""
		Description: Tests that load() raises an error 
		when parsing a JSON document from a file containing 
		invalid JSON.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0063.
		"""
		raise NotImplementedError

	def test_load_none(self):
		"""
		Description: Tests that load() raises an error 
		when attempting to parse a JSON document from 
		an empty file.

		Input: 

		Output:

		Test Case: Corresponds to test case TEST-0064.
		"""
		raise NotImplementedError

	def test_loads_correct(self):
		"""
		Description: Tests that loads() can correctly 
		parse a JSON document from a string containing 
		valid JSON.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0065.
		"""
		raise NotImplementedError

	def test_loads_invalid(self):
		"""
		Description: Tests that loads() raises an error 
		when attempting to parse a JSON document from a 
		string containing invalid JSON.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0066.
		"""
		raise NotImplementedError

	def test_loads_none(self):
		"""
		Description: Tests that loads() raises an error 
		when attempting to parse a JSON document from an 
		empty string.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0067.
		"""
		raise NotImplementedError
