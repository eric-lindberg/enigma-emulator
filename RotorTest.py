import unittest
from Rotor import Rotor

class TestRotor(unittest.TestCase):
    def initRotorsArray(self, position = '0', rings = '0'):
        rotors = []
        rotors.append(Rotor('I',position,rings))
        rotors.append(Rotor('II',position,rings))
        rotors.append(Rotor('III',position,rings))
        rotors.append(Rotor('IV',position,rings))
        rotors.append(Rotor('V',position,rings))

        return rotors

    def testWirings(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWZYX"
        rotors = self.initRotorsArray()

        for rotor in rotors:
            assert len(rotor.wiring) == 26, "Rotor does not have correct wiring"
            for letter in alphabet:
                assert letter in rotor.wiring, "Letter not wired in rotor"

    # Test forward mapping with position and rings at 0
    def testForwardMapping(self):
        rotors = self.initRotorsArray()
        rotors.append(Rotor('RFL','0','0')) # Test Reflector as well

        letters = "EABEVY"

        rotorIdx = 0
        for rotor in rotors:
            assert rotor.forwardEncode('A') == letters[rotorIdx], "Failed to encode letter correctly"
            rotorIdx += 1

    # Test forward mapping with position change
    def testForwardAdvance(self):
        rotors = self.initRotorsArray(position = '1')
        letters = "JICRY"

        rotorIdx = 0
        for rotor in rotors:
            assert rotor.forwardEncode('A') == letters[rotorIdx], "Failed to advance rotor correctly"
            rotorIdx += 1

    # Test forward mapping with ring setting
    def testForwardRing(self):
        rotors = self.initRotorsArray(rings = '1')
        letters = "KFPCL"
        rotorIdx = 0
        for rotor in rotors:
            assert rotor.forwardEncode('A') == letters[rotorIdx], "Failed to apply ring correctly"
            rotorIdx += 1

    # Test backward mapping with position and rings at 0
    def testBackwardMapping(self):
        rotors = self.initRotorsArray()
        letters = "UATHQ"

        rotorIdx = 0
        for rotor in rotors:
            assert rotor.backwardEncode('A') == letters[rotorIdx], "Failed to encode letter correctly"
            rotorIdx += 1

    # Test backward mapping with position change
    def testBackwardAdvance(self):
        rotors = self.initRotorsArray(position = '1')
        letters = "VIZYB"

        rotorIdx = 0
        for rotor in rotors:
            assert rotor.backwardEncode('A') == letters[rotorIdx], "Failed to advance rotor correctly"
            rotorIdx += 1

    # Test backward mapping with ring setting
    def testBackwardRing(self):
        rotors = self.initRotorsArray(rings = '1')
        letters = "KTNGC"

        rotorIdx = 0
        for rotor in rotors:
            assert rotor.backwardEncode('A') == letters[rotorIdx], "Failed to apply ring correctly"
            rotorIdx += 1

if __name__ == '__main__':
    unittest.main()