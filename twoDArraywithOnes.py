import numpy as np
A = np.array([[5,9,0], [4,7,2], [5,1,9]])
B = np.ones([3,3], dtype=int)

add = A + B
print("The addition of two matrices is: \n",add)

multiplication = A * B
print("The multiplication of two matrices is: \n",multiplication)

