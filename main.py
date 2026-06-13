import cv2
import numpy as np
import scipy as sy

import sys

from utils import *


def main():

    automated = len(sys.argv) > 1 and sys.argv[1] == "-a"

    print("Hello from assignment-1!")

    pause(automated)


if __name__ == "__main__":
    main()
