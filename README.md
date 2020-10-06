# pwdgen

Password generator for the command line, written in python

## What does it do?

Well... it generates passwords. There are currently 4 types: pin, password, crypt and aaa

### pin

Generates a pin with digits between 0 and 9 (0 1 2 3 4 5 6 7 8 9)

### password

Generates a password. It doesn't include all special characters, only "!@#\$%&\*()\_-+={[]}|:;<,>.?/"

### crypt

contains numbers, ascii letters and punctuation

### aaa

ÀâÃÀÅAÃÁÃAÆÀÅÃÀãāāÁâäáÀåäaÁÃāäÆÂaÅâååàåáåâāÀAàâÁÃà

## Installation

You need:

- python 3
- pip3
- 1 minute

You could just leave the file here, navigate to this directory and run `python3 pwdgen.py`, but that's inconvenient.
I copied the file to `/usr/local/bin` and removed the `.py` file extension so i can run `pwdgen` from everywhere. Might require a terminal relaunch, idk

And yeah, you need the dependencies. Run `pip3 install -r requirements.txt` from this directory and it should automagically install all dependencies.

## Usage

`pwdgen -pwd|-pin|-crypt|-aaa [-cp] -l L`

Everything in [] is optional
When there's a horizontal line (|), you can choose

- -pwd

  - generates a password

- -pin

  - generates a pin

- -crypt

  - generates a random string

- -aaa

  - ÅÁäãæäaàåaÃAÄáÂæaĀÂàäÃååáÀĀĀÄÅàaÆAAÄâaaâåäàAæÃÁāÄĀ

- -cp

  - copies the result

- l L
  - length of the string (L = integer)

# License

This project is licensed under the MIT License. Read [LICENSE](LICENSE) for more information
