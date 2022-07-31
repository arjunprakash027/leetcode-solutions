"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""


def plusOne(self, digits):
        str1 = ""
        for i in digits: #goes through all digits
            str1 = str1 + str(i) #converts the digits into strings
        value = int(str1) + 1 #convert string into int and adds 1 to it
        str1 = str(value) #converts the added value back to string
        lis = [int(d) for d in str(str1)] #converts the string into int and appends it to the list
        return lis #return the answer