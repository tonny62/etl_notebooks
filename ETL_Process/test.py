import unittest
import pickle
import src.dataTransformer as dt

class TestCleaning(unittest.TestCase):
    def getData(self):
        import pickle
        with open("testdata/jobsdata.pickle", 'rb') as fin:
            data = pickle.load(fin)
        return data

    def test_get_jobtitle(self):
        testdata = self.getData()[0]
        result = 'งานขาย งานบริการลูกค้า งานพัฒนาธุรกิจ > งานพัฒนาธุรกิจ\nงานบริหาร > งานบริหารทั่วไป\nงานบริหาร > งานผู้บริหารระดับสูง VP. Business Development (Energy)'
        self.assertEqual(result, dt.get_jobtitle(testdata))

    def test_get_jobtitle_isstring(self):
        testdata = self.getData()[0]
        result = dt.get_jobtitle(testdata)
        self.assertIsInstance(result, str)

    def test_get_ostarnetid_isint(self):
        result = dt.get_ostarnetid(testdata)
        self.assertIsInstance(result, int)


if(__name__ == '__main__'):
    unittest.main()
