from Crypto.Cipher import AES
from Crypto import Random

def main():
    key = get_key()
    IV = get_IV()
    crypto = AES.new(key, AES.MODE_ECB)
    encrypt = submit(crypto, IV)
    print("encrypt: {}".format(encrypt))
    valid = verify(encrypt, crypto, IV)
    print("valid: {}".format(valid))


def submit(crypto, IV):
    text = get_text()
    print("text: {}".format(text))
    encrypt = encrypt_text(text, crypto, IV)
    return encrypt

def verify(encrypt, crypto, IV):
    decrypt = decrypt_text(encrypt, crypto, IV)
    if ";admin=true;" in decrypt:
        decrypt = URL_decode(decrypt)
        print("decrypt: {}".format(decrypt))
        return True
    decrypt = URL_decode(decrypt)
    print("decrypt: {}".format(decrypt))
    return False


def decrypt_text(text, crypto, IV):
    t = IV
    blocks = get_blocks_bytes(text)
    decrypt = b""
    for block in blocks:
        string = crypto.decrypt(block)
        decrypt = decrypt + XOR_bytes(string, t)
        t = block
    return str(decrypt, "ascii")


def get_blocks_bytes(text):
    blocks = []
    block = b""
    i = 0
    for byte in text:
        block = block + bytes([byte])
        i += 1
        if i == 16:
            blocks.append(block)
            block = b""
            i = 0
    if len(block) != 0:
        blocks.append(block)
    return blocks

def encrypt_text(text, crypto, IV):
    t = IV
    encrypt = b""
    blocks = get_blocks(text)
    for block in blocks:
        t = encrypt_block(block, crypto, t)
        encrypt = encrypt + t
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


def get_text():
    text = input("enter string: ")
    text = URL_encode(text)
    new_text = "userid=456;userdata=" + text + ";session-id=31337"
    return new_text;


def URL_encode(text):
    out_text = text
    if ";" in text:
        i = text.find(";")
        new_text = text[:i] + "%3B" + text[i+1:] # removes the ; and replaces with %3B
        out_text = URL_encode(new_text) # calls again to check if there are more ; or =
    if "=" in text:
        i = text.find("=")
        new_text = text[:i] + "%3D" + text[i+1:] # removes the = replaces with %3D
        out_text = URL_encode(new_text) # calls again to check if there are more =
    return out_text


def URL_decode(text):
    out_text = text
    if "%3B" in text:
        i = text.find("%3B")
        new_text = text[:i] + ";" + text[i+3:]
        out_text = URL_decode(new_text)
    if "%3D" in text:
        i = text.find("%3D")
        new_text = text[:i] + "=" + text[i+3:]
        out_text = URL_decode(new_text)
    return out_text


def get_key():
    return Random.new().read(16)

# repeated for readablility
def get_IV():
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

    #print("block:  {}".format(new_string))
    return new_string




if __name__ == '__main__':
    main()
