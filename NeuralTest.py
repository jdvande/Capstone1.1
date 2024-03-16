import unittest
import os
from RateImage import rate_image
from PredictImage import PredictImage
from GenerateImage import GenerateImage
from PIL import Image


import unittest


class NeuralTest(unittest.TestCase):
    # This test case makes sure there are actual weights present so the neural network can rate images
    def test_is_running(self):
        is_running = False
        if os.path.isfile('weights/weights.pth'):
            is_running = True

        self.assertEqual(True, is_running)

    # This test case makes sure we can get an accurate class prediction from the neural network
    def test_can_predict(self):
        can_predict = False

        temp_generate = GenerateImage()
        temp_predict = PredictImage()

        temp_generate.set_random()
        img = temp_generate.generate_image()
        img.save("static/photos/image.png")

        predicted_class, probability = temp_predict.predict_image(temp_predict.preprocess_image())

        if (predicted_class >= 0) and (probability >= 0):
            can_predict = True

        self.assertEqual(True, can_predict)

    # This test case makes sure we can calculate a percentage of how accurate a generated image is to a Mondrian
    def test_get_percentage(self):
        get_percentage = False

        temp_generate = GenerateImage()

        temp_generate.set_random()
        values = temp_generate.param_get()

        percent = rate_image(values)

        if percent >= 0:
            get_percentage = True

        self.assertEqual(True, get_percentage)

