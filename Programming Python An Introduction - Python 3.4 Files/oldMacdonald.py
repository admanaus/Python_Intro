# oldMacdonald.py

def farm():
    farm = 'Old Macdonald had a farm,'
    return farm

def Oh():
    Oh = 'Ee-igh, Ee-igh, Oh!'
    return Oh

def oldMac(animal, sound):
    print(farm(), Oh())
    doubleSound = sound + ', ' + sound
    print('And on that farm he had a', animal+',', Oh())
    print('With a', doubleSound, 'here and a', doubleSound, 'there.')
    print('Here a', sound, 'there a', sound, 'everywhere a', doubleSound)
    print(farm(), Oh())
    return 

def main():
    animal = input('Enter an animal name: ')
    sound = input('Enter an animal sound: ')
    song = oldMac(animal, sound)
    print(song)
main()
