from util import *
import copy

#AES class is created
class aes:
    #Attributes of class
    __key0 = None
    __keylist = []
    __aesmode = 128
    __loop_condition = 10
    __key_mat=None
    __rounds = 10
    __opmode = 'ECB'
    __IV = None
    __key_status = True
    __op_status  = True

    #Initialization Function of Class
    def __init__(self,key='00000000000000000000000000000000',opmode = 'ECB'):
        #Key and Operation Mode is assigned
        self.setKey(key)
        self.__opmode = opmode.upper()
        print('Key0 is: ',self.__key0)
        print('Mode is: ',self.__opmode)

        #IV is generated, if mode is CBC
        if self.__opmode == 'CBC':
            self.__IV = generateIV()
            print('Initialization Vector: ',self.__IV)
        print('AES type is:',len(self.__key0)*4)

        #Number of Rounds are set
        self.setLength(len(self.__key0)*4)

        #Status is set to check, if key and mode are correct or not
        if len(self.__key0) not in (32,48,64):
            self.__key_status = False
        if self.__opmode != 'ECB' and self.__opmode != 'CBC':
            self.__op_status = False

    #Setter Function for key
    def setKey(self,key):
        self.__key0 = key
        self.__aesmode = len(key)*4

    #Function to generate n round keys 
    def generateKeys(self):
        #Matrix for key0 is generated
        self.__key_mat = generateMatrix(self.__key0)
        #copy of matrix is made
        temp_key_mat = copy.deepcopy(self.__key_mat)

        #Loop to make n round keys
        for i in range(self.__loop_condition):
            #Rotation is applied on key
            key_rot = rotateWord(copy.deepcopy(temp_key_mat))
            #Sbox is applied
            key_box = subWord(key_rot)
            #RCON is added to key after sbox operation
            xor_sub_rcon = XOR(key_box,RCON[i])
            #Answer is added to each row of current round key
            temp_key_mat = keyExpandXOR(temp_key_mat,xor_sub_rcon)
            #Final key is appended to list
            self.__keylist.append(temp_key_mat)
        #Finally, keys are rearranged if keys are of size 6x4 or 8x4 to get them in 4x4 form
        if self.__aesmode == 192 or self.__aesmode == 256:
            self.__keylist = rearrange(self.__keylist,self.__aesmode,self.__key_mat)
        # self.printKeys()

    #Function to print all round keys
    def printKeys(self):
        for i in range(len(self.__keylist)):
            print('Key'+str(i+1)+': ',self.__keylist[i])

    #Length of loop for encryption and key generation is set
    def setLength(self,mode):
        self.__aesmode = mode
        if mode == 128:
            self.__loop_condition = 10
            self.__rounds = 10
        elif mode == 192:
            self.__loop_condition = 8
            self.__rounds = 12
        else:
            self.__loop_condition = 7
            self.__rounds = 14

    #Function for encrypting plaintext to ciphertext using AES
    def encrypt(self):
        #If key length is not correct, then function returns
        if not self.__key_status:
            print('Key Length is not Correct!')
            return False
        #If operation mode is not correct, then function returns
        elif not self.__op_status:
            print('AES Operation Mode Incorrect!')
            return False
        #Plaintext is read in list of strings
        plain = readText('plain.pt')
        #Length of each string is checked, if length is less than 32 then padding is applied
        plain = checkPadding(plain)

        #List of store ciphers
        cipher = []
        #Loop to encrypt each block of plaintext
        for index in range(len(plain)):
            #Plaintext string is converted in matrix form
            plain_mat = generateMatrix(plain[index])

            #if mode is CBC, then IV is added to plaintext if first block else ciphertext of last block is added
            if self.__opmode == 'CBC':
                if index == 0:
                    plain_mat = XORMatrix(plain_mat,generateMatrix(self.__IV))
                else:
                    plain_mat = XORMatrix(plain_mat,last_result)

            #Round key 0 is added to plaintext
            addRoundKey0 = XORMatrix(plain_mat,self.__key_mat)
            last_result = addRoundKey0
            # print('Add Round Key0:',addRoundKey0)
            
            #Loop to pass plaintext through n number of rounds depending on AES type (128, 192, 256 etc)
            for i in range(self.__rounds):
                # print('Round '+str(i+1))
                # SBox is applied on matrix
                sub_mat = subMat(last_result)
                # print('Sub Mat: ',sub_mat)
                # Shift Rows Left is applied on matrix
                shift_mat = shiftMat(sub_mat)
                # print('Shift Rows:',shift_mat)

                #If not last round then mix column multiplication is also done
                if i == self.__rounds - 1:
                    mixColRes = shift_mat
                else:
                    mixColRes = mixColMult(shift_mat)
                    # print('Mix Columns:',mixColRes)

                #Lastly, current round key is added
                last_result = XORMatrix(mixColRes,self.__keylist[i])
                # print('Add Round Key'+str(i+1)+': ',last_result)
            #After n rounds, cipher is added to list
            cipher.append(last_result)
        #List containing ciphertext for each block is passed to function to store in file
        writeText(cipher,'encrypted.enc')
        return True
    
    #Function to decrypt ciphertext into plaintext using AES
    def decrypt(self):
        #Ciphertext is read
        cipher = readText('encrypted.enc')
        # print(cipher)

        #List to store plaintext
        plain = []
        #Loop to decrypt each block of ciphertext
        for index in range(len(cipher)):
            #Plaintext string is converted in matrix form
            cipher_mat = generateMatrix(cipher[index])
            #Round key0 is added to matrix
            addRoundkeyLast = XORMatrix(cipher_mat,self.__keylist[len(self.__keylist)-1])
            last_result = addRoundkeyLast
            # print('Add Round key Last: ',addRoundkeyLast)

            #Loop to pass plaintext through n number of rounds depending on AES type (128, 192, 256 etc)
            for i in range(self.__rounds):
                # print('Round '+str(i+1))
                # Shift Rows right is applied on matrix
                shift_mat = IshiftMat(last_result)
                # print('Inverse Shift Mat: ',shift_mat)
                # Inverse SBox is applied on matrix
                sub_mat = IsubMat(shift_mat)
                # print('Inverse Sub Mat: ',sub_mat)

                #If not last round then inverse mix column multiplication is also done after adding n round key else just key is added
                if i == self.__rounds - 1:
                    last_result = XORMatrix(sub_mat,self.__key_mat)
                else:
                    # print(self.__keylist[self.__rounds-2-i])
                    add_key = XORMatrix(sub_mat,self.__keylist[self.__rounds-2-i])
                    # print(add_key)
                    last_result = ImixColMult(add_key)
                    # print(last_result)
            #Lastly, if mode is CBC, then IV is added if first block else ciphertext of last block is added
            if self.__opmode == 'CBC':
                if index == 0:
                    last_result = XORMatrix(last_result,generateMatrix(self.__IV))
                else:
                    last_result = XORMatrix(generateMatrix(cipher[index-1]),last_result)
            #After n rounds plaintext is appended to list
            plain.append(last_result)
        #List containing plaintext for each block is passed to function to store in file
        writeText(plain,'decrypted.dec')