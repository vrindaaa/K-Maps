# CSE 101 - IP HW2
# K-Map Minimization 
# Name: Vrinda Narayan
# Roll Number: 2018120
# Section: A
# Group: 8
# Date: 16/10/2018

import unittest
from HW2_2018120 import minFunc

#as in question it is given that we don't have to check for invalid input hence my test file and main function will not cover those cases

class testpoint(unittest.TestCase):
	def test_minFunc(self):
                #boundary cases
                self.assertEqual(minFunc(4,'() d -'),0)
                self.assertEqual(minFunc(2,'(0,1,2,3) d -'), 1)
                self.assertEqual(minFunc(3,'() d (0,1,2)'), 0)
                self.assertEqual(minFunc(4,'() d (7,3,5)'), 0)
                self.assertEqual(minFunc(3,'() d (0,1,2)'), 0)
                self.assertEqual(minFunc(4,'(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15) d -'), 1)
                #test cases
                self.assertEqual(minFunc(4,'(0) d (1,2,3)'),"w'x'")
                self.assertEqual(minFunc(4,'(0,1,2,4,5,6,8,9,12,13,14) d -'), "w'z'+xz'+y'")
                #two possible results 
                self.assertIn(minFunc(4,'(1,3,7,11,15) d (0,2,5)'), ["yz+w'x'","w'z+yz"], msg=None)
                #two pi
                self.assertEqual(minFunc(4,'(0,1,4) d -'),"w'x'y'+w'y'z'")
                self.assertEqual(minFunc(4,'(0,1,3,4,5,7) d (15)'),"w'y'+w'z")
                #with three variables
                self.assertEqual(minFunc(3,'(0,1,2) d (3)'),"w'")
                self.assertEqual(minFunc(4,'(0,4,8,12) d (2,6,10,14)'),"z'")
                #one element in each corner
                self.assertEqual(minFunc(4,'(0,2,8,10) d -'),"x'z'")
                self.assertEqual(minFunc(4,'(1,3,9) d (11)'),"x'z")
                #when dont care is not included
                self.assertEqual(minFunc(4,'(1,3) d (15)'),"w'x'z")
                self.assertEqual(minFunc(4,'(5,10) d (15)'),"w'xy'z+wx'yz'")
                #kmap as a checkboard
                self.assertEqual(minFunc(4,'(0,3,5,6,9,10,12) d (15)'),"w'x'y'z'+w'x'yz+w'xy'z+w'xyz'+wx'y'z+wx'yz'+wxy'z'")
                #less than 4 variable
                self.assertEqual(minFunc(3,'(0,2,4,6) d -'),"y'")
                #when number of variables is 2
                self.assertEqual(minFunc(2,'(0,1,3) d -'),"w'+x")
                self.assertEqual(minFunc(2,'(0) d -'),"w'x'")
                self.assertEqual(minFunc(2,'() d (0,1)'),0)
                self.assertEqual(minFunc(2,'(0,2) d -'),"x'")

		
                
if __name__=='__main__':
	unittest.main()
