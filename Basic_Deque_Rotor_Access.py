from Deque_Rotor import Rotors

rotor = Rotors(1,2,3)

print(rotor.ring)
print(rotor.pos)

print(Rotors.Rotor[1][2])

for rotor_id in range(0, 5):
    for char_idx in range (0, 26):
        print(rotor_id, char_idx)
        print(Rotors.Rotor[rotor_id][char_idx], end=" ")