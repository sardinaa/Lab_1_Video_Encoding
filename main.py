# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code. Press Double
# Shift to search everywhere for classes, files, tool windows, actions,
# and settings.
from rgb_yuv import RGB2YUV, YUV2RGB
from run_length import run_length_encoding, run_length_decoding
import DCT_coding
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # 1) Start a script called rgb_yuv.py and create a
    # translator from 3 values in RGB into the 3 YUV
    # values, plus the opposite operation.
    imgs = np.random.randint(0, 256, size=(100, 100, 3))
    yuv = RGB2YUV(imgs)
    rgb = YUV2RGB(yuv)
    print("Original RGB values: " + str(
        imgs[0, 0, :]) + " Values in YUV space: " + str(
        yuv[0, 0, :]) + " Back to RGB: " + str(rgb[0, 0, :]))

    str_array = np.array(['A', 'A', 'B', 'C', 'C', 'C', 'C', 'C'])
    compressed_coding = run_length_encoding(str_array)
    print("Message to encode: ", str_array[:])
    print("Encoded message: ", compressed_coding)
    print("Decoded message: ", run_length_decoding(compressed_coding))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
