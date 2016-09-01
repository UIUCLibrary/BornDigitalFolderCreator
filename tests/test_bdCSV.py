import os
from unittest import TestCase, mock
from BDCreateFolders import csv_parser

class TestBdCSV(TestCase):
    def setUp(self):
        testfile = os.path.join(os.path.split(__file__)[0], "items.csv")
        self.testcase = csv_parser.bdCSV(testfile)

    def test_filename(self):

        self.assertEqual(os.path.basename(self.testcase.filename), "items.csv")

    def test_len(self):
        self.assertEqual(len(self.testcase), 5)

    def test_is_iteriable(self):
        for x in self.testcase:
            self.assertTrue(isinstance(x, csv_parser.bdItem), msg="returned item is not a csv_parser.bdItem object")