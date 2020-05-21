import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import sys
import struct

def main(argv):
    if len(argv) != 2:
        print("Usage: ECB.py <filename>")
        exit(0)
    if ".bmp" not in argv[1]:
        do_text_file(argv[1])

def do_text_file(filename):
    key = get_key();
    text = open_text_file(filename)
    crypto = AES.new(key, AES.MODE_ECB)
    encrypt = encrypt_text(text, crypto)
    print("key     {}".format(key))
    print("string: {}".format(encrypt))
    print("len:    {}".format(len(encrypt)))

def encrypt_text(text, crypto):
    encrypt = b""
    blocks = get_blocks(text)
    for block in blocks:
        encrypt = encrypt + encrypt_block(block, crypto)
    return encrypt

def get_blocks(text):
    blocks = []
    block = []
    i = 0
    for letter in text:
        block.append(letter)
        i += 1
        if i == 16:
            blocks.append("".join(block))
            block.clear()
            i = 0
    if len(block) != 0:
        blocks.append("".join(block))
    return blocks

def encrypt_block(block, crypto):
    if len(block) > 16:
        print("block size too large, must be 16 bytes or less")
        exit(1)
    new_block = add_pad(bytes(block, "ascii"))
    return crypto.encrypt(new_block)

def get_key():
    return Random.new().read(16)

def open_text_file(filename):
    f = open(filename, "r")
    lines = f.read()
    f.close()
    return lines

def add_pad(string):
    new_string = string
    if len(string) == 1:
        new_string = string + b"\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f"
    elif len(string) == 2:
        new_string = string + b"\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e"
    elif len(string) == 3:
        new_string = string + b"\x0d\x0d\x0d\x0d\x0d\x0d\x0d\x0d\x0d\x0d\x0d\x0d\x0d"
    elif len(string) == 4:
        new_string = string + b"\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c"
    elif len(string) == 5:
        new_string = string + b"\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b"
    elif len(string) == 6:
        new_string = string + b"\x0a\x0a\x0a\x0a\x0a\x0a\x0a\x0a\x0a\x0a"
    elif len(string) == 7:
        new_string = string + b"\x09\x09\x09\x09\x09\x09\x09\x09\x09"
    elif len(string) == 8:
        new_string = string + b"\x08\x08\x08\x08\x08\x08\x08\x08"
    elif len(string) == 9:
        new_string = string + b"\x07\x07\x07\x07\x07\x07\x07"
    elif len(string) == 10:
        new_string = string + b"\x06\x06\x06\x06\x06\x06"
    elif len(string) == 11:
        new_string = string + b"\x05\x05\x05\x05\x05"
    elif len(string) == 12:
        new_string = string + b"\x04\x04\x04\x04"
    elif len(string) == 13:
        new_string = string + b"\x03\x03\x03"
    elif len(string) == 14:
        new_string = string + b"\x02\x02"
    elif len(string) == 15:
        new_string = string + b"\x01"

    print("block:  {}".format(new_string))
    return new_string



if __name__ == '__main__':
    main(sys.argv)
