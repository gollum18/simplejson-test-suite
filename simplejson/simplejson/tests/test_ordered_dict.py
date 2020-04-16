# Name: test_ordered_dict.py
# Since: April 13th, 2020
# Author: Christen Ford
# Purpose: Performs unite testing on the simplejson.ordered_dict
#	module.

from unittest import TestCase

import simplejson.ordered_dict as ordered_dict

class TestOrderedDict(TestCase):
	"""Implements unit tests on the simplejson.ordered_dict
	module. The tests performed by this module make sane
	attempts at being as thorough as possible, but they are
	not exhaustive.
	"""

	def test_create(self):
		"""
		Description: Tests creating an OrderedDict through 
		__init__(). 
		
		Input:

		Output:

		Test Case: Corresponds to test case TEST-0068.
		"""
		raise NotImplementedError

	def test_clear(self):
		"""
		Description: Tests emptying an OrderedDict through 
		clear().

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0069.
		"""
		raise NotImplementedError

	def test_set_item(self):
		"""
		Description: Tests that __setitem() adds a 
		specified key-value pair to an OrderedDict.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0070.
		"""
		raise NotImplementedError

	def test_del_item(self):
		"""
		Description: Tests that __delitem__() deletes 
		a specified key-value pair from an OrderedDict.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0071.
		"""
		raise NotImplementedError

	def test_iter(self):
		"""
		Description: Tests that __iter__() returns a 
		generator fucntion that yields key-value pairs 
		from an OrderedDict in forward order.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0072.
		"""
		raise NotImplementedError

	def test_reversed(self):
		"""
		Description: Tests that __reversed__() returns 
		a generator function that yields key-value pairs 
		from an OrderedDict in reverse order.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0073.
		"""
		raise NotImplementedError

	def test_pop_item_front(self):
		"""Description: Tests that popitem(false) returns 
		the first key-value pair in an OrderedDict.

		Input:
		
		Output:

		Test Case: Corresponds to test case TEST-0074.
		"""
		raise NotImplementedError

	def test_pop_item_rear(self):
		"""Tests that popitem(true) returns the last key-value
		pair in an OrderedDict.
		Corresponds to test case TEST-0075.
		"""
		raise NotImplementedError

	def test_reduce(self):
		"""
		Description: Tests that __reduce__() functions 
		correctly.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0076.
		"""
		raise NotImplementedError

	def test_keys(self):
		"""
		Description: Tests that keys() returns a correct 
		generator function that yields all keys from the 
		OrderedDict.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0077.
		"""
		raise NotImplementedError

	def test_repr(self):
		"""
		Description: Tests that __repr__() returns the 
		correct string representation of an OrderedDict.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0078.
		"""
		raise NotImplementedError

	def test_copy(self):
		"""
		Description: Tests that copy() returns a correct 
		copy of an OrderedDict.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0079.
		"""
		raise NotImplementedError

	def test_fromkeys(self):
		"""
		Description: Tests that fromkeys() returns a 
		correct OrderedDict generated from an iterable of keys.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0080.
		"""
		raise NotImplementedError

	def test_equals_true(self):
		"""
		Description: Tests that __eq__() returns true 
		when two OrderedDicts are equal to each other.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0081.
		"""
		raise NotImplementedError

	def test_equals_false(self):
		"""
		Description: Tests that __eq__() returns false 
		when two OrderedDicts are not equal to each other.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0082.
		"""
		raise NotImplementedError

	def test_not_equals_true(self):
		"""
		Description: Tests that __eq__() returns false 
		when two OrderedDicts are not equal to each other.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0083.
		"""
		raise NotImplementedError

	def test_not_equals_false(self):
		"""
		Description: Tests that __ne__() returns true 
		when two OrderedDicts are not equal to each other.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0084.
		"""
		raise NotImplementedError

	def test_not_equals(self):
		"""
		Description: Tests that __ne__() returns false 
		when two OrderedDicts are equal to each other.

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0085.
		"""
		raise NotImplementedError
