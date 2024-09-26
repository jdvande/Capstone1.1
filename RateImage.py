from PredictImage import PredictImage
from GenerateImage import GenerateImage


# This function runs 25 different images generated using the same parameters in order to calculate how accurate those
# parameters are on average at creating Mondrian like images.
def rate_image(values):
    i = 0
    total_correct = 0
    process = PredictImage("static/photos/temp-img.png")
    while i < 25:
        temp_gen = GenerateImage(values)
        temp_img = temp_gen.generate_image()
        temp_img.save("static/photos/temp-img.png")

        processed_temp = process.preprocess_image()
        predicted_class, probability = process.predict_image(processed_temp)

        if predicted_class == 0:
            total_correct += 1
        i += 1

    percentage = (total_correct / 25) * 100
    percentage = round(percentage, 2)

    return percentage
