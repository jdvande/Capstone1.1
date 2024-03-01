# Requires pytest module

import PIL
from PIL import ImageTk, Image, ImageDraw

from GenerateImage import GenerateImage

import pytest
import os


class TestSuite:
    def test_generate(self):
        generate_test = GenerateImage()
        total_tests = 0
        while total_tests < 100:
            generate_test.set_random()
            generate_test.generate_image()
            total_tests += 1

    def test_v_line_count(self):
        v_line_test = GenerateImage()
        total_tests = 0
        while total_tests < 100:
            v_line_test.set_random()
            v_line_count = int(float(v_line_test.v_line_get()))

            start_x = 11
            start_y = 11

            v_test_image = v_line_test.generate_image()
            total_v_lines = 0
            while start_x < v_line_test.aspect_x - 11:
                if v_test_image.getpixel((start_x, start_y)) == (0, 0, 0):
                    total_v_lines += 1
                start_x += 1

            assert total_v_lines == v_line_count
            total_tests += 1

    def test_h_line_count(self):
        h_line_test = GenerateImage()
        total_tests = 0
        while total_tests < 100:
            h_line_test.set_random()
            h_line_count = int(float(h_line_test.h_line_get()))

            start_x = 11
            start_y = 11

            h_test_image = h_line_test.generate_image()
            total_h_lines = 0
            while start_y < h_line_test.aspect_y - 11:
                if h_test_image.getpixel((start_x, start_y)) == (0, 0, 0):
                    total_h_lines += 1
                start_y += 1

            assert total_h_lines == h_line_count
            total_tests += 1

    def test_line_spacing(self):
        ls_test = GenerateImage()
        total_tests = 0
        # Randomize Values
        while total_tests < 100:
            ls_test.set_random()
            line_spacing = int(float(ls_test.ls_get()))

            start_x = 10
            start_y = 10
            separation_count = line_spacing

            ls_image = ls_test.generate_image()

            # *** Test if vertical lines are separated enough ***
            while start_x < ls_test.aspect_x - 10:
                if ls_image.getpixel((start_x, 11)) == (0, 0, 0):
                    assert separation_count >= line_spacing
                    separation_count = 0

                start_x += 1
                separation_count += 1

            separation_count = line_spacing
            # *** Test if horizontal lines are separated enough ***
            while start_y < ls_test.aspect_y - 10:
                if ls_image.getpixel((11, start_y)) == (0, 0, 0):
                    assert separation_count >= line_spacing
                    separation_count = 0

                start_y += 1
                separation_count += 1
            total_tests += 1

    def test_line_thickness(self):
        lt_test = GenerateImage()
        total_tests = 0
        # Randomize Values
        while total_tests < 100:
            lt_test.set_random()
            line_thickness = int(float(lt_test.lt_get()))

            start_x = 0
            start_y = 14
            thickness_count = 0
            on_line = False

            lt_image = lt_test.generate_image()

            while start_x < lt_test.aspect_x:
                if (lt_image.getpixel((start_x, start_y)) == (0, 0, 1) or
                        lt_image.getpixel((start_x, start_y)) == (0, 0, 0)):
                    on_line = True
                    thickness_count += 1

                if on_line and (lt_image.getpixel((start_x, start_y)) != (0, 0, 1) and
                                lt_image.getpixel((start_x, start_y)) != (0, 0, 0)):
                    assert thickness_count == line_thickness
                    on_line = False
                    thickness_count = 0
                start_x += 1

            start_x = 14
            start_y = 0
            thickness_count = 0
            on_line = False

            while start_y < lt_test.aspect_y:
                if (lt_image.getpixel((start_x, start_y)) == (0, 0, 1) or
                        lt_image.getpixel((start_x, start_y)) == (0, 0, 0)):
                    on_line = True
                    thickness_count += 1

                if on_line and (lt_image.getpixel((start_x, start_y)) != (0, 0, 1) and
                                lt_image.getpixel((start_x, start_y)) != (0, 0, 0)):
                    assert thickness_count == line_thickness
                    on_line = False
                    thickness_count = 0
                start_y += 1

            total_tests += 1

    def test_image_saved(self):
        is_test = GenerateImage()
        is_test.set_random()
        is_test.generate_image()

        did_save = False

        if os.path.isfile("SaveHere/image.png"):
            did_save = True

        assert did_save
