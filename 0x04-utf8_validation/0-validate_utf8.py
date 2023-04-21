#!/usr/bin/python3
"""
    objectives:
        Prototype: def validUTF8(data)
    1-  if data is a valid UTF-8 encoding
            return True
        else
            return False
    2-  A character in UTF-8 can be 1 to 4 bytes long
    3-  The data set can contain multiple characters
    4-  The data will be represented by a list of integers
    5-  Each integer represents 1 byte of data, therefore you only
        need to handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """
        determines if a given data set represents a valid UTF-8 encoding
    """
    if data is None:
        return False

    for i in data:
        if i < 0 or i > 255:
            return False

    N_Bytes = 0

    for num in data:
        '''
            convert to binary get the last 8 bits
            and check if the first bit is 0
        '''
        Binary_rep = format(num, '#010b')[-8:]

        if N_Bytes == 0:

            for bit in Binary_rep:

                if bit == '0':
                    break

                N_Bytes += 1

            if N_Bytes == 0:
                continue

            if N_Bytes == 1 or N_Bytes > 4:
                return False

        else:

            '''
                check if the first bit is 1 and the second bit is 0
            '''
            if not (Binary_rep[0] == '1' and Binary_rep[1] == '0'):
                return False

        N_Bytes -= 1
    return True if N_Bytes == 0 else False
