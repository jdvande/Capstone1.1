import PIL
from PIL import Image, ImageDraw

import random
import os


class GenerateImage:
    def __init__(self, param_list=None):
        # Define Parameters

        self.aspect_x = 700
        self.aspect_y = 400

        if param_list is None:
            # horizontal line count
            self.h_line = 0
            # vertical line count
            self.v_line = 0
            # cd = color distribution
            self.cd = 0
            # lt = line thickness
            self.lt = 0
            # ls = line spacing
            self.ls = 0
            # hrsc = horizontal rectangle split chance
            self.hrsc = 0
            # vrsc = vertical rectangle split chance
            self.vrsc = 0
            # ncc = neighboring color chance
            self.ncc = 0
            # wrc = white rectangle chance
            self.wrc = 0
        else:
            # horizontal line count
            self.h_line = param_list[0]
            # vertical line count
            self.v_line = param_list[1]
            # cd = color distribution
            self.cd = param_list[2]
            # lt = line thickness
            self.lt = param_list[3]
            # ls = line spacing
            self.ls = param_list[4]
            # hrsc = horizontal rectangle split chance
            self.hrsc = param_list[5]
            # vrsc = vertical rectangle split chance
            self.vrsc = param_list[6]
            # ncc = neighboring color chance
            self.ncc = param_list[7]
            # wrc = white rectangle chance
            self.wrc = param_list[8]

    def set_random(self):
        self.h_line = random.randrange(0, 10)
        self.v_line = random.randrange(0, 15)
        self.cd = random.randrange(1, 10)
        self.lt = random.randrange(1, 5)
        self.ls = random.randrange(15, 20)
        self.hrsc = random.randrange(0, 100)
        self.vrsc = random.randrange(0, 100)
        self.ncc = random.randrange(0, 100)
        self.wrc = random.randrange(0, 100)

    def h_line_get(self):
        return self.h_line

    def v_line_get(self):
        return self.v_line

    def cd_get(self):
        return self.cd

    def lt_get(self):
        return self.lt

    def ls_get(self):
        return self.ls

    def hrsc_get(self):
        return self.hrsc

    def vrsc_get(self):
        return self.vrsc

    def ncc_get(self):
        return self.ncc

    def wrc_get(self):
        return self.wrc

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

    def generate_image(self):
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

            h_line_list = [10, self.aspect_y - 10]
            v_line_list = [10, self.aspect_x - 10]
            i = 0

            # Paint horizontal lines
            while i < int(float(self.h_line_get())):
                different = False
                random_pos = random.randrange(11, self.aspect_y - 11)

                if i == 0:
                    while not different:
                        if 10 + int(float(self.ls_get())) < random_pos < self.aspect_y - int(float(self.ls_get())) - 10:
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
                            if random_pos > j + int(float(self.ls_get())):
                                different = True
                            elif random_pos < j - int(float(self.ls_get())):
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
                        if 10 + int(float(self.ls_get())) < random_pos < self.aspect_x - int(float(self.ls_get())) - 10:
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
                    while new_image.getpixel((split_x_2 + 1, h_split_y)) != (0, 0, 0):
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
                        paint.rectangle((split_x_1 + 1, split_y_2, v_split_x - 1, h_split_y - 1), fill=rect_color,
                                        outline=rect_color, width=1)
                        painted_white = False
                    if not self.get_neighbor_chance() or painted_white:
                        rect_color = color_list[random.randrange(0, int(float(self.cd_get())))]
                    if not self.get_white_chance():
                        paint.rectangle((v_split_x + 1, split_y_2, point_x - 1, h_split_y - 1), fill=(255, 255, 255),
                                        outline=(255, 255, 255), width=1)
                        painted_white = True
                    else:
                        paint.rectangle((v_split_x + 1, split_y_2, point_x - 1, h_split_y - 1), fill=rect_color,
                                        outline=rect_color, width=1)
                        painted_white = False
                    if not self.get_neighbor_chance() or painted_white:
                        rect_color = color_list[random.randrange(0, int(float(self.cd_get())))]
                    if not self.get_white_chance():
                        paint.rectangle((v_split_x + 1, h_split_y + 1, point_x - 1, point_y - 1), fill=(255, 255, 255),
                                        outline=(255, 255, 255), width=1)
                        painted_white = True
                    else:
                        paint.rectangle((v_split_x + 1, h_split_y + 1, point_x - 1, point_y - 1), fill=rect_color,
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
                        paint.rectangle((split_x_1 + 1, h_split_y + 1, point_x - 1, point_y - 1),
                                        fill=(255, 255, 255), outline=(255, 255, 255), width=1)
                        painted_white = True
                    else:
                        paint.rectangle((split_x_1 + 1, h_split_y + 1, point_x - 1, point_y - 1),
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
                        paint.rectangle((v_split_x + 1, split_y_2, point_x - 1, point_y - 1), fill=rect_color,
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

        new_image.save("static/photos/image.png")

        return new_image

