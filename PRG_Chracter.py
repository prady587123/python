print(" Enter the character")
varAscii = input()

print(" Entered Character " + varAscii)

if ((ord(varAscii) >= 65 & ord(varAscii) <= 90) & (ord(varAscii) >= 97 & ord(varAscii) <= 122)):
    print("The input given is a character")
else:
    print("The input given is not a character")

    """
    This is a test
    It will not be printed
    """