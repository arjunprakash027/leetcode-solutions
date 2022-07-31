def plusOne(self, digits):
        str1 = ""
        for i in digits:
            str1 = str1 + str(i)
        value = int(str1) + 1
        str1 = str(value)
        lis = [int(d) for d in str(str1)]
        return lis