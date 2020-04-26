# Name: test_encoder.py
# Since: April 13th, 2020
# Author: Christen Ford
# Purpose: Performs unit tests on the simplejson.encoder module.

# NOTES:
"""
    -- Removed test cases 0027 to 0039 as it is impossible to test
    nested functions in Pythons unittest environment. I have merged them
    into test case 0026 as those test cases concern testing nested functions
    of the make_iterencode function.
"""

from decimal import Decimal, getcontext
from unittest import TestCase

import simplejson.encoder as encoder


class TestEncoder(TestCase):
    """Implements unit testing on the simplejson.encoder module.
    The tests implemented by this module make sane attempts at
    being as thorough as possible but they are not exhaustive.
    """

    def test_encode_basestring_correct(self):
        """
        Description: Tests that encode_basestring() can encode
        a Python3 Unicode string,

        Input:
            (str): u“[“abc”, “def”, “ghi”]”

        Output:
            (str): “[“abc”, “def”, “ghi”]”

        Test Case: Corresponds to test case TEST-0018.
        """
        self.assertEqual(
            encoder.encode_basestring(u'["abc", "def", "ghi"]'),
            '"[\\"abc\\", \\"def\\", \\"ghi\\"]"'
        )


    def test_encode_basestring_empty(self):
        """
        Description: Tests that encode_basestring() can encode
        an empty Python3 Unicode string.

        Input:
            (str): u""

        Output:
            (str): ""

        Test Case: Corresponds to test case TEST-0019.
        """
        out = encoder.encode_basestring(u"")
        self.assertEqual(
            out,
            "\"\""
        )


    def test_encode_basestring_str(self):
        """
        Description: Tests that encode_basestring() can encode
        objects using the __str__ magic method.

        Input:
            (Decimal): An instance of the Python Decimal class
            initialized to 1.01.

        Output:
            (str): A string representation of the input object.

        Test Case: Corresponds to test case TEST-0020.
        """
        test_input = Decimal('1.01')
        self.assertEqual(
            encoder.encode_basestring(str(test_input)),
            '"1.01"'
        )


    def test_encode_basestring_ascii_correct(self):
        """
        Description: Tests that py_encode_basestring_ascii() can
        encode a Python3 ASCII string,

        Input:
            (str): “[“abc”, “def”, “ghi”]”

        Output:
            (str): “[“abc”, “def”, “ghi”]”

        Test Case: Corresponds to test case TEST-0021.
        """
        self.assertEqual(
            encoder.encode_basestring_ascii('["abc", "def", "ghi"]'),
            '"[\\"abc\\", \\"def\\", \\"ghi\\"]"'
        )


    def test_encode_basestring_ascii_empty(self):
        """
        Description: Tests that py_encode_basestring_ascii() can
        encode an empty Python3 ASCII string.

        Input:
            (str): ""

        Output:
            (str): ""

        Test Case: Corresponds to test case TEST-0022.
        """
        self.assertEqual(
            encoder.encode_basestring_ascii(""),
            '""'
        )


    def test_encode_basestring_ascii_str(self):
        """
        Description: Tests py_encode_basestring_ascii() can
        encode objects using the __str__ magic method.

        Input:
            (Decimal): An instance of the Python Decimal class initialized
            to 1.01.

        Output:
            (str): A JSON representation of the input object.

        Test Case: Corresponds to test case TEST-0023.
        """
        test_input = Decimal('1.01')
        self.assertEqual(
            encoder.encode_basestring_ascii(str(test_input)),
            '"1.01"'
        )


    def test_encode_basestring_escape_correct(self):
        """
        Description: Tests that py_encode_basestring:replace() can
        properly escape characters in an ASCII string.

        Input:
            (str): “[“\b”, “\f”, “\n”]”

        Output:
            (str): “[“\\b”, “\\f”, “\\n”]”

        Test Case: Corresponds to test case TEST-0024.
        """
        self.assertEqual(
            encoder.py_encode_basestring_ascii(str(["\b", "\f", "\n"])),
            '"[\'\\\\x08\', \'\\\\x0c\', \'\\\\n\']"'
        )


    def test_encode_basestring_escape_mixed(self):
        """
        Description: Tests that py_encode_basestring:escape() fails
        when given strings with mixed encoding.

        Input:
            (str): “[“abc”, U+0065]”

        Output:
            (Error)

        Test Case: Corresponds to test case TEST-0025.
        """
        self.assertRaises(
            BaseException,
            encoder.py_encode_basestring_ascii,
            '["abc", U+00675]'
        )


    def test_make_iterencode(self):
        """
        Description: Tests that the _make_iterencode_() function
        properly configures a generator function to yield JSON
        string tokens  with default values.

        Input: A set of correct parameters where 'markers' is {} while
        the rest of the required parameters are initialized to their
        default values taken from JSONEncoder.

        Output:
            (generator): A generator function that yields JSON string
            tokens.

        Test Case: Corresponds to test case TEST-0026.
        """
        test_input = {
            "nums": [
                0, 1, 2
            ],
            "int": 0,
            "kvs": {
                "abc": 0,
                "def": 1,
                "ghi": 2
            }
        }
        test_output = "{\"nums\": [0, 1, 2], \"int\": 0, \"kvs\": {\"abc\": 0, \"def\": 1, \"ghi\": 2}}"
        encdr = encoder.JSONEncoder()
        self.assertEqual(
            encdr.encode(test_input),
            test_output
        )


    def test_create_json_encoder(self):
        """
        Description: Tests that a JSONEncoder object can be
        created with default options.

        Input: Assume all parameters for the JSONEncoder are
        initialized to their defaults.

        Output:
            (JSONEncoder): A JSONEncoder object initialized to the
            default configuration.

        Test Case: Corresponds to test case TEST-0040.
        """
        encdr = encoder.JSONEncoder()
        self.assertIsInstance(encdr, encoder.JSONEncoder)


    def test_json_encoder_encode_correct(self):
        """
        Description: Tests that JSONEncoder : encode() returns a
        string containing encoded JSON from a Python object.

        Input:
            (Object): A Python object.

        Output:
            (str): An encoded JSON string corresponding to the input object.

        Test Case: Corresponds to test case TEST-0041.
        """
        test_input = {
            "abc":0,
            "def":1,
            "ghi":2
        }
        test_output = [
            '{',
            '"abc"',
            ': ',
            '0',
            ', ',
            '"def"',
            ': ',
            '1',
            ', ',
            '"ghi"',
            ': ',
            '2',
            '}'
        ]
        encdr = encoder.JSONEncoder()
        gen = encdr.iterencode(test_input)
        for token in test_output:
            self.assertEqual(next(gen), token)


    def test_json_encoder_encode_none(self):
        """
        Description: Tests that JSONEncoder : encode() returns the
        JSON ‘null’ type.

        Input:
            (None): The Python None type.

        Output:
            (str): 'null'.

        Test Case: Corresponds to test case TEST-0042.
        """
        test_input = None
        encdr = encoder.JSONEncoder()
        self.assertEqual(encdr.encode(test_input), "null")


    def test_json_encoder_iterencode_correct(self):
        """
        Description: Tests that JSONEncoder : iterencode() yields
        encoded JSON chunks from a Python object.

        Input:
            (Object): A Python object.

        Output:
            (generator): A Python generator that yields chunks of
            the encoded Python object.

        Test Case: Corresponds to test case TEST-0043.
        """
        test_input = {
            "abc":0,
            "def":1,
            "ghi":2
        }
        test_output = [
            '{',
            '"abc"',
            ': ',
            '0',
            ', ',
            '"def"',
            ': ',
            '1',
            ', ',
            '"ghi"',
            ': ',
            '2',
            '}'
        ]
        encdr = encoder.JSONEncoder()
        gen = encdr.iterencode(test_input)
        for token in test_output:
            self.assertEqual(token, next(gen))


    def test_json_encoder_iterencode_none(self):
        """
        Description: Tests that JSONEncoder : iterencode() yields
        ‘null’.

        Input:
            (None)

        Output:
            (generator): A generator function that yields the encoded
            version of the Python None type.

        Test Case: Corresponds to test case TEST-0044.
        """
        encdr = encoder.JSONEncoder()
        self.assertEqual(next(encdr.iterencode(None)), "null")


    def test_json_encoder_html_encode_correct(self):
        """
        Description: Tests that JSONEncoderForHTML : encode()
        can properly encode a Python object

        Input:
            (Object): A Python object.

        Output:
            (str): The encoded Python object.

        Test Case: Corresponds to test case TEST-0045.
        """
        test_input = {
            "id": "0x0012",
            "name": "TEST-0045",
            "items": ["a", "b", "c"]
        }
        encdr = encoder.JSONEncoderForHTML()
        self.assertEqual(
            encdr.encode(test_input),
            '{"id": "0x0012", "name": "TEST-0045", "items": ["a", "b", "c"]}'
        )


    def test_json_encoder_html_encode_none(self):
        """
        Description: Tests that JSONEncoderForHTML : encode() can
        properly encode Pythons None type

        Input:
            (None)

        Output:
            (str): 'null'

        Test Case: Corresponds to test case TEST-0046.
        """
        encdr = encoder.JSONEncoderForHTML()
        self.assertEqual('null', encdr.encode(None))


    def test_json_encoder_html_iterencode_correct(self):
        """
        Description: Tests that the iterencode() method of the
        JSONEncoderForHTML can properly parse a Python object for
        HTML context.

        Input:
            (Object): A Python object.

        Output:
            (generator): A generator that yields chunks of the input
            object.

        Test Case: Corresponds to test case TEST-0047.
        """
        test_input = dict()
        test_input['name'] = 'test-0047'
        test_input['items'] = ['a', 'b', 'c']
        test_input['value'] = 10.0
        test_output = [
            "{",
            '"name"',
            ": ",
            '"test-0047"',
            ", ",
            '"items"',
            ": ",
            '["a"',
            ', "b"',
            ', "c"',
            "]",
            ", ",
            '"value"',
            ": ",
            "10.0",
            "}"
        ]
        encdr = encoder.JSONEncoderForHTML()
        for o, p in zip(test_output, list(encdr.iterencode(test_input))):
            self.assertEqual(o, p)


    def test_json_encoder_html_iterencode_none(self):
        """
        Description: Tests that the iterencode() method of
        the JSONEncoderDorHTML class can properly parse the
        Python None type.

        Input:
            (None)

        Output:
            (generator): A generator function that yields an HTML
            safe version of None, 'null'.

        Test Case: Corresponds to test case TEST-0048.
        """
        encdr = encoder.JSONEncoderForHTML()
        self.assertEqual(next(encdr.iterencode(None)), "null")
