import torch
import torchvision.transforms as transforms
from PIL import Image
from CNN import CNN


class PredictImage:

    def __init__(self, path=None):
        self.model = CNN()

        if path is None:
            self.image_path = "static/photos/image.png"
        else:
            self.image_path = path

    # This function takes in our generated image and resizes it as well as normalizes it to the same values as were used
    # in the neural network's training.
    def preprocess_image(self):
        transform = transforms.Compose([transforms.Resize((224, 224)), transforms.ToTensor(),
                                        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
        image = Image.open(self.image_path)
        image = transform(image).unsqueeze(0)
        return image

    # This function sorts an image that has been preprocessed into one of the two training classes used for the neural
    # network. It returns which class the network thinks the image belongs to as well as it's certainty as a percentage
    def predict_image(self, image):
        model_state_dict = torch.load("weights/weights.pth", map_location='cpu')
        self.model.load_state_dict(model_state_dict)

        self.model.eval()
        with torch.no_grad():
            output = self.model(image)
            probabilities = torch.softmax(output, dim=1)
            max_probability = torch.max(probabilities)
            _, predicted_class = torch.max(probabilities, 1)
        return predicted_class.item(), max_probability.item()
