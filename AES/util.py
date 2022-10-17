import copy
import random

#Sbox Stored in Dictionary of Dictonaries
SBox = {
'0':{'0':'63','1':'7C','2':'77','3':'7B','4':'F2','5':'6B','6':'6F','7':'C5','8':'30','9':'01','A':'67','B':'2B','C':'FE','D':'D7','E':'AB','F':'76'},
'1':{'0':'CA','1':'82','2':'C9','3':'7D','4':'FA','5':'59','6':'47','7':'F0','8':'AD','9':'D4','A':'A2','B':'AF','C':'9C','D':'A4','E':'72','F':'C0'},
'2':{'0':'B7','1':'FD','2':'93','3':'26','4':'36','5':'3F','6':'F7','7':'CC','8':'34','9':'A5','A':'E5','B':'F1','C':'71','D':'D8','E':'31','F':'15'},
'3':{'0':'04','1':'C7','2':'23','3':'C3','4':'18','5':'96','6':'05','7':'9A','8':'07','9':'12','A':'80','B':'E2','C':'EB','D':'27','E':'B2','F':'75'},
'4':{'0':'09','1':'83','2':'2C','3':'1A','4':'1B','5':'6E','6':'5A','7':'A0','8':'52','9':'3B','A':'D6','B':'B3','C':'29','D':'E3','E':'2F','F':'84'},
'5':{'0':'53','1':'D1','2':'00','3':'ED','4':'20','5':'FC','6':'B1','7':'5B','8':'6A','9':'CB','A':'BE','B':'39','C':'4A','D':'4C','E':'58','F':'CF'},
'6':{'0':'D0','1':'EF','2':'AA','3':'FB','4':'43','5':'4D','6':'33','7':'85','8':'45','9':'F9','A':'02','B':'7F','C':'50','D':'3C','E':'9F','F':'A8'},
'7':{'0':'51','1':'A3','2':'40','3':'8F','4':'92','5':'9D','6':'38','7':'F5','8':'BC','9':'B6','A':'DA','B':'21','C':'10','D':'FF','E':'F3','F':'D2'},
'8':{'0':'CD','1':'0C','2':'13','3':'EC','4':'5F','5':'97','6':'44','7':'17','8':'C4','9':'A7','A':'7E','B':'3D','C':'64','D':'5D','E':'19','F':'73'},
'9':{'0':'60','1':'81','2':'4F','3':'DC','4':'22','5':'2A','6':'90','7':'88','8':'46','9':'EE','A':'B8','B':'14','C':'DE','D':'5E','E':'0B','F':'DB'},
'A':{'0':'E0','1':'32','2':'3A','3':'0A','4':'49','5':'06','6':'24','7':'5C','8':'C2','9':'D3','A':'AC','B':'62','C':'91','D':'95','E':'E4','F':'79'},
'B':{'0':'E7','1':'C8','2':'37','3':'6D','4':'8D','5':'D5','6':'4E','7':'A9','8':'6C','9':'56','A':'F4','B':'EA','C':'65','D':'7A','E':'AE','F':'08'},
'C':{'0':'BA','1':'78','2':'25','3':'2E','4':'1C','5':'A6','6':'B4','7':'C6','8':'E8','9':'DD','A':'74','B':'1F','C':'4B','D':'BD','E':'8B','F':'8A'},
'D':{'0':'70','1':'3E','2':'B5','3':'66','4':'48','5':'03','6':'F6','7':'0E','8':'61','9':'35','A':'57','B':'B9','C':'86','D':'C1','E':'1D','F':'9E'},
'E':{'0':'E1','1':'F8','2':'98','3':'11','4':'69','5':'D9','6':'8E','7':'94','8':'9B','9':'1E','A':'87','B':'E9','C':'CE','D':'55','E':'28','F':'DF'},
'F':{'0':'8C','1':'A1','2':'89','3':'0D','4':'BF','5':'E6','6':'42','7':'68','8':'41','9':'99','A':'2D','B':'0F','C':'B0','D':'54','E':'BB','F':'16'}
}

