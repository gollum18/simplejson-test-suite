from unittest import TestCase

import simplejson

class TestInit(TestCase):

	def test_dump_correct(self):
		"""Tests that dump() functions correctly when given a 
		valid Python object and file pointer.
		Corresponds to test case TEST-0056.
		"""
		raise NotImplementedError

	def test_dump_invalid(self):
		"""Testst that dump() raises an error when given an
		invalid Python object.
		Corresponds to test case TEST-0057.
		"""
		raise NotImplementedError

	def test_dump_none(self):
		"""Tests that dump() raises an error when given the None
		type as the file pointer.
		Corresponds to test case TEST-0058.
		"""
		raise NotImplementedError

	def test_dumps_correct(self):
		"""Tests that dumps() returns a properly encoded JSON 
		string given a valid Python object and file pointer.
		Corresponds to test case TEST-0059.
		"""
		raise NotImplementedError

	def test_dumps_invalid(self):
		"""Tests that dumps() raises an error when given an invalid
		invalid Python object.
		Corresponds to test case TEST-0060.
		"""
		raise NotImplementedError

	def test_dumps_none(self):
		"""Tests that dumps() raises an error when given the Python
		None type.
		Corresponds to test case TEST-0061.
		"""
		raise NotImplementedError

	def test_load_correct(self):
		"""Tests that load() can correctly parse a JSON document
		from a file.
		Corresponds to test case TEST-0062.
		"""
		raise NotImplementedError

	def test_load_invalid(self):
		"""Tests that load() raises an error when parsing a JSON
		document from a file containing invalid JSON.
		Corresponds to test case TEST-0063.
		"""
		raise NotImplementedError

	def test_load_none(self):
		"""Tests that load() raises an error when attempting to
		parse a JSON document from an empty file.
		Corresponds to test case TEST-0064.
		"""
		raise NotImplementedError

	def test_loads_correct(self):
		"""Tests that loads() can correctly parse a JSON document
		from a string containing valid JSON.
		Corresponds to test case TEST-0065.
		"""
		raise NotImplementedError

	def test_loads_invalid(self):
		"""Tests that loads() raises an error when attempting to
		parse a JSON document from a string containing invalid
		JSON.
		Corresponds to test case TEST-0066.
		"""
		raise NotImplementedError

	def test_loads_none(self):
		"""Tests that loads() raises an error when attempting to
		parse a JSON document from an empty string.
		Corresponds to test case TEST-0067.
		"""
		raise NotImplementedError
