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

        for test in 'EKMFLGDQVZNTOWYHXUSPAIBRCJ':
            self.assertEqual(rotor.Rotor[0][0], test)
            print(rotor.Rotor[0][0], end=" ")
            rotor.Rotor[0].rotate(-1)
        print()

        for test in 'AJDKSIRUXBLHWTMCQGZNPYFVOE':
            self.assertEqual(rotor.Rotor[1][0], test)
            print(rotor.Rotor[1][0], end=" ")
            rotor.Rotor[1].rotate(-1)
        print()

        for test in 'BDFHJLCPRTXVZNYEIWGAKMUSQO':
            self.assertEqual(rotor.Rotor[2][0], test)
            print(rotor.Rotor[2][0], end=" ")
            rotor.Rotor[2].rotate(-1)
        print()

        for test in 'ESOVPZJAYQUIRHXLNFTGKDCMWB':
            self.assertEqual(rotor.Rotor[3][0], test)
            print(rotor.Rotor[3][0], end=" ")
            rotor.Rotor[3].rotate(-1)
        print()

        for test in 'VZBRGITYUPSDNHLXAWMJQOFECK':
            self.assertEqual(rotor.Rotor[4][0], test)
            print(rotor.Rotor[4][0], end=" ")
            rotor.Rotor[4].rotate(-1)
        print()

        for test in 'YRUHQSLDPXNGOKMIEBFZCWVJAT':
            self.assertEqual(rotor.Rotor[5][0], test)
            print(rotor.Rotor[5][0], end=" ")
            rotor.Rotor[5].rotate(-1)
'''

    # alphabet = "ABCDEFGHIJKLMNOPQRSTUVWZYX"
    # rotors = self.initRotorsArray()

    # Test forward mapping with position and rings at 0
    # def testForwardMapping(self):
    #     rotors = self.initRotorsArray()
    #     rotors.append(Rotor('RFL', '0', '0'))  # Test Reflector as well


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