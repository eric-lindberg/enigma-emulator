import unittest
from typing import Dict, Any
from version2.enigma import Enigma
from version2.rotor import Rotors


class TestEnigma(unittest.TestCase):
    @staticmethod
    def create_config() -> Dict[str, Any]:
        config = {}
        config['rotor1'] = {}
        config['rotor2'] = {}
        config['rotor3'] = {}
        config['plugboard'] = {}

        return config

    @staticmethod
    def create_rotor_config(rotor: str,
                            config: Dict[str, Any],
                            number: str = 'I',
                            position: str = '0',
                            ring: str = '0'):
        config[rotor]['number'] = number
        config[rotor]['position'] = position
        config[rotor]['ring'] = ring

    def setUp(self):
        config = self.create_config()
        self.create_rotor_config(rotor='rotor1', config=config, number='I', position='0')
        self.create_rotor_config(rotor='rotor2', config=config, number='II', position='1')
        self.create_rotor_config(rotor='rotor3', config=config, number='III', position='2')

        config['plugboard'] = {'A': 'M', 'E': 'T'}
        self.enigma = Enigma(config)

    def tearDown(self):
        Rotors.reset()

    def test_rotors_assigned_in_order(self):
        self.assertEqual('I', Rotors.getAssignedRotorNumber(self.enigma.rotors[0]))
        self.assertEqual('II', Rotors.getAssignedRotorNumber(self.enigma.rotors[1]))
        self.assertEqual('III', Rotors.getAssignedRotorNumber(self.enigma.rotors[2]))

    def test_positions_assigned(self):
        self.assertEqual(0, self.enigma.rotors[0].position)
        self.assertEqual(1, self.enigma.rotors[1].position)
        self.assertEqual(2, self.enigma.rotors[2].position)