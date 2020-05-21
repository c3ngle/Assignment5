#from Crypto.Cipher import AES
import sys
import struct

def main(argv):
    if len(argv) != 2:
        print("Usage: ECB.py <filename>")
        exit(0)
    open_text_file(argv[1])
    string = "123456789ABCDEFG"
    string = add_pad(string)
    print("string: {}".format(string))
    print("len:    {}".format(len(string)))

def open_text_file(filename):
    f = open(filename, "r")
    f.close()

def add_pad(string):
    block = list(string)
    if len(string) == 1:
        block.extend(['\x0F','\x0F','\x0F','\x0F','\x0F','\x0F','\x0F','\x0F','\x0F','\x0F','\x0F','\x0F','\x0F','\x0F','\x0F'])
    elif len(string) == 2:
        block.extend(['\x0E','\x0E','\x0E','\x0E','\x0E','\x0E','\x0E','\x0E','\x0E','\x0E','\x0E','\x0E','\x0E','\x0E'])
    elif len(string) == 3:
        block.extend(['\x0D','\x0D','\x0D','\x0D','\x0D','\x0D','\x0D','\x0D','\x0D','\x0D','\x0D','\x0D','\x0D'])
    elif len(string) == 4:
        block.extend(['\x0C','\x0C','\x0C','\x0C','\x0C','\x0C','\x0C','\x0C','\x0C','\x0C','\x0C','\x0C'])
    elif len(string) == 5:
        block.extend(['\x0B','\x0B','\x0B','\x0B','\x0B','\x0B','\x0B','\x0B','\x0B','\x0B','\x0B'])
    elif len(string) == 6:
        block.extend(['\x0A','\x0A','\x0A','\x0A','\x0A','\x0A','\x0A','\x0A','\x0A','\x0A'])
    elif len(string) == 7:
        block.extend(['\x09','\x09','\x09','\x09','\x09','\x09','\x09','\x09','\x09'])
    elif len(string) == 8:
        block.extend(['\x08','\x08','\x08','\x08','\x08','\x08','\x08','\x08'])
    elif len(string) == 9:
        block.extend(['\x07','\x07','\x07','\x07','\x07','\x07','\x07'])
    elif len(string) == 10:
        block.extend(['\x06','\x06','\x06','\x06','\x06','\x06'])
    elif len(string) == 11:
        block.extend(['\x05','\x05','\x05','\x05','\x05'])
    elif len(string) == 12:
        block.extend(['\x04','\x04','\x04','\x04'])
    elif len(string) == 13:
        block.extend(['\x03','\x03','\x03'])
    elif len(string) == 14:
        block.extend(['\x02','\x02'])
    elif len(string) == 15:
        block.extend(['\x01'])

    print("block:  {}".format(block))
    return "".join(string)



if __name__ == '__main__':
    main(sys.argv)
