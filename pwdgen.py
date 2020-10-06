#!/usr/bin/env python3

#
# pwdgen
# Made by Lea Baumgart
# Licensed under the MIT License
#
# This is probably bad code, but it works™
# If you wanna use it, please read README.md
#


import secrets
import string
import argparse
import pyperclip

parser = argparse.ArgumentParser()
parser.add_argument('-l', type=int, help="Password length", required=True)
parser.add_argument('-pin', help="Type: pin", action='store_const', const='pin')
parser.add_argument('-pwd', help="Type: password", action='store_const', const='pwd')
parser.add_argument('-crypt', help="Type: crypt", action='store_const', const='crypt')
parser.add_argument('-aaa', help="Type: aaaaaaaaaaaaa", action='store_const', const='aaa')
parser.add_argument('-cp', '--copy', help="Copy to clipboard", action='store_const', const=True)
args = parser.parse_args()

if (args.l) and ((args.pin) or (args.pwd) or (args.crypt) or (args.aaa)):
    length = int(args.l)
    if (args.pin):
        alphabet = string.digits
        pin = ''.join(secrets.choice(alphabet) for i in range(length))
        print(pin)
        if (args.copy):
            pyperclip.copy(pin)
    elif (args.crypt):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        print(password)
        if (args.copy):
            pyperclip.copy(password)
    elif (args.aaa):
        alphabet = "aäàáâæãåāAÄÀÁÂÆÃÅĀ"
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        print(password)
        if (args.copy):
            pyperclip.copy(password)
    elif (args.pwd):
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()_-+={[]}|:;<,>.?/"
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        print(password)
        if (args.copy):
            pyperclip.copy(password)

    else:
        print("Invalid password type")
    
else:
    print("some arguments are missing")