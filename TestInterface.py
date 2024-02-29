from urllib.request import urlopen

import tkinter
from tkinter import *
from tkinter import ttk

import PIL
from PIL import ImageTk, Image, ImageDraw

import random
import os


class TestInterface(tkinter.Frame):

    # **** WINDOW ****
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.img = None
        self.parent = parent

        self.overallSettingsLabel = Label(self.master, text="Image settings:")

        self.imageText = Label(self.master, text="Image result:")

        # ** aspect ratio parameters **
        self.aspect_x = 700  # variable defining scale of generated image from left to right, 700px by default
        self.aspect_y = 400  # variable defining scale of generated image from top to bottom, 400px by default

        self.aspectLabel = Label(self.master, text="Aspect Ratio Selection:")
        self.aspect3_2Button = Button(self.master, text="3:2", command=lambda: self.set_aspect(900, 600))
        self.aspect6_4Button = Button(self.master, text="6:4", command=lambda: self.set_aspect(1800, 1200))
        self.aspect7_5Button = Button(self.master, text="7:5", command=lambda: self.set_aspect(2100, 1500))
        self.aspect2_3Button = Button(self.master, text="2:3", command=lambda: self.set_aspect(600, 900))
        self.aspect4_6Button = Button(self.master, text="4:6", command=lambda: self.set_aspect(1200, 1800))
        self.aspect5_7Button = Button(self.master, text="5:7", command=lambda: self.set_aspect(900, 600))
        self.aspectDefaultButton = Button(self.master, text="Default", command=lambda: self.set_aspect(700, 400))

        self.imagePresent = Label(self.master)

        self.parameterSliderText = Label(self.master, text="Parameter Configuration:")

        # *** Horizontal Lines ***
        self.h_line = tkinter.IntVar()  # variable defining number of horizontal lines
        self.hLineSliderText = Label(self.master, text="Number of horizontal lines:")

        self.hLineDisplay = ttk.Scale(self.master, from_=0, to=10, orient='horizontal', variable=self.h_line,
                                      command=self.h_line_changed)
        self.hLineSliderReading = Label(self.master, text=self.h_line_get())
        # *** Horizontal Lines ***

        # *** Vertical Lines ***
        self.v_line = tkinter.IntVar()  # variable defining number of vertical lines
        self.vLineSliderText = Label(self.master, text="Number of vertical lines:")

        self.vLineDisplay = ttk.Scale(self.master, from_=0, to=15, orient='horizontal', variable=self.v_line,
                                      command=self.v_line_changed)
        self.vLineSliderReading = Label(self.master, text=self.v_line_get())
        # *** Vertical Lines ***

        # *** Color Distribution ***
        self.color_dist = tkinter.IntVar()
        self.cdSliderText = Label(self.master, text="Color Distribution:")

        self.cdDisplay = ttk.Scale(self.master, from_=1, to=10, orient='horizontal', variable=self.color_dist,
                                   command=self.cd_changed)
        self.cdSliderReading = Label(self.master, text=self.cd_get())
        # *** Color Distribution ***

        # ***Line Thickness ***
        self.line_thickness = tkinter.IntVar()
        self.ltSliderText = Label(self.master, text="Line Thickness:")

        self.ltDisplay = ttk.Scale(self.master, from_=1, to=5, orient='horizontal', variable=self.line_thickness,
                                   command=self.lt_changed)
        self.ltSliderReading = Label(self.master, text=self.lt_get())
        # ***Line Thickness ***

        # ***Line Spacing ***
        self.line_spacing = tkinter.IntVar()
        self.lsSliderText = Label(self.master, text="Minimum Line Spacing:")

        self.lsDisplay = ttk.Scale(self.master, from_=15, to=20, orient='horizontal', variable=self.line_spacing,
                                   command=self.ls_changed)
        self.lsSliderReading = Label(self.master, text=self.ls_get())
        # ***Line Spacing ***

        # *** Horizontal Rectangle Split Chance ***
        self.hrsc = tkinter.IntVar()
        self.hrscSliderText = Label(self.master, text="Horizontal Rectangle Split Chance (%):")

        self.hrscDisplay = ttk.Scale(self.master, from_=0, to=100, orient='horizontal', variable=self.hrsc,
                                     command=self.hrsc_changed)
        self.hrscSliderReading = Label(self.master, text=self.hrsc_get())
        # *** Horizontal Rectangle Split Chance ***

        # *** Vertical Rectangle Split Chance ***
        self.vrsc = tkinter.IntVar()
        self.vrscSliderText = Label(self.master, text="Vertical Rectangle Split Chance (%):")

        self.vrscDisplay = ttk.Scale(self.master, from_=0, to=100, orient='horizontal', variable=self.vrsc,
                                     command=self.vrsc_changed)
        self.vrscSliderReading = Label(self.master, text=self.vrsc_get())
        # *** Vertical Rectangle Split Chance ***

        # *** Neighboring Color Chance ***
        self.ncc = tkinter.IntVar()
        self.nccSliderText = Label(self.master, text="Neighboring Color Chance (%):")

        self.nccDisplay = ttk.Scale(self.master, from_=0, to=100, orient='horizontal', variable=self.ncc,
                                    command=self.ncc_changed)
        self.nccSliderReading = Label(self.master, text=self.ncc_get())
        # *** Neighboring Color Chance ***

        # *** White Rectangle Chance ***
        self.wrc = tkinter.IntVar()
        self.wrcSliderText = Label(self.master, text="White Rectangle Chance (%):")

        self.wrcDisplay = ttk.Scale(self.master, from_=0, to=100, orient='horizontal', variable=self.wrc,
                                    command=self.wrc_changed)
        self.wrcSliderReading = Label(self.master, text=self.wrc_get())
        # *** White Rectangle Chance ***

        self.new_image = PIL.Image.new("RGB", (self.aspect_x, self.aspect_y), color=(255, 255, 255))
        self.photoImageNewImage = ImageTk.PhotoImage(self.new_image)
        self.imageTest = Label(self.master, image=self.photoImageNewImage)

        self.generateButton = Button(self.master, text="Generate", command=self.generate_image)

        self.resetButton = Button(self.master, text="Reset Image", command=self.no_image_image)

        self.randomButton = Button(self.master, text="Random", command=self.random_gen)

        self.default_url_image()  # present default image on startup

        self.aspectPresent = Label(self.master)

        self.update_ratio()

        self.imagePresent = Label(self.master)

        self.make_interface()

    # **** WINDOW ****

    def make_interface(self):
        # **** DEFAULTS ****
        # ** text above overall image settings **
        self.overallSettingsLabel.configure(background='LightGrey')
        self.overallSettingsLabel.grid(row=0, column=0, padx=20, pady=(20, 0), sticky=W)

        # ** text above generated image **
        self.imageText.configure(background='LightGrey')
        self.imageText.grid(row=0, column=1, padx=20, pady=(20, 0), sticky=W)

        self.aspectLabel.configure(background='LightGrey')
        self.aspectLabel.grid(row=1, column=0, padx=20, pady=(0, 0), sticky=NW)

        # ** 3:2 ratio **
        self.aspect3_2Button.grid(row=1, column=0, padx=23, pady=(20, 0), sticky=NW)

        # ** 6:4 ratio **
        self.aspect6_4Button.grid(row=1, column=0, padx=53, pady=(20, 0), sticky=NW)

        # ** 7:5 ratio **
        self.aspect7_5Button.grid(row=1, column=0, padx=83, pady=(20, 0), sticky=NW)

        # ** 2:3 ratio **
        self.aspect2_3Button.grid(row=1, column=0, padx=23, pady=(50, 0), sticky=NW)

        # ** 4:6 ratio **
        self.aspect4_6Button.grid(row=1, column=0, padx=53, pady=(50, 0), sticky=NW)

        # ** 5:7 ratio **
        self.aspect5_7Button.grid(row=1, column=0, padx=83, pady=(50, 0), sticky=NW)

        # ** default ratio **
        self.aspectDefaultButton.grid(row=1, column=0, padx=40, pady=(80, 0), sticky=NW)

        # **** PARAMETERS ****
        # ** text above all parameters *
        self.parameterSliderText.configure(background='LightGrey')
        self.parameterSliderText.grid(row=0, column=2, padx=0, pady=(20, 0), sticky=W)

        # *** Horizontal Lines ***
        self.hLineSliderText.configure(background='LightGrey')
        self.hLineSliderText.grid(row=1, column=2, padx=0, pady=(0, 0), sticky=NW)

        self.hLineDisplay.grid(row=1, column=2, padx=3, pady=(20, 0), sticky=NW)

        self.hLineSliderReading.configure(background='LightGrey')
        self.hLineSliderReading.grid(row=1, column=2, padx=110, pady=(23, 0), sticky=NW)

        self.hLineDisplay.set(10)
        # *** Horizontal Lines ***

        # *** Vertical Lines ***
        self.vLineSliderText.configure(background='LightGrey')
        self.vLineSliderText.grid(row=1, column=2, padx=0, pady=(50, 0), sticky=NW)

        self.vLineDisplay.grid(row=1, column=2, padx=3, pady=(70, 0), sticky=NW)

        self.vLineSliderReading.configure(background='LightGrey')
        self.vLineSliderReading.grid(row=1, column=2, padx=110, pady=(73, 0), sticky=NW)

        self.vLineDisplay.set(10)
        # *** Vertical Lines ***

        # ** Color Distribution **
        self.cdSliderText.configure(background='LightGrey')
        self.cdSliderText.grid(row=1, column=2, padx=0, pady=(100, 0), sticky=NW)

        self.cdDisplay.grid(row=1, column=2, padx=3, pady=(120, 0), sticky=NW)

        self.cdSliderReading.configure(background='LightGrey')
        self.cdSliderReading.grid(row=1, column=2, padx=110, pady=(123, 0), sticky=NW)

        self.cdDisplay.set(5)
        # *** Color Distribution ***

        # *** Line Thickness ***
        # also known as the thicc boi parameter
        self.ltSliderText.configure(background='LightGrey')
        self.ltSliderText.grid(row=1, column=2, padx=0, pady=(150, 0), sticky=NW)

        self.ltDisplay.grid(row=1, column=2, padx=3, pady=(170, 0), sticky=NW)

        self.ltSliderReading.configure(background='LightGrey')
        self.ltSliderReading.grid(row=1, column=2, padx=110, pady=(173, 0), sticky=NW)

        self.ltDisplay.set(3)
        # ***Line Thickness ***

        # *** Line Spacing ***
        self.lsSliderText.configure(background='LightGrey')
        self.lsSliderText.grid(row=1, column=2, padx=0, pady=(200, 0), sticky=NW)

        self.lsDisplay.grid(row=1, column=2, padx=3, pady=(220, 0), sticky=NW)

        self.lsSliderReading.configure(background='LightGrey')
        self.lsSliderReading.grid(row=1, column=2, padx=110, pady=(223, 0), sticky=NW)

        self.lsDisplay.set(20)
        # *** Line Spacing ***

        # *** Horizontal Rectangle Split Chance ***
        self.hrscSliderText.configure(background='LightGrey')
        self.hrscSliderText.grid(row=1, column=2, padx=0, pady=(250, 0), sticky=NW)

        self.hrscDisplay.grid(row=1, column=2, padx=3, pady=(270, 0), sticky=NW)

        self.hrscSliderReading.configure(background='LightGrey')
        self.hrscSliderReading.grid(row=1, column=2, padx=110, pady=(273, 0), sticky=NW)

        self.hrscDisplay.set(50)
        # *** Horizontal Rectangle Split Chance ***

        # *** Vertical Rectangle Split Chance ***
        self.vrscSliderText.configure(background='LightGrey')
        self.vrscSliderText.grid(row=1, column=2, padx=0, pady=(300, 0), sticky=NW)

        self.vrscDisplay.grid(row=1, column=2, padx=3, pady=(320, 0), sticky=NW)

        self.vrscSliderReading.configure(background='LightGrey')
        self.vrscSliderReading.grid(row=1, column=2, padx=110, pady=(323, 0), sticky=NW)

        self.vrscDisplay.set(50)
        # *** Vertical Rectangle Split Chance ***

        # *** Neighboring Color Chance ***
        self.nccSliderText.configure(background='LightGrey')
        self.nccSliderText.grid(row=1, column=2, padx=0, pady=(350, 0), sticky=NW)

        self.nccDisplay.grid(row=1, column=2, padx=3, pady=(370, 0), sticky=NW)

        self.nccSliderReading.configure(background='LightGrey')
        self.nccSliderReading.grid(row=1, column=2, padx=110, pady=(373, 0), sticky=NW)
        # *** Neighboring Color Chance ***

        # *** White Rectangle Chance ***
        self.wrcSliderText.configure(background='LightGrey')
        self.wrcSliderText.grid(row=1, column=2, padx=0, pady=(400, 0), sticky=NW)

        self.wrcDisplay.grid(row=1, column=2, padx=3, pady=(420, 0), sticky=NW)

        self.wrcSliderReading.configure(background='LightGrey')
        self.wrcSliderReading.grid(row=1, column=2, padx=110, pady=(423, 0), sticky=NW)
        # *** White Rectangle Chance ***

        # ** Generate Button **
        self.generateButton.grid(row=1, column=2, padx=0, pady=(450, 0), sticky=SW)

        # ** Reset Button **
        self.resetButton.grid(row=1, column=2, padx=65, pady=(450, 0), sticky=SW)

        # ** Random Button **
        self.randomButton.grid(row=1, column=2, padx=150, pady=(400, 0), sticky=SW)

    def set_aspect(self, x, y):
        self.aspect_x = x
        self.aspect_y = y
        self.update_ratio()

    def update_ratio(self):
        self.aspectPresent.destroy()

        self.aspectPresent = Label(self.master, text=str(self.aspect_x) + ":" + str(self.aspect_y) + "px")
        self.aspectPresent.configure(background='LightGrey')
        self.aspectPresent.grid(row=1, column=0, padx=150, pady=(0, 0), sticky=NW)

    def h_line_get(self):
        return '{: .2f}'.format(self.h_line.get())

    def h_line_changed(self, event):  # event is being used, do not delete argument
        # print(self.hLineDisplay.get())  # print line to console
        self.hLineSliderReading.configure(text=self.h_line_get())

    def v_line_get(self):
        return '{: .2f}'.format(self.v_line.get())

    def v_line_changed(self, event):  # event is being used, do not delete argument
        # print(self.vLineDisplay.get()) # print line to console
        self.vLineSliderReading.configure(text=self.v_line_get())

    def cd_get(self):
        return '{: .2f}'.format(self.color_dist.get())

    def cd_changed(self, event):
        self.cdSliderReading.configure(text=self.cd_get())

    def lt_get(self):
        return '{: .2f}'.format(self.line_thickness.get())

    def lt_changed(self, event):
        self.ltSliderReading.configure(text=self.lt_get())

    def ls_get(self):
        return '{: .2f}'.format(self.line_spacing.get())

    def ls_changed(self, event):
        self.lsSliderReading.configure(text=self.ls_get())

    def hrsc_get(self):
        return '{: .2f}'.format(self.hrsc.get())

    def hrsc_changed(self, event):
        self.hrscSliderReading.configure(text=self.hrsc_get())

    def vrsc_get(self):
        return '{: .2f}'.format(self.vrsc.get())

    def vrsc_changed(self, event):
        self.vrscSliderReading.configure(text=self.vrsc_get())

    def ncc_get(self):
        return '{: .2f}'.format(self.ncc.get())

    def ncc_changed(self, event):
        self.nccSliderReading.configure(text=self.ncc_get())

    def wrc_get(self):
        return '{: .2f}'.format(self.wrc.get())

    def wrc_changed(self, event):
        self.wrcSliderReading.configure(text=self.wrc_get())

    def delete_image(self):
        self.imagePresent.destroy()

    def preview_image(self):
        self.delete_image()
        new_image = PIL.Image.new("RGB", (self.aspect_x, self.aspect_y), color=(255, 255, 255))

        self.photoImageNewImage = ImageTk.PhotoImage(new_image)
        self.imageTest = Label(self.master, image=self.photoImageNewImage)
        self.imageTest.grid(row=1, column=1, padx=20, pady=(0, 0), sticky=W)

    def create_url_image(self, url):
        image_accessor = urlopen(url)
        raw = image_accessor.read()
        image_accessor.close()

        self.img = ImageTk.PhotoImage(data=raw)
        self.imagePresent = Label(self.master, image=self.img)
        self.imagePresent.grid(row=1, column=1, padx=20, pady=(0, 0), sticky=W)

    def no_image_image(self):
        self.delete_image()
        no_image_url = 'https://i.imgur.com/lC0Rslm.jpg'
        self.create_url_image(no_image_url)

    def default_url_image(self):
        self.delete_image()
        default_image_url = 'https://i.imgur.com/86DUwF5.png'
        self.create_url_image(default_image_url)

    def get_neighbor_chance(self):
        if int(float(self.ncc_get())) >= random.randrange(1, 100):
            return True
        else:
            return False

    def get_white_chance(self):
        if int(float(self.wrc_get())) <= random.randrange(1, 100):
            return True
        else:
            return False

    def set_random(self):
        self.hLineDisplay.set(random.randrange(0, 10))
        self.vLineDisplay.set(random.randrange(0, 15))
        self.cdDisplay.set(random.randrange(1, 10))
        self.ltDisplay.set(random.randrange(1, 5))
        self.lsDisplay.set(random.randrange(15, 20))
        self.hrscDisplay.set(random.randrange(0, 100))
        self.vrscDisplay.set(random.randrange(0, 100))
        self.nccDisplay.set(random.randrange(0, 100))
        self.wrcDisplay.set(random.randrange(0, 100))

    def random_gen(self):
        self.set_random()
        self.generate_image()

    def generate_image(self):
        self.delete_image()
        os.remove("SaveHere/image.png")
        new_image = PIL.Image.new("RGB", (self.aspect_x, self.aspect_y), color=(255, 255, 255))

        with (new_image as canvas):
            paint = ImageDraw.Draw(canvas)
            # *** Create color list and populate it ***
            # First six colors are colors from Mondrian's original works always
            color_list = [(45, 45, 46), (179, 34, 48), (42, 66, 106), (164, 167, 209), (240, 211, 45)]
            i = 0
            while i < 5:
                color_list.append(((random.randrange(0, 255)), (random.randrange(0, 255)),
                                   (random.randrange(0, 255))))
                i += 1

            # *** Generate Lines ***

            paint.line((10, 10, self.aspect_x - 10, 10), fill=(0, 0, 0), width=1)
            paint.line((10, self.aspect_y - 10, self.aspect_x - 10, self.aspect_y - 10), fill=(0, 0, 0),
                       width=1)
            paint.line((10, 10, 10, self.aspect_y - 10), fill=(0, 0, 0), width=1)
            paint.line((self.aspect_x - 10, 10, self.aspect_x - 10, self.aspect_y - 10), fill=(0, 0, 0),
                       width=1)

            h_line_list = [10, self.aspect_y-10]
            v_line_list = [10, self.aspect_x-10]
            i = 0

            # Paint horizontal lines
            while i < int(float(self.h_line_get())):
                different = False
                random_pos = random.randrange(11, self.aspect_y - 11)

                if i == 0:
                    while not different:
                        if 10+int(float(self.ls_get())) < random_pos < self.aspect_y-int(float(self.ls_get())) - 10:
                            different = True
                        if different:
                            paint.line((10, random_pos, self.aspect_x - 10, random_pos), fill=(0, 0, 0), width=1)
                            h_line_list.append(random_pos)
                        else:
                            random_pos = random.randrange(11, self.aspect_y - 11)
                    i += 1
                else:
                    while not different:
                        for j in h_line_list:
                            if random_pos > j+int(float(self.ls_get())):
                                different = True
                            elif random_pos < j-int(float(self.ls_get())):
                                different = True
                            else:
                                different = False
                                break

                        if different:
                            paint.line((10, random_pos, self.aspect_x - 10, random_pos), fill=(0, 0, 0), width=1)
                            h_line_list.append(random_pos)
                        else:
                            random_pos = random.randrange(11, self.aspect_y - 11)
                    i += 1
            i = 0

            # Paint vertical lines
            while i < int(float(self.v_line_get())):
                different = False
                random_pos = random.randrange(11, self.aspect_x - 11)

                if i == 0:
                    while not different:
                        if 10+int(float(self.ls_get())) < random_pos < self.aspect_x-int(float(self.ls_get())) - 10:
                            different = True
                        if different:
                            paint.line((random_pos, 10, random_pos, self.aspect_y - 10), fill=(0, 0, 0), width=1)
                            v_line_list.append(random_pos)
                        else:
                            random_pos = random.randrange(11, self.aspect_x - 11)
                    i += 1
                else:
                    while not different:
                        for j in v_line_list:
                            if random_pos > j + int(float(self.ls_get())):
                                different = True
                            elif random_pos < j - int(float(self.ls_get())):
                                different = True
                            else:
                                different = False
                                break
                        if different:
                            paint.line((random_pos, 10, random_pos, self.aspect_y - 10), fill=(0, 0, 0), width=1)
                            v_line_list.append(random_pos)
                        else:
                            random_pos = random.randrange(11, self.aspect_x - 11)
                    i += 1

            # *** Detect rectangles and apply color ***

            point_x = 10
            point_y = 10
            rect_color = color_list[random.randrange(0, int(float(self.cd_get())))]
            painted_white = False

            # Starts top left of image
            while point_x != self.aspect_x - 10 and point_y != self.aspect_y - 10:
                # Roll split chances
                v_split_chance = False
                if int(float(self.vrsc_get())) >= random.randrange(1, 100):
                    v_split_chance = True
                h_split_chance = False
                if int(float(self.hrsc_get())) >= random.randrange(1, 100):
                    h_split_chance = True
                v_split_counter = 0
                h_split_counter = 0
                # Save top left position of rectangle
                x_1 = point_x
                y_1 = point_y

                # Position at bottom left of rectangle
                point_y += 1
                while new_image.getpixel((point_x + 1, point_y)) != (0, 0, 0):
                    point_y += 1
                    h_split_counter += 1
                # If rectangle must split horizontally
                if h_split_chance:
                    h_split_counter = h_split_counter // 2
                    decision = random.randrange(0, 1)
                    if decision == 0:
                        h_split_y = point_y - random.randrange(5, h_split_counter)
                    else:
                        h_split_y = point_y + random.randrange(5, h_split_counter)
                    split_x_1 = point_x
                    split_x_2 = point_x
                    # Find opposite line
                    while new_image.getpixel((split_x_2+1, h_split_y)) != (0, 0, 0):
                        split_x_2 += 1
                # Position at bottom right of rectangle
                point_x += 1
                while new_image.getpixel((point_x, point_y + 1)) != (0, 0, 0) and new_image.getpixel(
                        (point_x, point_y - 1)) != (0, 0, 0):
                    point_x += 1
                    v_split_counter += 1
                # If rectangle must split vertically
                if v_split_chance:
                    v_split_counter = v_split_counter // 2
                    decision = random.randrange(0, 1)
                    if decision == 0:
                        v_split_x = point_x - random.randrange(5, v_split_counter)
                    else:
                        v_split_x = point_x + random.randrange(5, v_split_counter)
                    split_y_1 = point_y
                    split_y_2 = point_y
                    # Find opposite line
                    while new_image.getpixel((v_split_x, split_y_2 - 1)) != (0, 0, 0):
                        split_y_2 -= 1
                # Save bottom right position of rectangle
                x_2 = point_x
                y_2 = point_y

                if not self.get_neighbor_chance() or painted_white:
                    rect_color = color_list[random.randrange(0, int(float(self.cd_get())))]
                if not self.get_white_chance():
                    paint.rectangle((x_1, y_1, x_2, y_2), fill=(255, 255, 255), outline=(0, 0, 0), width=1)
                    painted_white = True
                else:
                    # Fill rectangles with color
                    paint.rectangle((x_1, y_1, x_2, y_2), fill=rect_color, outline=(0, 0, 0), width=1)
                    painted_white = False
                # Paint both splits at once
                if h_split_chance and v_split_chance:
                    if not self.get_neighbor_chance() or painted_white:
                        rect_color = color_list[random.randrange(0, int(float(self.cd_get())))]
                    if not self.get_white_chance():
                        paint.rectangle((split_x_1 + 1, split_y_2, v_split_x - 1, h_split_y - 1), fill=(255, 255, 255),
                                        outline=(255, 255, 255), width=1)
                        painted_white = True
                    else:
                        paint.rectangle((split_x_1+1, split_y_2, v_split_x-1, h_split_y-1), fill=rect_color,
                                        outline=rect_color, width=1)
                        painted_white = False
                    if not self.get_neighbor_chance() or painted_white:
                        rect_color = color_list[random.randrange(0, int(float(self.cd_get())))]
                    if not self.get_white_chance():
                        paint.rectangle((v_split_x + 1, split_y_2, point_x - 1, h_split_y - 1), fill=(255, 255, 255),
                                        outline=(255, 255, 255), width=1)
                        painted_white = True
                    else:
                        paint.rectangle((v_split_x+1, split_y_2, point_x-1, h_split_y-1), fill=rect_color,
                                        outline=rect_color, width=1)
                        painted_white = False
                    if not self.get_neighbor_chance() or painted_white:
                        rect_color = color_list[random.randrange(0, int(float(self.cd_get())))]
                    if not self.get_white_chance():
                        paint.rectangle((v_split_x + 1, h_split_y + 1, point_x - 1, point_y - 1), fill=(255, 255, 255),
                                        outline=(255, 255, 255), width=1)
                        painted_white = True
                    else:
                        paint.rectangle((v_split_x+1, h_split_y+1, point_x-1, point_y-1), fill=rect_color,
                                        outline=rect_color, width=1)
                        painted_white = False
                    paint.line((split_x_1 + 1, h_split_y, split_x_2, h_split_y), fill=(0, 1, 0),
                               width=int(float(self.lt_get())))
                    paint.line((v_split_x, split_y_1 - 1, v_split_x, split_y_2), fill=(0, 1, 0),
                               width=int(float(self.lt_get())))
                # Paint horizontal split
                elif h_split_chance and not v_split_chance:
                    if not self.get_neighbor_chance() or painted_white:
                        rect_color = color_list[random.randrange(0, int(float(self.cd_get())))]
                    if not self.get_white_chance():
                        paint.rectangle((split_x_1 + 1, h_split_y+1, point_x - 1, point_y - 1),
                                        fill=(255, 255, 255), outline=(255, 255, 255), width=1)
                        painted_white = True
                    else:
                        paint.rectangle((split_x_1+1, h_split_y+1, point_x - 1, point_y - 1),
                                        fill=rect_color, outline=rect_color, width=1)
                        painted_white = False
                    paint.line((split_x_1 + 1, h_split_y, split_x_2, h_split_y), fill=(0, 1, 0),
                               width=int(float(self.lt_get())))
                # Paint vertical split
                elif v_split_chance and not h_split_chance:
                    if not self.get_neighbor_chance() or painted_white:
                        rect_color = color_list[random.randrange(0, int(float(self.cd_get())))]
                    if not self.get_white_chance():
                        paint.rectangle((v_split_x + 1, split_y_2, point_x - 1, point_y - 1), fill=(255, 255, 255),
                                        outline=(255, 255, 255), width=1)
                        painted_white = True
                    else:
                        paint.rectangle((v_split_x+1, split_y_2, point_x-1, point_y-1), fill=rect_color,
                                        outline=rect_color, width=1)
                        painted_white = False
                    paint.line((v_split_x, split_y_1 - 1, v_split_x, split_y_2), fill=(0, 1, 0),
                               width=int(float(self.lt_get())))

                # Position back to bottom right of rectangle
                point_x -= 1
                while new_image.getpixel((point_x, point_y + 1)) != (0, 0, 0) and new_image.getpixel(
                        (point_x, point_y - 1)) != (0, 0, 0):
                    point_x -= 1

                # If at end of rectangle column
                if point_y == self.aspect_y - 10:
                    # Position bottom right of rectangle
                    point_x += 1
                    while new_image.getpixel((point_x, point_y + 1)) != (0, 0, 0) and new_image.getpixel(
                            (point_x, point_y - 1)) != (0, 0, 0):
                        point_x += 1
                    # Position at top of next rectangle set
                    while point_y != 10:
                        point_y -= 1

            # *** Apply line thickness ***

            # Thickify horizontal lines
            for j in h_line_list:
                paint.line((10, j, self.aspect_x - 10, j), fill=(0, 0, 1), width=int(float(self.lt_get())))
            # Thickify vertical lines
            for j in v_line_list:
                paint.line((j, 10, j, self.aspect_y - 10), fill=(0, 0, 1), width=int(float(self.lt_get())))
            # Thickify Boundary Box
            paint.line((10, 10, self.aspect_x - 10, 10), fill=(0, 0, 1), width=int(float(self.lt_get())))
            paint.line((10, self.aspect_y - 10, self.aspect_x - 10, self.aspect_y - 10), fill=(0, 0, 1),
                       width=int(float(self.lt_get())))
            paint.line((10, 10, 10, self.aspect_y - 10), fill=(0, 0, 1), width=int(float(self.lt_get())))
            paint.line((self.aspect_x - 10, 10, self.aspect_x - 10, self.aspect_y - 10), fill=(0, 0, 1),
                       width=int(float(self.lt_get())))

            # Repaint thin lines for testing
            for j in h_line_list:
                paint.line((10, j, self.aspect_x - 10, j), fill=(0, 0, 0), width=1)
            for j in v_line_list:
                paint.line((j, 10, j, self.aspect_y - 10), fill=(0, 0, 0), width=1)

            paint.line((10, 10, self.aspect_x - 10, 10), fill=(0, 0, 0), width=1)
            paint.line((10, self.aspect_y - 10, self.aspect_x - 10, self.aspect_y - 10), fill=(0, 0, 0),
                       width=1)
            paint.line((10, 10, 10, self.aspect_y - 10), fill=(0, 0, 0), width=1)
            paint.line((self.aspect_x - 10, 10, self.aspect_x - 10, self.aspect_y - 10), fill=(0, 0, 0),
                       width=1)

        self.photoImageNewImage = ImageTk.PhotoImage(new_image)
        self.imageTest = Label(self.master, image=self.photoImageNewImage)
        self.imageTest.grid(row=1, column=1, padx=20, pady=(0, 0), sticky=W)\

        new_image.save("SaveHere/image.png")

        return new_image

