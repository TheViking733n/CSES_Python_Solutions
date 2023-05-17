import zlib
import array
from Grid_Paths_data import data

data2 = []

byte_array = array.array('Q', data).tobytes()

# Compress the data using zlib
compressed_data = zlib.compress(byte_array, level=-1)

# Print the compressed data
from pyperclip import copy
copy(str(compressed_data))
