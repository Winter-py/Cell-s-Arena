#Password Generator
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
signs = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "~", "`", ";", ":", "'", "\"", ",", ".", "/", "<", ">", "?", "|"]

passwordgenerator = input("Would you like to generate a password? Y/N ")
if passwordgenerator == "Y" or "y":
    passwordlength = int(input("How long would you like your password to be? "))
    password = ""
    for i in range(passwordlength):
        password += random.choice(letters + numbers + signs)
    print("Your password is: " + password)