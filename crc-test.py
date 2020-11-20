import hashlib

def xor(a, b):

    result = []

    # Traverse all bits, if bits are
    # same, then XOR is 0, else 1
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


def mod2div(dividend, divisor):
    # Number of bits to be XORed at a time.
    pick = len(divisor)

    # Slicing the divident to appropriate
    # length for particular step
    tmp = dividend[0: pick]

    while pick < len(dividend):

        if tmp[0] == '1':

            # replace the divident by the result
            # of XOR and pull 1 bit down
            tmp = xor(divisor, tmp) + dividend[pick]

        else:  # If leftmost bit is '0'

            # If the leftmost bit of the dividend (or the
            # part used in each step) is 0, the step cannot
            # use the regular divisor; we need to use an
            # all-0s divisor.
            tmp = xor('0' * pick, tmp) + dividend[pick]

        # increment pick to move further
        pick += 1

    # For the last n bits, we have to carry it out
    # normally as increased value of pick will cause
    # Index Out of Bounds.
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    checkword = tmp
    return checkword


# Function used at the sender side to encode
# data by appending remainder of modular division
# at the end of data.
def encodeData(data, key):
    l_key = len(key)

    # Appends n-1 zeroes at end of data
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)

    # Append remainder in the original data
    codeword = data + remainder
    return codeword

def decodeData(code, key):
    remainder = mod2div(code, key)
    return remainder




data=input("Enter Data: ")
print("dataword:"+str(data))

key = "10001000000100001"
print("generating polynomial:"+key)
codeword = encodeData(data, key)
print("Checksum: ",codeword)
print("Transmitted Codeword:"+str(codeword))
code = input("enter transmitted codeword:")

recieved_data = int(decodeData(code, key))

if recieved_data == 0:
    print("NO ERROR! SUCCESSFUL TRANSMISSION")
else:
    print("ERROR HAS OCCURRED")
print(recieved_data)

