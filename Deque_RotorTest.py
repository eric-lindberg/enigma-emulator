import unittest
from Deque_Rotor import Rotors
# Rotors is the Class, Rotor is the deques part of the Class,
# rotor is the instanced (spawned) Object


class TestRotor(unittest.TestCase):
    def initRotorsArray(self):   # "Spawn Rotors Object"
        rotor = Rotors(1, 2, 3)
        return rotor

    def testRotor(self):

        rotor = self.initRotorsArray()  # Rotors(1, 2, 3)

        # Check Rotor controls
        self.assertEqual(rotor.rotor_id, 1)
        self.assertEqual(rotor.ring, 3)
        self.assertEqual(rotor.pos, 2)

        # Test Deque Rotor mechanisms
        self.assertEqual(len(rotor.Rotor), 6)  # Check for 6 Rotors
        for rotor_id in range(0, 5):  # Check all Rotors for 26 characters
            self.assertEqual(len(rotor.Rotor[rotor_id]), 26)

        # Test that every character in the Deque Rotor Object accessed by
        # Deque rotation is the same vs. this known good hardcoded List
        # of all the characters in all the Rotors in order

        chars = [['E','K','M','F','L','G','D','Q','V','Z','N','T','O',
                  'W','Y','H','X','U','S','P','A','I','B','R','C','J'],
                 ['A','J','D','K','S','I','R','U','X','B','L','H','W',
                  'T','M','C','Q','G','Z','N','P','Y','F','V','O','E'],
                 ['B','D','F','H','J','L','C','P','R','T','X','V','Z',
                  'N','Y','E','I','W','G','A','K','M','U','S','Q','O'],
                 ['E','S','O','V','P','Z','J','A','Y','Q','U','I','R',
                  'H','X','L','N','F','T','G','K','D','C','M','W','B'],
                 ['V','Z','B','R','G','I','T','Y','U','P','S','D','N',
                  'H','L','X','A','W','M','J','Q','O','F','E','C','K'],
                 ['Y','R','U','H','Q','S','L','D','P','X','N','G','O',
                  'K','M','I','E','B','F','Z','C','W','V','J','A','T']]
        for rotor_count in range(0, 5):
            for chr_count in range(0, 25):
                self.assertEqual(rotor.Rotor[rotor_count][0],
                                 chars[rotor_count][chr_count])
                print(rotor.Rotor[rotor_count][0], chars[rotor_count][chr_count])
                rotor.Rotor[rotor_count].rotate(-1)

    # TODO:
    # Test forward mapping with position and rings at 0
    # def testForwardMapping(self):
    #     rotors = self.initRotorsArray()
    #     rotors.append(Rotor('RFL','0','0'))  # Test Reflector as well

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