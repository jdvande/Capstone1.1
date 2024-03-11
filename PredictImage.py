import torch
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
from CNN import CNN


class PredictImage:

    def __init__(self):
        self.image_path = "static/photos/image.png"
        self.model = CNN()

    def preprocess_image(self):
        transform = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor(),
                                        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
        image = Image.open(self.image_path)
        image = transform(image).unsqueeze(0)
        return image

    def predict_image(self, image):
        self.model.eval()
        with torch.no_grad():
            output = self.model(image)
            probabilities = torch.softmax(output, dim=1)
            max_probability = torch.max(probabilities)
            _, predicted_class = torch.max(probabilities, 1)
        return predicted_class.item(), max_probability.item()


temp = PredictImage()
img = temp.preprocess_image()
predicted_class, probabilities = temp.predict_image(img)

print('Probability:', probabilities)
