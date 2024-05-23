# Object

#!/usr/bin/env python3
import os
import sys
import numpy as np

def getNeigAmount(currentMatrix):
    # TODO:
    return True

def moveToNextGen(neigMatrix):
    # TODO:
    return True

def printMatrix(matrix):
    """Prints a NumPy matrix with integer formatting."""
    if matrix.dtype != np.int:
        matrix = matrix.astype(int)  # Convert to integer if not already # TODO: WHAT HAPPEN IF YOU CANNOT CONVERT IT TO INT
    # Create a string representation with formatted output
    formatted = '\n'.join(['\t'.join(map(str, row)) for row in matrix])
    print(formatted)

# def checkIfChanged(currentMatrix, nextGenMatrix):
#     # TODO:

def main():
    # Create the matrix
    matrix = np.array([
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
])
    # Send to eval
    # Move to next Gen
    # Print result

if __name__ == "__main__":
    main()
