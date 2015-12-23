from Crypto.Cipher import AES
import base64


if __name__ == '__main__':
    key = 'a2ffa5c9be07488bbb04a3a47d3c5f6a'
    mode = AES.MODE_CBC
    # iv = '64175472480004614961023454661220'
    encryptor = AES.new(key, mode)
    text = 'j' * 64 + 'i' * 128
    ciphertext = encryptor.encrypt(text)
    t = base64.b64encode(ciphertext)
    print t