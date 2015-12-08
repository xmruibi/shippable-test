import unittest

class BasicTestCase(unittest.TestCase):

    def test_true(self):
        self.assertFalse(not True)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(BasicTestCase())
    return suite

def main():
    unittest.main()

if __name__ == "__main__":
    main()