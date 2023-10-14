from machine import Pin
from time import sleep
import utime

led = Pin(25, Pin.OUT)
UserLocVar = []
UserInput = input('\tEnter the message to be encoded below\n\tOnly input lower alphabet or morse sequences : ')
AlsoUserOutput = ''

UserDictnr = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..','e':'.', 'f':'..-.',
            'g':'--.', 'h':'....','i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..',
            'm':'--', 'n':'-.', 'o':'---', 'p':'.--.','q':'--.-', 'r':'.-.', 
            's':'...', 't':'-','u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-',
            'y':'-.--', 'z':'--..'}

AlsoUserDictnr = {'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e', '..-.':'f',
            '--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k', '.-..':'l',
            '--':'m', '-.':'n', '---':'o', '.--.':'p', '--.-':'q', '.-.':'r', 
            '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x',
            '-.--':'y', '--..':'z'}

if UserInput.islower() == True:
    print('\n\tMorse code script:')
    for i in range(len(UserInput)):
        UserOutput = UserDictnr.get(UserInput[i],' ')
        print(UserOutput)
        UserLocVar.append(UserOutput)
    print('\n\tMorse LED sequence')
    for i in range(len(UserLocVar)):
        for j in range(len(UserLocVar[i])):
            if UserLocVar[i][j] == '.':
                print(UserLocVar[i][j])
                led.value(1)
                utime.sleep(0.3)
                led.value(0)
                utime.sleep(0.3)
            elif UserLocVar[i][j] == '-':
                print(UserLocVar[i][j])
                led.value(1)
                utime.sleep(1)
                led.value(0)
                utime.sleep(0.3)
            else:
                led.value(0)
                
else:            
    UserLocVar += UserInput.split()

    for i in range(len(UserLocVar)):
        if UserLocVar[i] in UserDictnr.values():
            AlsoUserOutput += AlsoUserDictnr.get(UserLocVar[i])    
        else:
            print('\tWrong text or morse sequence entered please try again')
        
print(AlsoUserOutput)
print('\tEnd of session')
