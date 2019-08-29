from typing import Dict, Any
from collections import deque
from configparser import ConfigParser
import sys

'''
Basic emulator of a "simple" Enigma machine.
This is based extensively on the model and sample C emulator published by
Harald Schmidt of the Miami College of Arts and Sciences
(http://www.cs.miami.edu/home/harald/enigma/index.html)

This code just encodes/decodes the given message. It has been upgraded
to make use of deque components and to emulate four-rotor as well as
three-rotor configurations.
'''


# Implement full Deque_Rotor class here
class Rotor():
    def __init__(self, mapping: str):
        self.rotor = deque(mapping)
        self.position = 0
        self.ring = 0


class Rotors():
    available_rotors = {
        'I': Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ'),
        'II': Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE'),
        'III': Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO'),
        'IV': Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB'),
        'V': Rotor('VZBRGITYUPSDNHLXAWMJQOFECK')
    }

    assigned_rotors = {}

    reflector = Rotor('YRUHQSLDPXNGOKMIEBFZCWVJAT')

    @staticmethod
    def getRotor(rotor_id: str, pos: int, ring: int):
        if rotor_id in Rotors.available_rotors:
            rotor = Rotors.available_rotors[rotor_id]
            Rotors.assigned_rotors[rotor_id] = rotor
            del(Rotors.available_rotors[rotor_id])
        else:
            raise ValueError(f'Rotor ID {rotor_id} does not exist or has been assigned')

        rotor.position = pos
        rotor.ring = ring

        return rotor

class Plugboard():
    def __init__(self, wirings: Dict[str, str]):
        self.wiring = {}
        for key in wirings:
            assert key.upper() not in self.wiring and \
                   wirings[key] not in self.wiring,\
                   "Plugboard may not wire same key twice"
            self.wiring[key.upper()] = wirings[key]
            self.wiring[wirings[key]] = key.upper()


class Enigma():
    def __init__(self, settings: Dict[str, Any]):
        self.rotors = []
        self.add_rotor(settings['rotor1'])
        self.add_rotor(settings['rotor2'])
        self.add_rotor(settings['rotor3'])
        if 'rotor4' in settings:
            self.add_rotor(settings['rotor4'])
        self.reflector = Rotors.reflector
        self.plugboard = Plugboard(settings['plugboard']._sectors)

    def add_rotor(self, rotor_settings: Dict[str, Any]):
        rotor_id = rotor_settings['number']
        position = rotor_settings['position']
        ring = rotor_settings['ring']
        self.rotors.append(Rotors.getRotor(rotor_id=rotor_id,
                                          pos=position,
                                          ring=ring))

    def advance_rotors(self):
        offset = 0
        while True:
            self.rotors[offset].advance()
            if offset + 1 < len(self.rotors) and self.rotors[offset].position == 0:
                offset += 1
            else:
                return

    def encode_char(self, inch: str):
        assert inch.isalpha()

        outch = self.plugboard.get_wiring(inch.upper())
        self.advance_rotors()
        for rotor in self.rotors:
            outch = rotor.forward_encode(outch)
        outch = self.reflector.forward_encode(outch)
        for rotor in reversed(self.rotors):
            outch = rotor.backward_encode(outch)
        outch = self.plugboard.get_wiring(outch)
        assert outch != inch.upper(),"Error - character coded to itself"

        return outch


if __name__ == '__main__':
    c = ConfigParser()
    with open('config.ini', 'r') as f:
        c.read_file(f)
    e = Enigma(c._sections)

    print("Input the message to be encoded")
    print("Only alphabetic values, without spaces "
          "or punctuation, are accepted.\n")
    print("Hit return without typing any message to exit.\n")

    while True:
        inmsg = input("Message --> ")
        msg = ''
        if len(inmsg) == 0:
            sys.exit()

        for c in inmsg:
            if c.isalpha():
                msg += c.upper()

        print(e.encode(msg))
