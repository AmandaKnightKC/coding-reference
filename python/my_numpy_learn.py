import numpy as np

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)  # Convrt list to NumPy array

second_list = [6, 7, 8, 9, 10]
# Convert second list to NumPy array
two_d_array = np.array([my_array, second_list])
print(two_d_array)  # Output: [[1 2 3 4 5] [6 7 8 9 10]]
# what kind of Python object is this? what class or structure. Output: <class 'numpy.ndarray'>
print(type(two_d_array))

print(two_d_array.shape)
print(two_d_array.size)
print(two_d_array.dtype)  # data types of the elements inside the array.
# Output: int64 (or int32 depending on the platform) common values: int64, float64, complex128, bool, object, str, datetime64, timedelta64
print(two_d_array.ndim)  # number of dimensions of the array. Output:

np.identity(n=5)     # platform   )
eye = np.eye(N=3, M=4, k=1, dtype=float)  # Create an identity matrix

np.ones(shape=(2, 3), dtype=int)  # Create an array of ones
np.zeros(shape=(2, 3), dtype=float)  # Create an array of zeros
# Create an array filled with a specific value
np.full(shape=(2, 3), fill_value=7, dtype=int)
np.arange(start=0, stop=10, step=2)  # Create an array with a range of values
# Create an array with evenly spaced values
np.linspace(start=0, stop=1, num=5)
np.random.rand(2, 3)  # Create an array with random values
# Create an array with random values from a normal distribution
np.random.randn(2, 3)
# Create an array with random integers
np.random.randint(low=0, high=10, size=(2, 3))
# Create an array with random choices from a list
np.random.choice(a=[1, 2, 3, 4, 5], size=(2, 3), replace=True)
np.random.seed(42)  # Set a random seed for reproducibility
random_array = np.random.rand(2, 3)  # Create a random array
print(random_array)

# array slicing and indexing
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_slice = array[2]  # Get the third row of the array
print(array_slice)  # Output: [7 8 9]
small_array = np.array([1, 2, 3, 4])
# Get a sub-array from the first two rows and columns 1 to 2
print(small_array[1])
