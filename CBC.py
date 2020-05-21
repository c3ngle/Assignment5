from Crypto.Cipher import AES
from Crypto import Random
import sys
import struct

def main(argv):
    if len(argv) != 2:
        print("Usage: CBC.py <filename>")
        exit(0)
    if ".bmp" not in argv[1]:
        encrypt_text_file(argv[1])


def encrypt_text_file(filename):
    text = open_text_file(filename)
    key = get_key()
    crypto = AES.new(key, AES.MODE_ECB)
    encrypt = encrypt_text(text, crypto)
    print("output: {}".format(encrypt))
    print("len:    {}".format(len(encrypt)))


def encrypt_text(text, crypto):
    t = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" # IV
    blocks = get_blocks(text)
    for block in blocks:
        t = encrypt_block(block, crypto, t)
    return t


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


def encrypt_block(block, crypto, t):
    if len(block) > 16 or len(t) > 16:
        print("block or t is too large, they must be 16 bytes or less")
        exit(1)

    block = add_pad(bytes(block, "ascii"))
    new_block = XOR_bytes(block, t)
    return crypto.encrypt(new_block)


def XOR_bytes(bytes1, bytes2):
    new_bytes = b""
    for i in range(len(bytes1)):
        new_bytes = new_bytes + bytes([bytes1[i] ^ bytes2[i]])
    return new_bytes


def open_text_file(filename):
    f = open(filename, "r")
    text = f.read()
    f.close()
    return text


def get_key():
    return Random.new().read(16)


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
