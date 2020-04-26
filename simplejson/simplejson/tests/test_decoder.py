# Name: test_decoder.py
# Since: April 13th, 2020
# Author: Christen Ford
# Purpose: Implementes unit tests for simplejson.decoder.

from unittest import TestCase

import simplejson.decoder as decoder
import simplejson.errors as errors


class TestDecoder(TestCase):
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
        test_input = '"{"abc": 0, "def": 1, "ghi": 2}"'
        decoded_str, last_char_index = decoder.py_scanstring(
            s=test_input,
            end=1
        )
        self.assertEqual(decoded_str, "{")
        self.assertEqual(last_char_index, 3)


    def test_scanstring_malformed(self):
        """
        Description: Tests that the py_scanstring() function is
        able to properly detect malformed JSON. This test case
        may include multiple different strings to ensure
        well-rounded error detection.

        Input:
            (tuple): ("{]", "[}")

        Output:
            (JSONDecodeError)

        Test Case: Corresponds to test TEST-0001.
        """
        test_inputs = ('"{]"', '"[}"')
        for test_input in test_inputs:
            self.assertRaises(
                decoder.JSONDecodeError,
                decoder.py_scanstring,
                s=test_input,
                end=1
            )


    def test_scanstring_empty(self):
        """
        Description: Tests that the py_scanstring() function is
        able to properly detect empty strings.

        Input:
            (str): ""

        Output:
            (JSONDecodeError)

        Test Case: Corresponds to test TEST-0002.
        """
        test_input = '""'
        self.assertRaises(
            errors.JSONDecodeError,
            decoder.py_scanstring,
            s=test_input,
            end=1
        )


    def test_json_object_correct(self):
        """
        Description: Test that the JSONObject() method can properly
        decode JSON objects to Python dictionaries.

        Input:
            (tuple): ("{"abc": 0, "def": 1, "ghi": 2}", 0)

        Output:
            (dict): ({"abc": 0, "def": 1, "ghi": 2}, 30)

        Test Case: Corresponds to test TEST-0003.
        """
        test_input = ('{"abc": 0, "def": 1, "ghi": 2}', 1)
        out_dict = dict()
        out_dict["abc"] = 0
        out_dict["def"] = 1
        out_dict["ghi"] = 2
        test_output = (out_dict, 30)
        dcdr = decoder.JSONDecoder()
        self.assertEqual(
            decoder.JSONObject(
                state=test_input,
                encoding=dcdr.encoding,
                strict=dcdr.strict,
                scan_once=dcdr.scan_once,
                object_hook=dcdr.object_hook,
                object_pairs_hook=dcdr.object_pairs_hook
            ),
            test_output
        )


    def test_json_object_malformed(self):
        """
        Description: Tests that the JSONObject() method can detect
        improperly formed JSON object.

        Input:
            (tuple): ("{"abc": 0, "def": 1, "ghi" :2]", 1)

        Output:
            (JSONDecodeError)

        Test Case: Corresponds to test TEST-0004.
        """
        test_input = ('\"{"abc": 0, "def": 1, "ghi": 2]\"', 1)
        dcdr = decoder.JSONDecoder()
        self.assertRaises(
            errors.JSONDecodeError,
            decoder.JSONObject,
            state=test_input,
            encoding=dcdr.encoding,
            strict = dcdr.strict,
            scan_once = dcdr.scan_once,
            object_hook = dcdr.object_hook,
            object_pairs_hook = dcdr.object_pairs_hook
    )


    def test_json_object_empty(self):
        """
        Description: Tests that the JSONObject() method can detect
        empty strings.

        Input:
            (tuple): ('', 0)

        Output:
            (JSONDecodeError)

        Test Case: Corresponds to test TEST-0005.
        """
        test_input = ("", 0)
        dcdr = decoder.JSONDecoder()
        self.assertRaises(
            errors.JSONDecodeError,
            decoder.JSONObject,
            state=test_input,
            encoding=dcdr.encoding,
            strict = dcdr.strict,
            scan_once = dcdr.scan_once,
            object_hook = dcdr.object_hook,
            object_pairs_hook = dcdr.object_pairs_hook
        )


    def test_json_array_correct(self):
        """
        Description: Tests that the JSONArray method can decode
        a properly formed JSONArray.

        Input:
            (tuple): ("["abc", "def", "ghi"]", 1)

        Output:

        Test Case: Corresponds to test TEST-0006.
        """
        test_input = ('["abc", "def", "ghi"]', 1)
        test_output = (['abc', 'def', 'ghi'], 21)
        dcdr = decoder.JSONDecoder()
        self.assertEqual(
            decoder.JSONArray(
                test_input,
                dcdr.scan_once
            ),
            test_output
        )


    def test_json_array_malformed(self):
        """
        Description: Tests that the JSONArray method can properly
        detect a malformed JSON array.

        Input:
            (str): ("["abc", "def", "ghi"}", 1)

        Output:
            (JSONDecodeError)

        Test Case: Corresponds to test TEST-0007.
        """
        test_input = ('["abc", "def", "ghi"}', 1)
        dcdr = decoder.JSONDecoder()
        self.assertRaises(
            errors.JSONDecodeError,
            decoder.JSONArray,
            test_input,
            dcdr.scan_once
        )


    def test_json_array_empty(self):
        """
        Description: Tests that the JSONArray() method can
        properly detect an empty string.

        Input:
            (tuple): ("", 0)

        Output:
            (JSONDecodeError)

        Test Case: Corresponds to test TEST-0008.
        """
        test_input = ('', 0)
        dcdr = decoder.JSONDecoder()
        self.assertRaises(
            errors.JSONDecodeError,
            decoder.JSONArray,
            test_input,
            dcdr.scan_once
        )


    def test_json_decoder_create_utf(self):
        """
        Description: Tests that a JSONDecoder object can be created
        to decode JSON strings with the 'utf-8' character encoding.

        Input:
            (str): "utf-8"

        Output:
            (JSONDecoder)

        Test Case: Corresponds to test TEST-0009.
        """
        dcdr = decoder.JSONDecoder(encoding="utf-8")
        self.assertEqual(dcdr.encoding, "utf-8")


    def test_json_decoder_create_unicode(self):
        """
        Description: Tests that a JSONDecoder object can be created
        with the unicode character encoding.

        Input:
            (str): "unicode"

        Output:
            (JSONDecoder)

        TestCase: Corresponds to test TEST-0010.
        """
        dcdr = decoder.JSONDecoder(encoding="unicode")
        self.assertEqual(dcdr.encoding, "unicode")


    def test_json_decoder_create_invalid(self):
        """
        Description: Tests that a JSONDecoder object cannot be
        created when given an invalid encoding.

        Input:
            (str): "ISO-8859-1"

        Output:
            (JSONDecodeError)

        Test Case: Corresponds to test TEST-0011.
        """
        self.assertRaises(
            errors.JSONDecodeError,
            decoder.JSONDecoder,
            encoding="ISO-8859-1"
        )


    def test_json_decoder_decode_correct(self):
        """
        Description: Tests that the decode() method of the
        JSONDecoder class can decode a properly formed JSON
        document.

        Input:
            (str): {"id": "001", "name": "test-012", "items": ["a", "b", "c"]}

        Output:

        Test Case: Corresponds to test TEST-0012.
        """
        test_input = '{"id": "001", "name": "test-012", "items": ["a", "b", "c"]}'
        test_output = dict()
        test_output["id"] = "001"
        test_output["name"] = "test-012"
        test_output["items"] = ["a", "b", "c"]
        dcdr = decoder.JSONDecoder()
        self.assertEqual(dcdr.decode(test_input), test_output)


    def test_json_decoder_decode_malformed(self):
        """
        Description: Tests that the decode() method of the
        JSONDecoder class can properly recognize a malformed JSON
        document.

        Input:
            (str): {"id": "001", "name": "test-012", "items": ["a", "b", "c"]]

        Output:
            (JSONDecodeError)

        Test Case: Corresponds to test TEST-0013.
        """
        test_input = '{"id": "001", "name": "test-012", "items": ["a", "b", "c"]]]'
        dcdr = decoder.JSONDecoder()
        self.assertRaises(
            errors.JSONDecodeError,
            dcdr.decode,
            test_input
        )


    def test_json_decoder_decoder_empty(self):
        """
        Decsription: Tests that the decode() method of the
        JSONDecode class can recognize an empty string.

        Input:
            (str): ""

        Output:
            (JSONDecodeError)

        Test Case: Corresponds to test TEST-0014.
        """
        test_input = ''
        dcdr = decoder.JSONDecoder()
        self.assertRaises(
            errors.JSONDecodeError,
            dcdr.decode,
            test_input
        )


    def test_raw_decoder_decode_correct(self):
        """
        Description: Tests that the raw_decode() method of the
        JSONDecoder class can properly decode an embedded JSON
        document.

        Input:
            (str): "["abc", "def", "ghi"] This is a test!"

        Output:

        Test Case: Corresponds to test TEST-0015.
        """
        dcdr = decoder.JSONDecoder()
        test_input = '["abc", "def", "ghi"] This is a test!'
        test_output = (['abc', 'def', 'ghi'], 21)
        self.assertEqual(dcdr.raw_decode(test_input), test_output)


    def test_raw_decoder_decode_malformed(self):
        """
        Description: Tests that the raw_decode() method of the
        JSONDecoder class can recognize a malformed JSON document.

        Input:
            (str): "["abc", "def", "ghi"} This is a test!"

        Output:
            (JSONDecodeError)

        Test Case: Corresponds to test TEST-0016.
        """
        dcdr = decoder.JSONDecoder()
        test_input = '["abc", "def", "ghi"} This is a test!'
        self.assertRaises(
            errors.JSONDecodeError,
            dcdr.raw_decode,
            test_input
        )


    def test_raw_decoder_decoder_empty(self):
        """
        Description: Tests that the raw_decode() method of the
        JSONDecoder class can recognize an empty string.

        Input:
            (str): ""

        Output:
            (JSONDecodeError)

        Test Case: Corresponds to test TEST-0017.
        """
        test_input = ''
        dcdr = decoder.JSONDecoder()
        self.assertRaises(
            errors.JSONDecodeError,
            dcdr.raw_decode,
            test_input
        )
