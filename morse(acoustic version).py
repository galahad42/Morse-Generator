import winsound                                     
from time import sleep


general = {'a': '.-',
           'b': '-...',
           'c': '-.-.',
           'd': '-..',
           'e': '.',
           'f': '..-.',
           'g': '--.',
           'h': '....',
           'i': '..',
           'j': '.---',
           'k': '-.-',
           'l': '.-..',
           'm': '--',
           'n': '-.',
           'o': '---',
           'p': '.--.',
           'q': '--.-',
           'r': '.-.',
           's': '...',
           't': '-',
           'u': '..-',
           'v': '...-',
           'w': '.--',
           'x': '-..-',
           'y': '-.--',
           'z': '--..',
           '1': '.----',
           '2': '..---',
           '3': '...--',
           '4': '....-',
           '5': '.....',
           '6': '-....',
           '7': '--...',
           '8': '---..',
           '9': '----.',
           '10': '-----', 
           ' ': ' ',
           '.': '.-.-.-',
           ',': '--..--',
           '?': '..--..'
}
convertedData = []


def dit():                                        
    frequence = 1500
    alarmTime = 150
    winsound.Beep(frequence, alarmTime)


def dah():                                        
    frequence = 1500
    alarmTime = 1500
    winsound.Beep(frequence, alarmTime)


def breaks():                                     
    sleep(5)



def verifyMsg(msg):                                            
    for char in msg:
        convertedData.append(general[char])


def soundMsg(msg_list):                                 
    for char in msg_list:
        print(char)
        sleep(1)
        if (char == ' '):
            breaks()
        for element in char:
            if (element == '.'):
                dit()
            elif (element == '-'):
                dah()


def cleaningData(dataList):
    dataList.clear()


def callFunctions():
    verifyMsg(userMsg)
    soundMsg(convertedData)
    cleaningData(convertedData)



while (True):
    try:
       
        userMsg = input(str('Enter your message: ')).lower()
        callFunctions()

    except KeyError:
        print('Invalid text, please type your text again')
