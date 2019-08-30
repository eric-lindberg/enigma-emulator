import unittest
from version2.rotor import Rotor, Rotors


class TestRotor(unittest.TestCase):
    def setUp(self):
        rotor_numbers = ['I', 'II', 'III', 'IV', 'V']
        self.rotors = []
        for number in rotor_numbers:
            self.rotors.append(Rotors.getRotor(number, 0, 0))

        self.rotors.append(Rotors.reflector)

    def tearDown(self):
        Rotors.reset()

    @unittest.skip('Enable to test wiring rules')
    def test_wiring(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWZYX"

        for rotor in self.rotors:
            self.assertEqual(26, len(rotor.rotor))
            for letter in alphabet:
                self.assertTrue(ord(letter) in rotor.rotor)

    @unittest.skip('Enable to test forward mapping logic')
    def test_forward_mapping(self):
        letters = 'EABEVY'
        for idx in range(6):
            self.assertEqual(self.rotors[idx].forward_encode('A'), letters[idx])

    @unittest.skip('Enable to test backward mapping logic')
    def test_backward_mapping(self):
        letters = "UATHQ"
        for idx in range(5):
            self.assertEqual(self.rotors[idx].backward_encode('A'), letters[idx])

    @unittest.skip('Enable to test forward mapping with advanced rotor')
    def test_forward_advance(self):
        letters = "JICRY"
        for rotor in self.rotors:
            rotor.position = 1

        for idx in range(5):
            self.assertEqual(self.rotors[idx].forward_encode('A'), letters[idx])

    @unittest.skip('Enable to test backward mapping with advanced rotor')
    def test_backward_advance(self):
        letters = "VIZYB"
        for rotor in self.rotors:
            rotor.position = 1

        for idx in range(5):
            self.assertEqual(self.rotors[idx].forward_encode('A'), letters[idx])

    @unittest.skip('Enable to test forward mapping with ring setting')
    def test_forward_ring(self):
        letters = "KFPCL"
        for rotor in self.rotors:
            rotor.ring = 1

        for idx in range(5):
            self.assertEqual(self.rotors[idx].forward_encode('A'), letters[idx])

    @unittest.skip('Enable to test backward mapping with ring setting')
    def test_backward_ring(self):
        letters = "KTNGC"
        for rotor in self.rotors:
            rotor.ring = 1

        for idx in range(5):
            self.assertEqual(self.rotors[idx].backward_encode('A'), letters[idx])