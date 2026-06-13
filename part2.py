import cv2
import numpy as np
import scipy as sy


# UTILS
# This section contains helper functions for the main function calls that are called from main.py

def print_channel_statistics(channel) -> None:

    # min
    print("min:\t\t\t" + str(np.amin(channel)))

    # max
    print("max:\t\t\t" + str(np.amax(channel)))

    # average/mean
    print("average:\t\t" + str(np.average(channel)))

    # median
    print("median:\t\t\t" + str(np.median(channel)))

    # mode
    print("mode:\t\t\t" + str(sy.stats.mode(channel).mode))

    # skew
    print("skew:\t\t\t" + str(sy.stats.skew(channel)))

    # range
    print("range:\t\t\t" + str(np.ptp(channel)))

    # standard deviation
    print("standard deviation:\t" + str(np.std(channel)))

    # variance
    print("variance:\t\t" + str(np.var(channel)))

    print("\n")

# MAIN FUNCTIONS
# These are the top level functions called from main.py


def print_statistics(image_path: str) -> None:
    image = cv2.imread(image_path)

    # split into color channels
    # the order is blue, gree, red, rather than RGB. Whyyyyyy
    b,g,r = cv2.split(image)

    print("Red Channel Statistics:")
    print_channel_statistics(r)

    print("Blue Channel Statistics:")
    print_channel_statistics(b)

    print("Green Channel Statistics:")
    print_channel_statistics(g)
