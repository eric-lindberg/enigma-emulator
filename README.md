# enigma-emulator
Simple Python emulator of an enigma machine. This is the first step in a toy NLP project I'm working on.

## The Enigma Machine
## Codes
The surprise for me in researching the Enigma machine is that it is fundamentally just an extended version of the old Caesar cipher, in which each character is substituted with another character offset in the alphabet. For example, with an offset of 2, "ABCD" becomes "CDEF". For those who remember spoiler-encodings from back in the days of 1990's Usenet forums, ROT-13 is just a specific instance of a Caesar code.

In a more complex version of the Caesar code, the offset is increased by one, modulo 26 (or whatever the size of your alphabet), for each character encoded. In this instance, with an initial offset of 2, "ABCD" becomes "CEGI", because the offset from "A" is 2, from "B" is 3, and so on. 

For further discussion of this, check out Harald Schmidl's [project](http://www.cs.miami.edu/home/harald/enigma) on the subject of Enigma, which I used extensively to validate my implementation.

### How Enigma Encodes a Character
For all practical purposes, the Enigma machine does a variation of this, mixed with a simple substitution cipher, but encoded three times in a row across all rotors, further encoded with a simple substitution cipher in the "Reflector". The encoding is then made backwards through the three rotors again. Finally, to further obfuscate the original character, both the input and the output are run through the "plugboard", in which some pairs of characters are swapped. As a character is encoded, the first rotor has its position advanced by one. When any rotor advances past "Z", the next rotor in order is advanced by one.

#### The Rotors and the Reflector
The sample config file sets up the rotors and plugboard. Each enigma machine made use of three out of five available rotors, arranged in a particular order. In this implementation, "rotor1" is the one the character is encoded through first in the first run, and last after going through the reflector.

Each type of rotor (numbered "I", "II", "III", "IV", and "V") had a different substitution cipher encoding built into it. The "position" setting ("rotor1Pos", "rotor2Pos", and "rotor3Pos") is started at a specific index offset between 0 and 25. (This was actually a letter value in the original machines.) The ring setting was an additional offset setting that could be used against each rotor.

#### The Plugboard
The plugboard was physically a series of plugs corresponding to each letter, each of which could be connected to another letter. As a result, no letter in a pair of connected letters can be connected to another letter. For example, if "A" is connected to "T", then "T" cannot be connected to any other letter. Also note that this means that "A" will be substituted for "T" both in the input and output characters, and also that "T" will be substituted for "A".

### Decoding the Message
The upshot of this encoding, reflection, and backwards encoding is that the Enigma machine will decode the word that was encoded if the machine is reset to the original settings. For example, using the default configuration here, "HELLO" will encode to "AMNCZ". If you then reset the system back to the original configuration settings and enter "AMNCZ", it should output "HELLO". There are some more interesting details in how the coded message can provide some hints about the rotor settings to use without necessarily giving away the code.

## Running the Application
The code runs using Python (version 3). In the directory containing the code, run "$ python3 Enigma.py"

`$ python3 Enigma.py`

`Input the message to be encoded`

`Only alphabetic values, without spaces or punctuation, are accepted.`

`Hit return without typing any message to exit.`

`Message -->`

Enter the text you'd like to encode and it will output the results. Enter a blank string to exit the app. If you then restart the app and enter the codes, you should get the original text back.

## Next Steps
If you'd like to comment or let me know of any errors, please post them on the blog entry (https://cheeseandpear.blogspot.com/2019/04/programming-doodle-enigma-emulator.html) or send me an email (elindberg@acm.org). My intention next is to start playing with decrypting strategies, probably focusing on modern NLP tools, rather than trying to mimic the actual methods, such as the Bombe or Banburismus. Though now that I think of it, those might be fun to try as well...

TODO:  Purely as a Python learning exercise, implement the Rotors structure as Python deque objects.

This is the purpose of the deque branch.

Working:  Basic_Deque_Rotor_Access.py

Run it to access the Rotor Class from the Deque_Rotor.py file which is a compound List object with a
Dict object, some ints, and 5 deque objects representing the Rotors of the Enigma Machine.

What we don't want to do is access all the Rotor Characters as if they are in a 2D array.  We want to emulate the
Rotation of the Rotors to simulate the mechanical function of the Enigma Machine.  Writing the deques as Rotors,
we can easily simulate their Rotation, which should simplify the index math of the original program.