import numpy as np
import array

class myArray(array.array):
    arraymem1 = np.array([1,2,3])
    arraymem2 = np.array([5,8,6])

    def addition(self):
        result = self.arraymem1 +self.arraymem2
        return result

    def subtraction(self):
        result = self.arraymem1 - self.arraymem2
        return result

    def multiplication(self):
        result = self.arraymem1 * self.arraymem2
        return result


arrayObj = myArray('u')
arrayObj.arraymem1 = np.array([[1,5,9],[8,7,3]])
arrayObj.arraymem2 = np.array([[3,1,7],[5,2,4]])
print("The array after addition: \n", arrayObj.addition())
print("The array after subtraction: \n",arrayObj.subtraction())
print("The array after multiplication: \n",arrayObj.multiplication()) 