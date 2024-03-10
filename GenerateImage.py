import PIL
from PIL import Image, ImageDraw

import random
import os


class GenerateImage:
    # Initialize default values and set parameters either through direct input or default values.
    def __init__(self, param_list=None):
        # Define Parameters

        self.aspect_x = 700
        self.aspect_y = 400
        self.h_line_list = []
        self.v_line_list = []

        self.new_image = PIL.Image.new("RGB", (self.aspect_x, self.aspect_y), color=(255, 255, 255))
        self.color_list = [(45, 45, 46), (179, 34, 48), (42, 66, 106), (164, 167, 209), (240, 211, 45)]

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

    # Used to set random parameter values within their allowed limits
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

    # Returns a list of all current parameters in the same order as they came in
    def param_get(self):
        params = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        params[0] = self.h_line
        params[1] = self.v_line
        params[2] = self.cd
        params[3] = self.lt
        params[4] = self.ls
        params[5] = self.hrsc
        params[6] = self.vrsc
        params[7] = self.ncc
        params[8] = self.wrc

        return params

    # Getter and setter functions for individual parameter values
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

    # First step in the image generation algorithm, creating the color list.
    def create_color_list(self):
        # First six colors are always colors from Mondrian's original works always
        i = 0
        while i < 5:
            self.color_list.append(((random.randrange(0, 255)), (random.randrange(0, 255)),
                               (random.randrange(0, 255))))
            i += 1

    # Second step in the image generation algorithm
    # Creates a black boundary box for which the rest of the image will be painted inside of
    def generate_lines(self):
        with (self.new_image as canvas):
            paint = ImageDraw.Draw(canvas)
            # *** Generate Lines ***

            paint.line((10, 10, self.aspect_x - 10, 10), fill=(0, 0, 0), width=1)
            paint.line((10, self.aspect_y - 10, self.aspect_x - 10, self.aspect_y - 10), fill=(0, 0, 0),
                       width=1)
            paint.line((10, 10, 10, self.aspect_y - 10), fill=(0, 0, 0), width=1)
            paint.line((self.aspect_x - 10, 10, self.aspect_x - 10, self.aspect_y - 10), fill=(0, 0, 0),
                       width=1)

            self.h_line_list = [10, self.aspect_y - 10]
            self.v_line_list = [10, self.aspect_x - 10]
        return self.new_image

    # The first major step in the image generation algorithm which aims to paint the first round of lines, the
    # horizontal lines. These lines are painted across the canvas, from boundary to boundary, spread out according
    # to the line spacing parameter.
    def paint_horizontal(self):
        with (self.new_image as canvas):
            paint = ImageDraw.Draw(canvas)
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
                            self.h_line_list.append(random_pos)
                        else:
                            random_pos = random.randrange(11, self.aspect_y - 11)
                    i += 1
                else:
                    while not different:
                        for j in self.h_line_list:
                            if random_pos > j + int(float(self.ls_get())):
                                different = True
                            elif random_pos < j - int(float(self.ls_get())):
                                different = True
                            else:
                                different = False
                                break

                        if different:
                            paint.line((10, random_pos, self.aspect_x - 10, random_pos), fill=(0, 0, 0), width=1)
                            self.h_line_list.append(random_pos)
                        else:
                            random_pos = random.randrange(11, self.aspect_y - 11)
                    i += 1
        return self.new_image

    # The second major step in the image generation algorithm which aims to paint the second round of lines, the
    # vertical lines. These lines are painted across the canvas, from boundary to boundary, spread out according
    # to the line spacing parameter.
    def paint_vertical(self):
        with (self.new_image as canvas):
            paint = ImageDraw.Draw(canvas)
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
                            self.v_line_list.append(random_pos)
                        else:
                            random_pos = random.randrange(11, self.aspect_x - 11)
                    i += 1
                else:
                    while not different:
                        for j in self.v_line_list:
                            if random_pos > j + int(float(self.ls_get())):
                                different = True
                            elif random_pos < j - int(float(self.ls_get())):
                                different = True
                            else:
                                different = False
                                break
                        if different:
                            paint.line((random_pos, 10, random_pos, self.aspect_y - 10), fill=(0, 0, 0), width=1)
                            self.v_line_list.append(random_pos)
                        else:
                            random_pos = random.randrange(11, self.aspect_x - 11)
                    i += 1
        return self.new_image

    # This is the third major step in the image generation algorithm which paints rectangles created by intersections
    # between the previously painted vertical and horizontal lines. It begins tracing lines from the top left of
    # the canvas to "discover" rectangles to paint and potentially divide into sub rectangles depending on the
    # split chance.
    #
    # Rectangles are painted once the algorithm finds the two bounding coordinates of a rectangle. This painting is
    # based on three parameters, the chance of it being white, the chance of it being the color of it's neighbor,
    # and finally the color randomly selected from the previously created color list. The color takes priority based on
    # the order previous, a rectangle will be white if it rolls it so, if not then the same color and if not those two,
    # then a random color from the list.
    #
    # The general flow of the algorithm detects rectangles from top left, down to the bottom of the first set, then
    # positions itself back at the top right of the next set. This repeats until it hits the edge of the right most
    # boundary box.
    #
    # Below is a small diagram which follows the general flow of the algorithm through a painted canvas with lines.
    #
    # Arrows are the direction the algorithm traces, starting from the top left. ↓ ↑ → ←
    # An x represents a coordinate needed to color a specific rectangle, the algorithm traverses to reach all x.
    #
    #
    #        #1          #2          #3
    # ↓ x-----------|-----------|-----------|
    # ↓ |           |   ↑       |           |
    # ↓ |           |   ↑       |           |
    # ↓ |           |   ↑       |           |
    # ↓ |           |   ↑       |           |
    # ↓ x-----------x-----------|-----------|
    #   |→→→→→→→→→→→|   ↑       |           |
    # ↓ |←←←←←←←←←←←|   ↑       |           |
    # ↓ |           |   ↑       |           |
    # ↓ |           |   ↑       |           |
    # ↓ x-----------x-----------|-----------|
    #   |→→→→→→→→→→→|   ↑       |           |
    #   |←←←←←←←←←←←|   ↑       |           |
    # ↓ |           |   ↑       |           |
    # ↓ |           |   ↑       |           |
    # ↓ |-----------x-----------|-----------|
    # ↓  →→→→→→→→→→→→→→ ↑
    #
    # The pattern illustrated here repeats for section 2 and 3 to find all rectangles. Although the rectangles in this
    # example are uniform, this works for rectangles of varying sizes and positions across the canvas.
    def rectangle_recognition(self):
        with (self.new_image as canvas):
            paint = ImageDraw.Draw(canvas)
            # *** Detect rectangles and apply color ***

            point_x = 10
            point_y = 10
            rect_color = self.color_list[random.randrange(0, int(float(self.cd_get())))]
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
                while self.new_image.getpixel((point_x + 1, point_y)) != (0, 0, 0):
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
                    while self.new_image.getpixel((split_x_2 + 1, h_split_y)) != (0, 0, 0):
                        split_x_2 += 1
                # Position at bottom right of rectangle
                point_x += 1
                while self.new_image.getpixel((point_x, point_y + 1)) != (0, 0, 0) and self.new_image.getpixel(
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
                    while self.new_image.getpixel((v_split_x, split_y_2 - 1)) != (0, 0, 0):
                        split_y_2 -= 1
                # Save bottom right position of rectangle
                x_2 = point_x
                y_2 = point_y

                if not self.get_neighbor_chance() or painted_white:
                    rect_color = self.color_list[random.randrange(0, int(float(self.cd_get())))]
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
                        rect_color = self.color_list[random.randrange(0, int(float(self.cd_get())))]
                    if not self.get_white_chance():
                        paint.rectangle((split_x_1 + 1, split_y_2, v_split_x - 1, h_split_y - 1), fill=(255, 255, 255),
                                        outline=(255, 255, 255), width=1)
                        painted_white = True
                    else:
                        paint.rectangle((split_x_1 + 1, split_y_2, v_split_x - 1, h_split_y - 1), fill=rect_color,
                                        outline=rect_color, width=1)
                        painted_white = False
                    if not self.get_neighbor_chance() or painted_white:
                        rect_color = self.color_list[random.randrange(0, int(float(self.cd_get())))]
                    if not self.get_white_chance():
                        paint.rectangle((v_split_x + 1, split_y_2, point_x - 1, h_split_y - 1), fill=(255, 255, 255),
                                        outline=(255, 255, 255), width=1)
                        painted_white = True
                    else:
                        paint.rectangle((v_split_x + 1, split_y_2, point_x - 1, h_split_y - 1), fill=rect_color,
                                        outline=rect_color, width=1)
                        painted_white = False
                    if not self.get_neighbor_chance() or painted_white:
                        rect_color = self.color_list[random.randrange(0, int(float(self.cd_get())))]
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
                        rect_color = self.color_list[random.randrange(0, int(float(self.cd_get())))]
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
                        rect_color = self.color_list[random.randrange(0, int(float(self.cd_get())))]
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
                while self.new_image.getpixel((point_x, point_y + 1)) != (0, 0, 0) and self.new_image.getpixel(
                        (point_x, point_y - 1)) != (0, 0, 0):
                    point_x -= 1

                # If at end of rectangle column
                if point_y == self.aspect_y - 10:
                    # Position bottom right of rectangle
                    point_x += 1
                    while self.new_image.getpixel((point_x, point_y + 1)) != (0, 0, 0) and self.new_image.getpixel(
                            (point_x, point_y - 1)) != (0, 0, 0):
                        point_x += 1
                    # Position at top of next rectangle set
                    while point_y != 10:
                        point_y -= 1
        return self.new_image

    # This is the last major step in the image generation algorithm which goes over all painted lines with a thicker
    # line based on the line thickness parameter. This is much easier since earlier the start and end coordinates of all
    # lines were saved, so it's just a matter of painting them again with a thicker line.
    def thickify_lines(self):
        with (self.new_image as canvas):
            paint = ImageDraw.Draw(canvas)
            # *** Apply line thickness ***

            # Thickify horizontal lines
            for j in self.h_line_list:
                paint.line((10, j, self.aspect_x - 10, j), fill=(0, 0, 1), width=int(float(self.lt_get())))
            # Thickify vertical lines
            for j in self.v_line_list:
                paint.line((j, 10, j, self.aspect_y - 10), fill=(0, 0, 1), width=int(float(self.lt_get())))
            # Thickify Boundary Box
            paint.line((10, 10, self.aspect_x - 10, 10), fill=(0, 0, 1), width=int(float(self.lt_get())))
            paint.line((10, self.aspect_y - 10, self.aspect_x - 10, self.aspect_y - 10), fill=(0, 0, 1),
                       width=int(float(self.lt_get())))
            paint.line((10, 10, 10, self.aspect_y - 10), fill=(0, 0, 1), width=int(float(self.lt_get())))
            paint.line((self.aspect_x - 10, 10, self.aspect_x - 10, self.aspect_y - 10), fill=(0, 0, 1),
                       width=int(float(self.lt_get())))
        return self.new_image

    # This function is the final step and only matters for testing. Since tracing thicker lines complicates an already
    # complicated algorithm, a thin line is repainted over the thick lines using a specific color value that can be
    # picked up within test cases. This color is one rgb value off from the black value used earlier, so it is near
    # impossible to see the difference with a human eye.
    def repaint(self):
        with (self.new_image as canvas):
            paint = ImageDraw.Draw(canvas)
            # Repaint thin lines for testing
            for j in self.h_line_list:
                paint.line((10, j, self.aspect_x - 10, j), fill=(0, 0, 0), width=1)
            for j in self.v_line_list:
                paint.line((j, 10, j, self.aspect_y - 10), fill=(0, 0, 0), width=1)

            paint.line((10, 10, self.aspect_x - 10, 10), fill=(0, 0, 0), width=1)
            paint.line((10, self.aspect_y - 10, self.aspect_x - 10, self.aspect_y - 10), fill=(0, 0, 0),
                       width=1)
            paint.line((10, 10, 10, self.aspect_y - 10), fill=(0, 0, 0), width=1)
            paint.line((self.aspect_x - 10, 10, self.aspect_x - 10, self.aspect_y - 10), fill=(0, 0, 0),
                       width=1)
        return self.new_image

    # This function calls all image generation functions in order to create our version of a Mondrian using parameters
    # decided on by us and our industry mentor. Images are currently saved in a static folder to be displayed, which may
    # or may not be changed in the future to a database system given we have enough time.
    def generate_image(self):
        self.create_color_list()
        self.generate_lines()
        self.paint_horizontal()
        self.paint_vertical()
        self.rectangle_recognition()
        self.thickify_lines()
        self.repaint()

        self.new_image.save("static/photos/image.png")

        return self.new_image

