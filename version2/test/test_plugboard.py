import unittest
from version2.plugboard import Plugboard


class TestPlugboard(unittest.TestCase):
    def test_add_connection(self):
        pb = Plugboard({'A':'B'})
        self.assertEqual('A', pb.wiring['B'])
        self.assertEqual('B', pb.wiring['A'])

    def test_remove_connection(self):
        pb = Plugboard({'A':'B'})
        pb.remove_pair('A','B')
        self.assertFalse('A' in pb.wiring)
        self.assertFalse('B' in pb.wiring)

    def test_get_wiring(self):
        pb = Plugboard({'A':'B', 'C':'D'})
        self.assertEqual('A', pb.get_wiring('B'))
        self.assertEqual('D', pb.get_wiring('C'))