# ======================================================================================================================
# 2023-2024 California State University San Marcos Capstone Project: Ai Art Generation, version 0.1
# Authors: Josh Vande Berg, Bryce Tuller, Abraham Rosales
# ======================================================================================================================

# AUTHORS NOTE: Pycharm installed packages should be: Pillow, pip, setuptools, wheel, pytest

# ** Import statements **
from urllib.request import urlopen

import tkinter
from tkinter import *
from tkinter import ttk

import PIL
from PIL import ImageTk, Image, ImageDraw

import random
from TestInterface import TestInterface

if __name__ == '__main__':
    tkRoot = Tk()
    tkRoot.geometry("1400x700")
    tkRoot.title("DemoMondrian")
    tkRoot.configure(background='LightGrey')
    aiArtGui = TestInterface(tkRoot)
    tkRoot.mainloop()
