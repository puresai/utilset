import hashlib
import unittest

from utilset import phone


class TestPhone(unittest.TestCase):

    def test_md5_phone(self):
        self.assertEqual(
            phone.md5_phone("(123) 456-7890"),
            phone.md5_phone("123-456-7890"))
        self.assertEqual(
            phone.md5_phone("1234567890"),
            hashlib.md5(b"1234567890").hexdigest())


if __name__ == '__main__':
    unittest.main()
