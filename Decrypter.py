#Martin Skachkov
#Decrypting Software For B.E.D.S.

def decrypter(input0, input1, binary):
    """This function takes 3 inputs, first two being the cipher and the last
    being the encrypted message, first its turns the excrypted message to binary
    via the cipher. After that it takes the binary and turns it into text.
    """
    binary = binary.replace(input0,"0")#Replaces any reference of input0 with 0
    binary = binary.replace(input1,"1")#Replaces any reference of input1 with 1
    individual = binary.split() #Splits binary into list of words
    str_final= ' ' #final output
    str_data = ' ' #Intermediate Output step
    #Converts Binary to ASCII
    for i in individual:
        for b in range(0, len(i), 7):
            temp_data = int(i[b:b + 7])
            decimal_data = BinaryToDecimal(temp_data)
            str_data = str_data + chr(decimal_data)
        str_final= str_final+str_data
        str_data = ' '
    return str_final
# Defining BinarytoDecimal() function
def BinaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return (decimal)
#Encrypting Function
def encrypter(input0, input1, text):
    textList = text.split( )
    finalText = ""
    for word in textList:
        binWord = str(''.join(format(ord(i), 'b') for i in word))
        finalText += binWord + " "
    finalText = finalText.replace("0", input0)
    finalText = finalText.replace("1", input1)
    return finalText