#Inverse Sbox Stored in Dictionary of Dictonaries
ISBox = {
'0':{'0':'52','1':'09','2':'6A','3':'D5','4':'30','5':'36','6':'A5','7':'38','8':'BF','9':'40','A':'A3','B':'9E','C':'81','D':'F3','E':'D7','F':'FB'},
'1':{'0':'7C','1':'E3','2':'39','3':'82','4':'9B','5':'2F','6':'FF','7':'87','8':'34','9':'8E','A':'43','B':'44','C':'C4','D':'DE','E':'E9','F':'CB'},
'2':{'0':'54','1':'7B','2':'94','3':'32','4':'A6','5':'C2','6':'23','7':'3D','8':'EE','9':'4C','A':'95','B':'0B','C':'42','D':'FA','E':'C3','F':'4E'},
'3':{'0':'08','1':'2E','2':'A1','3':'66','4':'28','5':'D9','6':'24','7':'B2','8':'76','9':'5B','A':'A2','B':'49','C':'6D','D':'8B','E':'D1','F':'25'},
'4':{'0':'72','1':'F8','2':'F6','3':'64','4':'86','5':'68','6':'98','7':'16','8':'D4','9':'A4','A':'5C','B':'CC','C':'5D','D':'65','E':'B6','F':'92'},
'5':{'0':'6C','1':'70','2':'48','3':'50','4':'FD','5':'ED','6':'B9','7':'DA','8':'5E','9':'15','A':'46','B':'57','C':'A7','D':'8D','E':'9D','F':'84'},
'6':{'0':'90','1':'D8','2':'AB','3':'00','4':'8C','5':'BC','6':'D3','7':'0A','8':'F7','9':'E4','A':'58','B':'05','C':'B8','D':'B3','E':'45','F':'06'},
'7':{'0':'D0','1':'2C','2':'1E','3':'8F','4':'CA','5':'3F','6':'0F','7':'02','8':'C1','9':'AF','A':'BD','B':'03','C':'01','D':'13','E':'8A','F':'6B'},
'8':{'0':'3A','1':'91','2':'11','3':'41','4':'4F','5':'67','6':'DC','7':'EA','8':'97','9':'F2','A':'CF','B':'CE','C':'F0','D':'B4','E':'E6','F':'73'},
'9':{'0':'96','1':'AC','2':'74','3':'22','4':'E7','5':'AD','6':'35','7':'85','8':'E2','9':'F9','A':'37','B':'E8','C':'1C','D':'75','E':'DF','F':'6E'},
'A':{'0':'47','1':'F1','2':'1A','3':'71','4':'1D','5':'29','6':'C5','7':'89','8':'6F','9':'B7','A':'62','B':'0E','C':'AA','D':'18','E':'BE','F':'1B'},
'B':{'0':'FC','1':'56','2':'3E','3':'4B','4':'C6','5':'D2','6':'79','7':'20','8':'9A','9':'DB','A':'C0','B':'FE','C':'78','D':'CD','E':'5A','F':'F4'},
'C':{'0':'1F','1':'DD','2':'A8','3':'33','4':'88','5':'07','6':'C7','7':'31','8':'B1','9':'12','A':'10','B':'59','C':'27','D':'80','E':'EC','F':'5F'},
'D':{'0':'60','1':'51','2':'7F','3':'A9','4':'19','5':'B5','6':'4A','7':'0D','8':'2D','9':'E5','A':'7A','B':'9F','C':'93','D':'C9','E':'9C','F':'EF'},
'E':{'0':'A0','1':'E0','2':'3B','3':'4D','4':'AE','5':'2A','6':'F5','7':'B0','8':'C8','9':'EB','A':'BB','B':'3C','C':'83','D':'53','E':'99','F':'61'},
'F':{'0':'17','1':'2B','2':'04','3':'7E','4':'BA','5':'77','6':'D6','7':'26','8':'E1','9':'69','A':'14','B':'63','C':'55','D':'21','E':'0C','F':'7D'}
}

#Hex to Binary Mapping is stored in dictionary
hex_bin_dict = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}

#RCONS of upto 10 rounds are stored
RCON = [
['01','00','00','00'], 
['02','00','00','00'], 
['04','00','00','00'], 
['08','00','00','00'], 
['10','00','00','00'], 
['20','00','00','00'], 
['40','00','00','00'], 
['80','00','00','00'], 
['1B','00','00','00'], 
['36','00','00','00']
]

#Mix Column Matrix is stored
MixColumn = [['02','01','01','03'],['03','02','01','01'],['01','03','02','01'],['01','01','03','02']]

#Inverse Mix Column Matrix is stored
IMixColumn = [['0E','09','0D','0B'],['0B','0E','09','0D'],['0D','0B','0E','09'],['09','0D','0B','0E']]

#Function to read key from file
def readKey(filepath):
    f = open(filepath,'r')
    key = f.read()
    #Removes newline characters (if any)
    key = key.strip()
    f.close()
    return key

#Function to generate matrix from string in Nx4 form
def generateMatrix(key):
    #Calculating number of rows
    size = int(len(key)/8)
    mat = []
    #Iterating for n rows
    for i in range(size):
        #Getting 8 characters for each row and changing into upper-case
        sub_key = key[8*i:8*i+8].upper()
        temp = []
        #iterating on 4 columns for each row
        for j in range(4):
            #Making each cell of 2 characters or 1 byte(8 bits)
            temp.append(sub_key[j*2:j*2+2])
        mat.append(temp)
    return mat

