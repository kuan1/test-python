import numpy as np
import numpy

# Creating int numpy arrays
python_list = [1,2,3,4,5]
print('Type: ', type(python_list))
print(python_list)

two_dimensional_list = [[0,1,2],[3,4,5],[6,7,8]]
print(two_dimensional_list)

numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))
print(numpy_array_from_list)

# Creating float numpy arrays
python_list = [1,2,3,4,5]
numpy_array_from_list2 = np.array(python_list, dtype=float)
print(numpy_array_from_list2)

# Creating boolean numpy arrays
numpy_bool_array = np.array([0,1,-1,0,0], dtype=bool)
print(numpy_bool_array)

# Creating multidimensional array using numpy

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

# 下边不学了...