'''
given a string with binary numbers return the value of addition of those 2 numbers
'''

def addBinary(self, a, b):
        sum = bin(int(a,2)+int(b,2))
        return sum[2:]
