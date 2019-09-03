import unittest
from version2.rotor import Rotor, Rotors


class TestRotor(unittest.TestCase):
    @staticmethod
    def createAllRotors():
        rotor_numbers = ['I', 'II', 'III', 'IV', 'V']
        rotors = []
        for number in rotor_numbers:
            rotors.append(Rotors.getRotor(number, 0, 0))

        rotors.append(Rotors.reflector)
        return rotors

    @staticmethod
    def getAlphabet():
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @staticmethod
    def getReverseAlphabet():
        return "ZYXWVUTSRQPONMLKJIHGFEDCBA"

    @staticmethod
    def createDefaultRotor(wiring:str):
        return Rotor(wiring)

    @unittest.skip('Enable to test wiring rules')
    def test_wiring(self):
        alphabet = self.getAlphabet()

        rotors = self.createAllRotors()
        for rotor in rotors:
            self.assertEqual(26, len(rotor.rotor))
            for letter in alphabet:
                self.assertTrue(ord(letter) in rotor.rotor)

    # Make sure each letter maps to its location in the wiring
    @unittest.skip('Enable to test forward mapping logic')
    def test_forward_mapping(self):
        rotor = self.createDefaultRotor(self.getAlphabet())
        alphabet = self.getAlphabet()
        for letter in alphabet:
            coded_val = rotor.forward_encode(letter)
            self.assertEqual(letter, coded_val)

    # Make sure each letter maps to its location rot-N in the wiring,
    # based upon the position value of the rotor
    @unittest.skip('Enable to test forward mapping w. non-0 position')
    def test_advance_forward_mapping(self):
        rotor = self.createDefaultRotor(self.getAlphabet())
        alphabet = self.getAlphabet()
        a_offset = ord('A')
        for pos in range(26):
            rotor.position = pos
            for letter in alphabet:
                coded_val = rotor.forward_encode(letter)
                letter_val = ord(letter)
                letter_offset = ((letter_val - a_offset) + pos) % 26
                self.assertEqual(coded_val, chr(letter_offset + a_offset))

    # With an alphabetically organized array, this is identical to
    # the results of forward-encoding, so test against reverse
    # alphabetical order
    @unittest.skip('Enable to test backward mapping logic')
    def test_backward_mapping(self):
        rotor = self.createDefaultRotor(self.getReverseAlphabet())
        alphabet = self.getAlphabet()
        a_offset = ord('A')
        for letter in alphabet:
            coded_val = rotor.backward_encode(letter)
            letter_offset = ord(letter) - a_offset
            self.assertEqual(coded_val, chr(a_offset + (25-letter_offset)))

    # Now try the same against a position-adjusted mapping
    def test_advance_backward_mapping(self):
        rotor = self.createDefaultRotor(self.getReverseAlphabet())
        alphabet = self.getAlphabet()
        a_offset = ord('A')
        for pos in range(26):
            for letter in alphabet:
                coded_val = rotor.backward_encode(letter)
                letter_offset = ((ord(letter) - a_offset) + pos) % 26
                self.assertEqual(coded_val, chr(a_offset + (25-letter_offset)))

    @unittest.skip('Enable to test forward mapping with ring setting')
    def test_forward_ring(self):
        rotors = self.createAllRotors()
        letters = "KFPCL"
        for rotor in rotors:
            rotor.ring = 1

        for idx in range(5):
            self.assertEqual(rotors[idx].forward_encode('A'), letters[idx])

    @unittest.skip('Enable to test backward mapping with ring setting')
    def test_backward_ring(self):
        rotors = self.createAllRotors()
        letters = "KTNGC"
        for rotor in rotors:
            rotor.ring = 1

        for idx in range(5):
            self.assertEqual(rotors[idx].backward_encode('A'), letters[idx])