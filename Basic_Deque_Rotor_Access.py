from Deque_Rotor import Rotors

rotor = Rotors(1,2,3)

print(rotor.ring, rotor.pos, rotor.rotor_id)
print(rotor.Rotor[1][2])

for rotor_id in range(0, 5):
    for char_idx in range (0, 26):
        print(rotor_id, char_idx)
        print(rotor.Rotor[rotor_id][char_idx], end=" ")
print()
print(rotor.rotor_ids)
print(rotor.rotor_ids[3])
print(rotor.rotor_ids[6])
for x in rotor.rotor_ids:
    print(x, end=' ')
# print(rotor.rotor_ids('III'))
print()
print(rotor.rotor_ids.keys())


'''
# Python program to demonstrate   
# accesing a element from a Dictionary  
  
# Creating a Dictionary  
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 
  
# accessing a element using key 
print("Acessing a element using key:") 
print(Dict['name']) 
  
# accessing a element using key 
print("Acessing a element using key:") 
print(Dict[1]) 
  
# accessing a element using get() 
# method 
print("Acessing a element using get:") 
print(Dict.get(3)) 

'''