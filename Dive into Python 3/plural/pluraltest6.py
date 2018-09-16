'''Unit test for plural6.py'''

import plural6
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
            self.assertEqual(plural6.plural(singular), plural)

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
            self.assertEqual(plural6.plural(singular), plural)

    def test_y(self):
        'words ending in Y'
        nouns = {
            'utility': 'utilities',
            'vacancy': 'vacancies',
            'boy': 'boys',
            'day': 'days'
        }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_ouce(self):
        'words ending in OUSE'
        nouns = {
            'mouse': 'mice',
            'louse': 'lice'
        }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_child(self):
        'special case: child'
        nouns = {
            'child': 'children'
        }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_oot(self):
        'special case: foot'
        nouns = {
            'foot': 'feet'
        }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_ooth(self):
        'words ending in OOTH'
        nouns = {
            'booth': 'booths',
            'tooth': 'teeth'
        }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_f_ves(self):
        'words ending in F that become VES'
        nouns = {
            'leaf': 'leaves',
            'loaf': 'loaves'
        }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_sis(self):
        'words ending in SIS'
        nouns = {
            'thesis': 'theses'
        }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_man(self):
        'words ending in MAN'
        nouns = {
            'man': 'men',
            'mailman': 'mailmen',
            'human': 'humans',
            'roman': 'romans'
        }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_ife(self):
        'words ending in IFE'
        nouns = {
            'knife': 'knives',
            'wife': 'wives',
            'lowlife': 'lowlifes'
        }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_eau(self):
        'words ending in EAU'
        nouns = {
            'tableau': 'tableaux'
        }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_elf(self):
        'words ending in ELF'
        nouns = {
            'elf': 'elves',
            'shelf': 'shelves',
            'delf': 'delfs',
            'pelf': 'pelfs'
        }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_same(self):
        'words that are their own plural'
        nouns = {
            'sheep': 'sheep',
            'deer': 'deer',
            'fish': 'fish',
            'moose': 'moose',
            'aircraft': 'aircraft',
            'series': 'series',
            'haiku': 'haiku'
        }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)

    def test_default(self):
        'unexceptional words'
        nouns = {
            'papaya': 'papayas',
            'whip': 'whips',
            'palimpsest': 'palimpsests'
        }
        for singular, plural in nouns.items():
            self.assertEqual(plural6.plural(singular), plural)


if __name__ == '__main__':
    unittest.main()