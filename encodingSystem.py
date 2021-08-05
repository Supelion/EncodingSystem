import time
import os

os.system("cls")
print("\n\nWelcome to Supelion's encoding and decrypting system!")
time.sleep(2)
print("\n\nNOTE: This only works for lowercase letters and alphabets because I am too lazy to map all the others lol")
time.sleep(1)

op = input("\n\nOperation: (encode / decode) ")
operation = op.lower()

def encode(input):
    encodeMapping = {
        ord("a"): "h",
        ord("b"): "g",
        ord("c"): "q",
        ord("d"): "l",
        ord("e"): "a",
        ord("f"): "r",
        ord("g"): "v",
        ord("h"): "w",
        ord("i"): "f",
        ord("j"): "m",
        ord("k"): "b",
        ord("l"): "c",
        ord("m"): "z",
        ord("n"): "u",
        ord("o"): "x",
        ord("p"): "o",
        ord("q"): "p",
        ord("r"): "j",
        ord("s"): "d",
        ord("t"): "e",
        ord("u"): "i",
        ord("v"): "k",
        ord("w"): "n",
        ord("x"): "s",
        ord("y"): "t",
        ord("z"): "y"
    }
    return input.translate(encodeMapping)

def decode(input):
    decodeMapping = {
        ord("h"): "a",
        ord("g"): "b",
        ord("q"): "c",
        ord("l"): "d",
        ord("a"): "e",
        ord("r"): "f",
        ord("v"): "g",
        ord("w"): "h",
        ord("f"): "i",
        ord("m"): "j",
        ord("b"): "k",
        ord("c"): "l",
        ord("z"): "m",
        ord("u"): "n",
        ord("x"): "o",
        ord("o"): "p",
        ord("p"): "q",
        ord("j"): "r",
        ord("d"): "s",
        ord("e"): "t",
        ord("i"): "u",
        ord("k"): "v",
        ord("n"): "w",
        ord("s"): "x",
        ord("t"): "y",
        ord("y"): "z"
    }
    return input.translate(decodeMapping)

if operation == "encode":

    userIn = input("Enter a string to encode:   ")
    userInput = userIn.lower()
    print(encode(userInput))

elif operation == "decode":

    userIn = input("Enter a string to decode:  ")
    userInput = userIn.lower()
    print(decode(userInput))

else:
    print("Invalid Input!")