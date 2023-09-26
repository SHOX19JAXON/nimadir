morse = {"-----": "0", ".----": "1", "..--": "2", "...--": "3", "....-": "4", ".....":"5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",}
soz = input("Morze alifbosidan so'z kiriting: ").split(" ")

for i in soz:
    for keys, values in morse.items():
        if i in keys:
            print(values, end = "")

