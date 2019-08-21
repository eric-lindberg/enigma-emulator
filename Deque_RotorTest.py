import unittest
from Deque_Rotor import Rotors


class TestRotor(unittest.TestCase):
    def initRotorsArray(self):

        rotor = Rotors(1, 2, 3)

        return rotor

    def testRotor(self):

        rotor = Rotors(1, 2, 3)

        self.assertEqual(rotor.rotor_id, 1)
        self.assertEqual(rotor.ring, 3)
        self.assertEqual(rotor.pos, 2)

    #     rotor = Rotor.Rotor
    #     self.assertEqual(rotor(0, 0), 'E')
    #     self.assertEqual(rotor(1, 0), 'A')
    #     self.assertEqual(rotor(2, 0), 'B')
    #     self.assertEqual(rotor(3, 0), 'E')
    #     self.assertEqual(rotor(4, 0), 'V')
    #     self.assertEqual(rotor(5, 0), 'Y')

        # rotors = collections.deque('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        # self.assertEqual(rotors[0], 'E')
        # rotors.rotate(-1)
        # self.assertEqual(rotors[0], 'K')

        # , position = '0', rings = '0'):
        # rotors = []
        # rotors.append(Rotor('I', position, rings))
        # rotors.append(Rotor('II', position, rings))
        # rotors.append(Rotor('III', position, rings))
        # rotors.append(Rotor('IV', position, rings))
        # rotors.append(Rotor('V', position, rings))
        # alphabet = "ABCDEFGHIJKLMNOPQRSTUVWZYX"
        # rotors = self.initRotorsArray()

        # for rotor in rotors:
        #     assert len(rotor.wiring) == 26, \
        #         "Rotor does not have correct wiring"
        #     for letter in alphabet:
        #         assert ord(letter) in rotor.wiring, \
        #             "Letter not wired in rotor"

    # Test forward mapping with position and rings at 0
    # def testForwardMapping(self):
    #     rotors = self.initRotorsArray()
    #     rotors.append(Rotor('RFL', '0', '0'))  # Test Reflector as well
'''
        letters = "EABEVY"

        rotor_idx = 0
        for rotor in rotors:
            assert rotor.forward_encode('A') == letters[rotor_idx], \
                "Failed to encode letter correctly"
            rotor_idx += 1

    # Test forward mapping with position change
    def testForwardAdvance(self):
        rotors = self.initRotorsArray(position = '1')
        letters = "JICRY"

        rotor_idx = 0
        for rotor in rotors:
            assert rotor.forward_encode('A') == letters[rotor_idx], \
                "Failed to advance rotor correctly"
            rotor_idx += 1

    # Test forward mapping with ring setting
    def testForwardRing(self):
        rotors = self.initRotorsArray(rings = '1')
        letters = "KFPCL"
        rotor_idx = 0
        for rotor in rotors:
            assert rotor.forward_encode('A') == letters[rotor_idx], \
                "Failed to apply ring correctly"
            rotor_idx += 1

    # Test backward mapping with position and rings at 0
    def testBackwardMapping(self):
        rotors = self.initRotorsArray()
        letters = "UATHQ"

        rotor_idx = 0
        for rotor in rotors:
            assert rotor.backward_encode('A') == letters[rotor_idx], \
                "Failed to encode letter correctly"
            rotor_idx += 1

    # Test backward mapping with position change
    def testBackwardAdvance(self):
        rotors = self.initRotorsArray(position = '1')
        letters = "VIZYB"

        rotor_idx = 0
        for rotor in rotors:
            assert rotor.backward_encode('A') == letters[rotor_idx], \
                "Failed to advance rotor correctly"
            rotor_idx += 1

    # Test backward mapping with ring setting
    def testBackwardRing(self):
        rotors = self.initRotorsArray(rings = '1')
        letters = "KTNGC"

        rotor_idx = 0
        for rotor in rotors:
            assert rotor.backward_encode('A') == letters[rotor_idx], \
                "Failed to apply ring correctly"
            rotor_idx += 1

'''
if __name__ == '__main__':
    unittest.main()