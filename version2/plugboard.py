from typing import Dict


class Plugboard():
    def __init__(self, wirings: Dict[str, str]):
        self.wiring = {}
        for key in wirings:
            assert key.upper() not in self.wiring and \
                   wirings[key] not in self.wiring,\
                   "Plugboard may not wire same key twice"
            self.wiring[key.upper()] = wirings[key]
            self.wiring[wirings[key]] = key.upper()

    def get_wiring(self, ch: str) -> str:
        if ch in self.wiring:
            return self.wiring[ch]
        else:
            return ch

    def add_pair(self, ch1: str, ch2: str):
        assert ch1.isalpha() and ch2.isalpha()
        assert ch1 not in self.wiring and ch2 not in self.wiring
        self.wiring[ch1.upper()] = ch2.upper()
        self.wiring[ch2.upper()] = ch1.upper()

    def remove_pair(self, ch1:str , ch2:str):
        assert ch1.isalpha() and ch2.isalpha()
        if ch1.upper() in self.wiring:
            assert self.wiring[ch1.upper()] == ch2.upper()

        self.wiring.pop(ch1.upper(), None)
        self.wiring.pop(ch2.upper(), None)