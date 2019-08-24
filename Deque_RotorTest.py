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

        self.assertEqual(rotor.rotor_id, 1)
        self.assertEqual(rotor.ring, 3)
        self.assertEqual(rotor.pos, 2)
        self.assertEqual(rotor.Rotor[rotor.rotor_id][rotor.pos], "D")
        rotor.Rotor[rotor.rotor_id].rotate(-1)
        self.assertEqual(rotor.Rotor[rotor.rotor_id][rotor.pos], "K")

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