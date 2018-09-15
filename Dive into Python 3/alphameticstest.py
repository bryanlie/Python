from alphametics import solve
import unittest

class KnownValues(unittest.TestCase):
    def test_out(self):
        '''TO + GO == OUT'''
        self.assertEqual(solve('TO + GO == OUT'), '21 + 81 == 102')

    def test_too(self):
        '''I + DID == TOO'''
        self.assertEqual(solve('I + DID == TOO'), '9 + 191 == 200')

    def test_mom(self):
        '''AS + A == MOM'''
        self.assertEqual(solve('AS + A == MOM'), '92 + 9 == 101')

    def test_best(self):
        '''HES + THE == BEST'''
        self.assertEqual(solve('HES + THE == BEST'), '426 + 842 == 1268')

    def test_late(self):
        '''NO + NO + TOO == LATE'''
        self.assertEqual(solve('NO + NO + TOO == LATE'), '74 + 74 + 944 == 1092')

    def test_onze(self):
        '''UN + UN + NEUF == ONZE'''
        self.assertEqual(solve('UN + UN + NEUF == ONZE'), '81 + 81 + 1987 == 2149')

    def test_deux(self):
        '''UN + DEUX + DEUX + DEUX + DEUX == NEUF'''
        self.assertEqual(solve('UN + DEUX + DEUX + DEUX + DEUX == NEUF'), '25 + 1326 + 1326 + 1326 + 1326 == 5329')

if __name__ == '__main__':
     unittest.main()