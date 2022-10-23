#Import function here

def testFunction(var1,var2,var3):
    return((var1 + var2)*var3)
#print(testFunction(1,2.0,'3'))


import unittest
class InputTest(unittest.TestCase):
    def testBool(self):
        result1 = testFunction(False)
        result2 = testFunction(True)
        result3 = testFunction(False,False)

        #Test boolean inputs
    def testIntegers(self):
        #Test if the
        #Test the range of integers that can be put in (While Loop?)

