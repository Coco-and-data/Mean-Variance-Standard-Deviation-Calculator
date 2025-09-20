from mean_var_std import calculate
import json

print("Testing with [0,1,2,3,4,5,6,7,8]:")
result = calculate([0,1,2,3,4,5,6,7,8])
print(json.dumps(result, indent=2))

print("\n" + "="*50 + "\n")

print("Testing with [1,2,3,4,5,6,7,8,9]:")
result2 = calculate([1,2,3,4,5,6,7,8,9])
print(json.dumps(result2, indent=2))

print("\n" + "="*50 + "\n")

print("Testing with list of 8 elements (should give error):")
try:
    calculate([1,2,3,4,5,6,7,8])
except ValueError as e:
    print(f"Error caught correctly: {e}")

print("\n" + "="*50 + "\n")

import numpy as np
print("Visualization of 3x3 matrix from first example:")
matrix = np.array([0,1,2,3,4,5,6,7,8]).reshape(3, 3)
print("List: [0,1,2,3,4,5,6,7,8]")
print("3x3 Matrix:")
print(matrix)
print("\nRows (axis=1):")
for i, row in enumerate(matrix):
    print(f"  Row {i}: {row}")
print("\nColumns (axis=0):")
for i in range(3):
    print(f"  Column {i}: {matrix[:, i]}")
