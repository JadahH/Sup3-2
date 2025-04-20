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


def cube_avg():
    pass