import time
import numpy as np
import subprocess

"""
    Print each element in the provided list with a 1-second interval between prints.

    Parameters
    ----------
    lst : list
        The list of items to print sequentially.
    """

def print_element(lst):
    for item in lst:
        print(item)
        time.sleep(1)

"""
    Split a 3D numpy array (cube-shaped) into 8 equally sized chunks by halving each axis,
    and return the average of each chunk.

    Parameters
    ----------
    arr : numpy.ndarray
        A 3-dimensional, cube-shaped array with even-length sides.

    Returns
    -------
    numpy.ndarray
        A 1D array of length 8 containing the mean of each chunk, in the order
        determined by iterating over the first, second, then third axis halves.

    Raises
    ------
    ValueError
        If `arr` is not 3D, not cube-shaped, or has odd dimensions.
    """
def cube_avg(arr: np.ndarray) -> np.ndarray:
    if arr.ndim != 3:
        raise ValueError("Input must be 3D")
    x, y, z = arr.shape
    if x != y or y != z:
        raise ValueError("Input must be cube‐shaped")
    if x % 2 != 0:
        raise ValueError("Cube dimensions must be an even number")

    half = x // 2
    means = []
    for i in (0, half):
        for j in (0, half):
            for k in (0, half):
                sub = arr[i:i+half, j:j+half, k:k+half]
                means.append(sub.mean())
    return np.array(means)