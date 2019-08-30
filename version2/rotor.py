from collections import deque


# Implement full Deque_Rotor class here
class Rotor():
    def __init__(self, mapping: str):
        assert len(mapping) == 26, 'Must map all characters of alphabet'
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
    def getRotor(rotor_id: str, pos: int, ring: int) -> Rotor:
        if rotor_id in Rotors.available_rotors:
            rotor = Rotors.available_rotors[rotor_id]
            Rotors.assigned_rotors[rotor_id] = rotor
            del(Rotors.available_rotors[rotor_id])
        else:
            raise ValueError(f'Rotor ID {rotor_id} does not exist or has been assigned')

        rotor.position = pos
        rotor.ring = ring

        return rotor

    @staticmethod
    def getAssignedRotorNumber(rotor: Rotor) -> str:
        if rotor in Rotors.assigned_rotors.values():
            for key in Rotors.assigned_rotors:
                if Rotors.assigned_rotors[key] == rotor:
                    return key

        return ''

    @staticmethod
    def reset():
        for key in Rotors.assigned_rotors:
            Rotors.available_rotors[key] = Rotors.assigned_rotors[key]

        Rotors.assigned_rotors = {}