#Function to rotate matrix for key generation
def rotateWord(mat):
    #Last row of matrix is selected
    rotate_list = mat[len(mat)-1]
    #Left rotate is applied on last row
    rotate_list = rotate_list[1:]+rotate_list[:1]
    return rotate_list

#Function to apply sbox on last row
def subWord(sub_list):
    for i in range(len(sub_list)):
        #Value of each cell of last row is passed to SBox and corresponding value is stored back in cell
        sub_list[i] = SBox[sub_list[i][0]][sub_list[i][1]]
    return sub_list

#Function to apply inverse sbox on last row
def IsubWord(sub_list):
    for i in range(len(sub_list)):
        #Value of each cell of last row is passed to inverse SBox and corresponding value is stored back in cell
        sub_list[i] = ISBox[sub_list[i][0]][sub_list[i][1]]
    return sub_list

#Function to apply XOR on two rows
def XOR(v1,v2):
    #Both row cells are converted from Hex to Binary
    mat1 = Hex2Bin(v1)
    mat2 = Hex2Bin(v2)
    #Empty Answer list is created
    ans = []
    #Loop to iterate for each cell in row
    for i in range(len(mat1)):
        #Each cell is XORed using Function
        ans.append(XORtwoNums(mat1[i],mat2[i]))
    #Answer list is returned after converting it back to Hex
    return Bin2Hex(ans)

#Function to XOR two matrices
def XORMatrix(mat1,mat2):
    mat3 = []
    #Loop iterated on each row
    for i in range(len(mat1)):
        #XOR function applies operation on one row at a time
        mat3.append(XOR(mat1[i],mat2[i]))
    return mat3

#Function to Apply SBox on whole matrix
def subMat(mat):
    res = []
    #Loop iterated on each row
    for i in range(len(mat)):
        #Answer returned from Row Sbox operation function is stored
        res.append(subWord(mat[i]))
    return res

#Function to Apply SBox on whole matrix
def IsubMat(mat):
    res = []
    #Loop iterated on each row
    for i in range(len(mat)):
        #Answer returned from Row Sbox operation function is stored
        res.append(IsubWord(mat[i]))
    return res

#Function to apply Shift rows left on matrix
def shiftMat(mat):
    #Loop iterated to apply shifting on each row
    for i in range(len(mat)):
        #Matrix is passed to shiftRow function with row that is to be shifted and number of times it needs to be shifted
        mat = shiftRow(mat,i,i)
    return mat

#Function to apply Shift rows left on matrix
def IshiftMat(mat):
    #Loop iterated to apply shifting on each row
    for i in range(len(mat)):
        #Matrix is passed to IshiftRow function with row num that is to be shifted and number of times it needs to be shifted
        mat = IshiftRow(mat,i,i)
    return mat

#Recursive Function to apply left shift on matrix row with given row number and the number of shifts
def shiftRow(mat,row,round):
    if round == 0:
        return mat
    temp = mat[0][row]
    mat[0][row] = mat[1][row]
    mat[1][row] = mat[2][row]
    mat[2][row] = mat[3][row]
    mat[3][row] = temp
    return shiftRow(mat,row,round-1)

#Recursive Function to apply right shift on matrix row with given row number and the number of shifts
def IshiftRow(mat,row,round):
    if round == 0:
        return mat
    temp = mat[3][row]
    mat[3][row] = mat[2][row]
    mat[2][row] = mat[1][row]
    mat[1][row] = mat[0][row]
    mat[0][row] = temp
    return IshiftRow(mat,row,round-1)

#Function to convert a row from Hex to Binary
def Hex2Bin(word):
    mat=[]
    for i in range(len(word)):
        mat.append(Hex2BinNum(word[i]))
    return mat

#Function to convert a row from Binary to Hex
def Bin2Hex(word):
    mat=[]
    for i in range(len(word)):
        mat.append(Bin2HexNum(word[i]))
    return mat

#Function to apply XOR on key matrix with each answer added to next row of key 
def keyExpandXOR(key,v2):
    ans = []
    #Iteration on rows of key
    for i in range(len(key)):
        #v1 stores current row
        v1 = key[i]
        #If 5th row and 256 bit AES then additional SBox is applied to answer of last row
        if i == 4 and len(key) == 8:
            v2 = subWord(copy.deepcopy(v2))
        #XOR operation applied on 2 lists(rows)
        temp = XOR(v1,v2)
        ans.append(temp)
        #Answer stored in v2 to be XORed with next row in key matrix
        v2 = temp
    return ans

#Function to rearrange keys from 6x4 and 8x4 to 4x4 form incase of AES-192 and AES-256
def rearrange(key_list,mode,key0):
    new_key_list = []
    #List of keys is flattened in single list
    flat_list = [key for keys in key_list for key in keys]
    #Key0 is appended at start
    flat_list = key0+flat_list
    #First 16 bytes are discarded as they are not needed in n round keys
    flat_list = flat_list[4:]

    #Loop iterated 12 or 14 times depending on AES type
    for i in range(int(mode/32)+6):
        #new list gets and stores 16 bytes(128 bits) at each index
        new_key_list.append(flat_list[0:4])
        #these 16 bytes are discarded from total list
        flat_list = flat_list[4:]
    return new_key_list

