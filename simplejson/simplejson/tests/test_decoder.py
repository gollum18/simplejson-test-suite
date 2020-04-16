# Name: test_decoder.py
# Since: April 13th, 2020
# Author: Christen Ford
# Purpose: Implementes unit tests for simplejson.decoder.

from unittest import TestCase

import simplejson.decoder as decoder

class TestDecoder(UnitCase):
	"""Implements a set of unit tests for the simplejson.decoder
	module. These test cases make sane attempts at testing each
	class and method found in the decoder module but they
	are not exhaustively extensive.
	"""

	def test_scanstring_correct(self):
		"""
		Description: Tests that the py_scanstring() function 
		is able to parse valid JSON. Assumes optional 
		functional parameters are left at their defaults.

		Input: '{'abc': 0, 'def': 1, 'ghi': 2'}'

		Output: A tuple of the decoded JSON string and 
		the index in the string after the ending quote.

		Test Case: Corresponds to test TEST-0000.
		"""
		raise NotImplementedError

	def test_scanstring_malformed(self):
		"""
		Description: 

		Input: 

		Output:

		Test Case: Corresponds to test TEST-0001.
		"""
		raise NotImplementedError

	def test_scanstring_empty(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test TEST-0002.
		"""
		raise NotImplementedError

	def test_json_object_correct(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test TEST-0003.
		"""
		raise NotImplementedError

	def test_json_object_malformed(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test TEST-0004.
		"""
		raise NotImplementedError

	def test_json_object_empty(self):
		"""

		Corresponds to test TEST-0005.
		"""
		raise NotImplementedError

	def test_json_array_correct(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test TEST-0006.
		"""
		raise NotImplementedError

	def test_json_array_malformed(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test TEST-0007.
		"""
		raise NotImplementedError

	def test_json_array_empty(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test TEST-0008.
		"""
		raise NotImplementedError

	def test_json_decoder_create_utf(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test TEST-0009.
		"""
		raise NotImplementedError

	def test_json_decoder_create_unicode(self):
		"""
		Description:

		Input:

		Output:

		TestCase: Corresponds to test TEST-0010.
		"""
		raise NotImplementedError

	def test_json_decoder_create_invalid(self):
		"""
		Decsription:

		Input:

		Output:

		Test Case: Corresponds to test TEST-0011.
		"""
		raise NotImplementedError

	def test_json_decoder_decode_correct(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test TEST-0012.
		"""
		raise NotImplementedError

	def test_json_decoder_decode_malformed(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test TEST-0013.
		"""
		raise NotImplementedError

	def test_json_decoder_decoder_empty(self):
		"""
		Decsription:

		Input:

		Output:

		Test Case: Corresponds to test TEST-0014.
		"""
		raise NotImplementedError

	def test_raw_decoder_decode_correct(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test TEST-0015.
		"""
		raise NotImplementedError

	def test_raw_decoder_decode_malformed(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test TEST-0016.
		"""
		raise NotImplementedError

	def test_raw_decoder_decoder_empty(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test TEST-0017.
		"""
		raise NotImplementedError
