# Name: test_encoder.py
# Since: April 13th, 2020
# Author: Christen Ford
# Purpose: Performs unit tests on the simplejson.encoder module.


from unittest import TestCase

import simplejson.encoder as encoder

class TestEncoder(TestCase):
	"""Implements unit testing on the simplejson.encoder module.
	The tests implemented by this module make sane attempts at
	being as thorough as possible but they are not exhaustive.
	"""

	def test_encode_basestring_correct(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0018.
		"""
		raise NotImplementedError

	def test_encode_basestring_empty(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0019.
		"""
		raise NotImplementedError

	def test_encode_basestring_str(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0020.
		"""
		raise NotImplementedError

	def test_encode_basestring_ascii_correct(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0021.
		"""
		raise NotImplementedError

	def test_encode_basestring_ascii_empty(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0022.
		"""
		raise NotImplementedError

	def test_encode_basestring_ascii_str(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0023.
		"""
		raise NotImplementedError

	def test_encode_basestring_escape_correct(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0024.
		"""
		raise NotImplementedError

	def test_encode_basestring_escape_mixed(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0025.
		"""
		raise NotImplementedError

	def test_make_iterencode(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0026.
		"""
		raise NotImplementedError

	def test_encode_int_correct(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0027.
		"""
		raise NotImplementedError

	def test_encode_int_nonint(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0028.
		"""
		raise NotImplementedError

	def test_encode_int_none(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0029.
		"""
		raise NotImplementedError

	def test_iterencode_list_correct(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0030.
		"""
		raise NotImplementedError

	def test_iterencode_list_empty(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0031.
		"""
		raise NotImplementedError

	def test_iterencode_list_none(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0032.
		"""
		raise NotImplementedError

	def test_make_iterencode_skey_correct(self):
		"""
		Desciption:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0033.
		"""
		raise NotImplementedError

	def test_make_iterencode_skey_none(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0034.
		"""
		raise NotImplementedError

	def test_iterencode_dict_correct(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0035.
		"""
		raise NotImplementedError

	def test_iterencode_dict_empty(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0036.
		"""
		raise NotImplementedError

	def test_iterencode_dict_none(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0037.
		"""
		raise NotImplementedError

	def test_make_iterencode_iterencode_correct(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0038.
		"""
		raise NotImplementedError

	def test_make_iterencode_iterencode_empty(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0039.
		"""
		raise NotImplementedError


	def test_create_json_encoder(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0040.
		"""
		raise NotImplementedError

	def test_json_encoder_encode_correct(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0041.
		"""
		raise NotImplementedError

	def test_json_encoder_encode_none(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0042.
		"""
		raise NotImplementedError

	def test_json_encoder_iterencode_correct(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0043.
		"""
		raise NotImplementedError

	def test_json_encoder_iterencode_none(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0044.
		"""
		raise NotImplementedError

	def test_json_encoder_html_encode_correct(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0045.
		"""
		raise NotImplementedError

	def test_json_encoder_html_encode_none():
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0046.
		"""

	def test_json_encoder_html_iterencode_correct(self):
		"""
		Description:

		Input:

		Output:

		Test Case: Corresponds to test case TEST-0047.
		"""
		raise NotImplementedError

	def test_json_encoder_html_iterencode_none(self):
		"""
		Description: Tests that the iterencode() method of 
		the JSONEncoderDorHTML class can properly parse the 
		Python None type.

		Input:
			(None)

		Output:
			

		Test Case: Corresponds to test case TEST-0048.
		"""
		raise NotImplementedError