#Function to Read Plaintext or Ciphertext from given file path
def readText(filepath):
    f = open(filepath,'r')
    str = f.readlines()
    #Newline(if any) is removed from each block
    str = [str[i].strip().upper() for i in range(len(str))]
    f.close()
    return str

#Function to convert a number from hex to binary
def Hex2BinNum(num):
    ans = hex_bin_dict[num[0]]+hex_bin_dict[num[1]]
    return ans

#Function to convert a number from binary to hex
def Bin2HexNum(num):
    keys = list(hex_bin_dict.keys())
    values = list(hex_bin_dict.values())
    ans = keys[values.index(num[:4])]+keys[values.index(num[4:])]
    return ans

#Function to multiply two numbers
def mult(v1,v2):
    #Both numbers are converted to binary
    bin_v1 = Hex2BinNum(v1)
    bin_v2 = Hex2BinNum(v2)
    ans = Hex2BinNum('00')
    #Loop to iterate on each bit of mix column value
    for i in range(len(bin_v2)):
        #If bit is one then position(n) of bit is checked and left shift is applied on v1 n times
        if bin_v2[i] == '1':
            #After left shift returned answer is added to answer string each time
            ans = XORtwoNums(ans,leftShift(bin_v1,len(bin_v2)-1-i))
    return Bin2HexNum(ans)

#Function to apply XOR operation on two numbers
def XORtwoNums(v1,v2):
    ans = ''
    #Loop iterated on each bit
    for i in range(len(v1)):
        #If to apply XOR operation on each bit and decide the resultant value, which is appended to temp
        if (v1[i] == '1' and v2[i] == '0') or (v1[i] == '0' and v2[i] == '1'):
            ans+='1'
        else:
            ans+='0'
    return ans

#Left Shift is applied n number of times on a binary number
def leftShift(bin_v1,num):
    #Irreducible polynomial
    irreducible = '00011011'

    #Loop iterated for num shifts
    for i in range(num):
        temp = bin_v1[0]
        bin_v1 = bin_v1[1:]+'0'
        #After each shift if '1' is overflowed then irreducible is XORed with resultant
        if temp == '1':
            bin_v1 = XORtwoNums(bin_v1,irreducible)
    return bin_v1

#Function to apply mix column multiplication
def mixColMult(mat1):
    #resultant matrix
    result=[['00','00','00','00'],['00','00','00','00'],['00','00','00','00'],['00','00','00','00']]
    #iterate through rows
    for i in range(len(mat1)):
        #iterate through columns
        for j in range(len(mat1)):
            #iterate through rows
            for k in range(len(mat1)):
                #Row of matrix is multiplied with column of mix column matrix and stored in resultant[i][j]
                result[i][j] = Bin2HexNum(XORtwoNums(Hex2BinNum(result[i][j]),Hex2BinNum(mult(mat1[i][k],MixColumn[k][j]))))
    return result

#Function to apply inverse mix column multiplication
def ImixColMult(mat1):
    #resultant matrix
    result=[['00','00','00','00'],['00','00','00','00'],['00','00','00','00'],['00','00','00','00']]
    #iterate through rows
    for i in range(len(mat1)):
        #iterate through columns
        for j in range(len(mat1)):
            #iterate through rows
            for k in range(len(mat1)):
                #Row of matrix is multiplied with column of inverse mix column matrix and stored in resultant[i][j]
                result[i][j] = Bin2HexNum(XORtwoNums(Hex2BinNum(result[i][j]),Hex2BinNum(mult(mat1[i][k],IMixColumn[k][j]))))
    return result

#Function to write plaintext or ciphertext to file given filepath
def writeText(text,filepath):
    f = open(filepath,'w')
    for i in range(len(text)):
        temp = ''
        for j in range(len(text[i])):
            for k in range(len(text[i][j])):
                temp+=text[i][j][k]
        f.write(temp)
        if i != len(text)-1:
            f.write('\n')
    f.close()

#Function to generate random 16 bytes(128 bit) IV in case of CBC mode
def generateIV():
    ans=''
    for i in range(16):
        temp=''
        for j in range(8):
            temp+=str(random.randint(0,1))
        ans += Bin2HexNum(temp)
    return ans

#Function to check and apply padding on left of each block if block size is less than 16 bytes(128 bits)
def checkPadding(plain):
    for i in range(len(plain)):
        temp = "0" * (32-len(plain[i]))
        plain[i] = temp + plain[i]
    return plain
