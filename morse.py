morse_dictionary = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    " ": "/"
}
convert = ""

print("1. Text to Morse Code\n2. Morse Code to Text")
x = input("Choose what you want to do: ")
if x == "1":
    text = "`"
    while len(text.strip("abcdefghijklmnopqrstuvwxyz1234567890.,? ")) != 0:
        text = input("Enter a Text to convert to Morse Code: ")
        text = text.lower()
        if len(text.strip("abcdefghijklmnopqrstuvwxyz1234567890.,? ")) != 0:
            print("Invalid text")

    for i in range(len(text)):
        convert += morse_dictionary.get(text[i]) + " "
    print("The Morse Code is:", convert)
elif x == "2":
    text = input("Enter your Morse Code to convert to Text: ").split(" ")

    for i in range(len(text)):
        try:
            convert += list(morse_dictionary.keys())[list(morse_dictionary.values()).index(text[i])]
        except:
            print("Invalid text")
            break
    print("The Text is:", convert.upper())


