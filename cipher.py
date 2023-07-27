caesar_cipher = {
    "a": "f",
    "b": "g",
    "c": "h",
    "d": "i",
    "e": "j",
    "f": "k",
    "g": "l",
    "h": "m",
    "i": "n",
    "j": "o",
    "k": "p",
    "l": "q",
    "m": "r",
    "n": "s",
    "o": "t",
    "p": "u",
    "q": "v",
    "r": "w",
    "s": "x",
    "t": "y",
    "u": "z",
    "v": "a",
    "w": "b",
    "x": "c",
    "y": "d",
    "z": "e",
}

sentence = input("Please enter a sentence: ")

encrypted = []

for letter in sentence:
    if letter.isalpha():
        encrypted.append(caesar_cipher.get(letter.lower(), letter.lower()))
    else:
        encrypted.append(letter.lower())
print(f"The encrypted sentence is: {''.join(encrypted)}")
# This is the finished code!!
