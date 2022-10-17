from util import *
from aes import aes

def main():
    #key path
    key_path = 'aes.key'
    #mode path
    mode_path = 'mode.txt'
    #key is read 
    key = readKey(key_path)
    #operation mode is read
    op_mode = readKey(mode_path)
    #aes object is created
    obj = aes(key,op_mode)
    #all round keys are generated
    obj.generateKeys()
    #encryption is done
    status = obj.encrypt()
    #decryption is done, if encryption is successful
    if status:
        obj.decrypt()

if __name__ == "__main__":
    main()