import hashlib
import unittest

from utilset import email


class TestEmail(unittest.TestCase):

    def test_is_valid(self):
        self.assertTrue(email.is_valid("user@puresai.com"))
        self.assertFalse(email.is_valid("user@puresai."))
        self.assertFalse(email.is_valid("user@puresai.com."))
        self.assertFalse(email.is_valid("puresai.com"))
        self.assertTrue(email.is_valid("user@13sai.com"))

    def test_md5_email(self):
        self.assertEqual(
            email.md5_email("User@Gmail.com"),
            email.md5_email(" user@gmail.com "))
        self.assertEqual(
            email.md5_email("u.s.e.r+tag@gmail.com"),
            email.md5_email("usertag@gmail.com"))
        self.assertEqual(
            email.md5_email("user@puresai.com"),
            hashlib.md5(b"user@puresai.com").hexdigest())


if __name__ == '__main__':
    unittest.main()