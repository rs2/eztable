import unittest
from zqtable import Table, InvalidIndex


class TestRename(unittest.TestCase):

    def setUp(self):
        self.s = ['pkmn', 'lvl', 'ownr']
        self.t = Table(self.s)

        self.t.extend([
            ('Pikachu', 12, 'ash'),
            ('Squirtle', 18, 'ash'),
            ('Starmie', 4, 'misty'),
        ])

    def test_basic_rename(self):
        t = self.t.rename(
            old_names=self.t.column_names,
            new_names=['Pokemon', 'Level', 'Owner']
        )

        self.assertEquals(
            t._rename_dict,
            {'pkmn': 'Pokemon', 'lvl': 'Level', 'ownr': 'Owner'}

        )

        self.assertEquals(
            t.column_names,
            ['Pokemon', 'Level', 'Owner']
        )

    def test_get_renamed_column(self):
        t = self.t.rename(
            old_names=self.t.column_names,
            new_names=['Pokemon', 'Level', 'Owner']
        )
        p = t._get_column('Pokemon')
        self.assertEquals(
            list(p),
            ['Pikachu', 'Squirtle', 'Starmie']
        )
