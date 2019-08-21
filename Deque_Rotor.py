import collections


class Rotors:

    rotor_ids = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'RFL'}
    Rotor = [collections.deque('EKMFLGDQVZNTOWYHXUSPAIBRCJ'),
             collections.deque('AJDKSIRUXBLHWTMCQGZNPYFVOE'),
             collections.deque('BDFHJLCPRTXVZNYEIWGAKMUSQO'),
             collections.deque('ESOVPZJAYQUIRHXLNFTGKDCMWB'),
             collections.deque('VZBRGITYUPSDNHLXAWMJQOFECK'),
             collections.deque('YRUHQSLDPXNGOKMIEBFZCWVJAT')]

    def __init__(self, rotor_id, pos='0', ring='0'):

        self.rotor_id = rotor_id
        self.pos = pos
        self.ring = ring




    #   "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #
    # def select_rotor(self, rotor_num):
    #     encoding = [ord(ch) for ch in self.wirings[rotor_num]]
    #     return np.array(encoding)

    # def __init__(self, rotor_id, pos = '0', ring = '0'):
    #     self.id = rotor_id.upper()
    #     assert self.id in self.rotor_ids, "unrecognized Rotor ID " + self.id
    #     rotor_num = self.rotor_ids.index(self.id)

        # self.wiring = self.select_rotor(rotor_num)

    # self.position = int(pos)
    # assert self.position >= 0 and self.position < 26, \
    #     "Initial position must be between 0 and 25"
    #
    # self.ring = int(ring)
    # assert self.ring >= 0 and self.ring < 26, \
    #     "Ring setting must be between 0 and 25"
'''
    def advance(self):
        self.position += 1
        if self.position == 26:
            self.position = 0

    def forward_encode(self, ch):
        assert ch.isalpha()
        ch = ch.upper()
        chidx = ord(ch) - ord('A')
        idx = (chidx + self.position) % 26
        idx = (idx - self.ring) % 26
        # Adjust idx for rings (need to review ring model)
        chidx = self.wiring[idx] - ord('A')
        chidx = (chidx + self.ring) % 26
        return chr(((chidx - self.position) % 26) + ord('A'))

    def backward_encode(self, ch):
        assert ch.isalpha()
        ch = ch.upper()
        chidx = ord(ch) - ord('A')
        idx = (chidx + self.position) % 26
        idx = (idx - self.ring) % 26
        # Adjust idx for rings (need to review ring model)
        chidx = np.where(self.wiring == idx + ord('A'))[0]
        chidx = (chidx + self.ring) % 26
        return chr(((chidx - self.position) % 26) + ord('A'))
'''