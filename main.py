from random import randint

letterCharacters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                   "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                   "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", ",",
                   ".", "/", "<", ">", "?", ":", ";", "\'", "\"", "[", "]", "{", "}", "\\", "|", " ", "`", "~", "¡", "£", "¥", "º", "¤"]
numberCharacters = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                    "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41",
                    "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62",
                    "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83",
                    "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99"]


def convertToNumber(inputChar):
    return numberCharacters[letterCharacters.index(inputChar)]


def convertToLetter(inputChar):
    return letterCharacters[numberCharacters.index(inputChar)]


def cipherText(inputText):
    numberText = ""
    numberText += str(randint(0, 9))

    for i in range(len(inputText)):
        numberText += convertToNumber(inputText[i])

        if (i + 1) % 2 == 0:
            numberText += str(randint(0, 9))
            numberText += str(randint(0, 9))

    numberText += str(randint(0, 9))

    outputText = ""

    for i in range(0,len(numberText),2):
        twoDigitChar = str(numberText[i]) + str(numberText[i+1])
        outputText += convertToLetter(twoDigitChar)

    return outputText


def decipherText(inputText):
    numberText = ""

    for i in range(len(inputText)):
        numberText += convertToNumber(inputText[i])

    stripOuterText = ""

    for i in range(len(numberText)):
        if i == 0:
            continue
        if i == len(numberText) - 1:
            continue
        stripOuterText += numberText[i]

    outputText = ""
    index = 0
    count = 1

    while index < len(stripOuterText):
        if count % 3 == 0:
            index += 2
            count += 1
            continue

        twoDigitChar = stripOuterText[index] + stripOuterText[index + 1]
        outputText += convertToLetter(twoDigitChar)

        index += 2
        count += 1

    return outputText


def menu():
    choice = "0"

    while choice != "q":
        inputText = ""
        outputText = ""

        print("What would you like to do?")
        print("1. Cipher")
        print("2. Decipher")
        print("q. Quit")
        choice = str(input())

        if choice == "1":
            inputText = input("What would you like to cipher?\n")
            outputText = cipherText(inputText)
            print()
            print(f"Ciphered Text:\t{outputText}")
            print()

        elif choice == "2":
            inputText = input("What would you like to decipher?\n")
            outputText = decipherText(inputText)
            print()
            print(f"Deciphered Text:\t{outputText}")
            print()

    print("Bye!")


if __name__ == "__main__":
    menu()
