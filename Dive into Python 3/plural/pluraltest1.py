'''Unit test for plural1.py'''

import plural1
import unittest


class KnownValues(unittest.TestCase):
    def test_sxz(self):
        'words ending in S, X, and Z'
        nouns = {
            'bass': 'basses',
            'bus': 'buses',
            'walrus': 'walruses',
            'box': 'boxes',
            'fax': 'faxes',
            'suffix': 'suffixes',
            'mailbox': 'mailboxes',
            'buzz': 'buzzes',
            'waltz': 'waltzes'
        }
        for singular, plural in nouns.items():
            self.assertEqual(plural1.plural(singular), plural)

    def test_h(self):
        'words ending in H'
        nouns = {
            'coach': 'coaches',
            'glitch': 'glitches',
            'rash': 'rashes',
            'watch': 'watches',
            'cheetah': 'cheetahs',
            'cough': 'coughs'
        }
        for singular, plural in nouns.items():
            self.assertEqual(plural1.plural(singular), plural)

    def test_y(self):
        'words ending in Y'
        nouns = {
            'utility': 'utilities',
            'vacancy': 'vacancies',
            'boy': 'boys',
            'day': 'days'
        }
        for singular, plural in nouns.items():
            self.assertEqual(plural1.plural(singular), plural)

    def test_default(self):
        'unexceptional words'
        nouns = {
            'papaya': 'papayas',
            'whip': 'whips',
            'palimpsest': 'palimpsests'
        }
        for singular, plural in nouns.items():
            self.assertEqual(plural1.plural(singular), plural)


if __name__ == '__main__':
    unittest.main()