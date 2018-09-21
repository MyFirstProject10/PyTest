import unittest
import firstlib

class TestFirstLib(unittest.TestCase):
    def testFunction(self):
        self.assertEqual(3, 3, "3 and 3 are indeed equal... aren't they?")
        # assertTrue()
        # assertRaises()
        self.assertEqual(firstlib.analysis.test(), 1, "test not working...")

    # aslo available: @unittest.skip(reason) and @unittest.skipIf(condition, reason)
    @unittest.expectedFailure
    def testError(self):
        self.assertTrue(0/0, "I can divide 0 times 0!!")

if __name__ == "__main__":
    unittest.main()
