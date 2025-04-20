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