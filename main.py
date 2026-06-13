import cv2
import numpy as np
import scipy as sy

import sys

import utils
import part2

ORIGINAL_IMAGE = "HW1_IMG_CS898BA.png"


def main():

    automated = len(sys.argv) > 1 and sys.argv[1] == "-a"

    print("Processing statistics on the original image:\n")

    part2.print_statistics(ORIGINAL_IMAGE)

    print("Processing Complete")
    
    utils.pause(automated)


if __name__ == "__main__":
    main()
