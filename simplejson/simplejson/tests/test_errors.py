from unittest import TestCase

from simplejson.errors import linecol, errmsg, JSONDecodeError

class TestErrors(TestCase):

	def test_linecol_correct(self):
		"""Test that linecol() returns a correct tuple indicating
		the line and column number an error occurred.
		Corresponds to test case TEST-0049.
		"""
		raise NotImplementedError

	def test_linecol_none(self):
		"""Tests that linecol() raises an error when given the None
		type.
		Corresponds to test case TEST-0050.
		"""
		raise NotImplementedError

	def test_errmsg_correct(self):
		"""Tests that errmsg() returns a formatted error message
		given correct parameters.
		Corresponds to test case TEST-0051.
		"""
		raise NotImplementedError

	def test_errmsg_invalid(self):
		"""Tests that errmsg() raises an error when given an
		invalid starting index.
		Corresponds to test case TEST-0052.
		"""
		raise NotImplementedError

	def test_create(self):
		"""Tests that a JSONDecodeError can be created from 
		correct parameters.
		Corresponds to test case TEST-0053.
		"""
		raise NotImplementedError

	def test_reduce(self):
		"""Tests that __reduce__() of JSONDecodeError works 
		correctly.
		Corresponds to test case TEST-0054.
		"""
		raise NotImplementedError
