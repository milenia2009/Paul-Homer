import pandas as pd
import numpy as np


# Numpy Examples

import numpy as np

Nump_Array = np.array([[1,2,3],[4,5,6]])

print(Nump_Array)

Nump_Array+=2

print(Nump_Array)


#declare list of values
list_of_strings = ["5","6","7","8","9", "10"]

#declare empty list to store converted values
result = []

#'not memory effiecent'
for string in list_of_strings:
    result.append(int(string))
    
print(result)

#'memory efficent' can change first param to int, str, float
result = map(float,list_of_strings)

print(list(result))