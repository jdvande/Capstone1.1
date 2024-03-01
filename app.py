import io

from flask import Flask, render_template, request, send_file
from GenerateImage import GenerateImage
from PIL import Image

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('Login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/generate-image')
def generate_image():
    # Create an image using PIL, for example
    image = Image.new('RGB', (1500, 800), '#EDFCFE')
    img_io = io.BytesIO()  # Create a BytesIO buffer
    image.save(img_io, 'PNG')  # Save the image as PNG to the buffer
    img_io.seek(0)  # Seek to the start of the stream
    return send_file(img_io, mimetype='image/png')  # Send the buffer's content as a PNG image


if __name__ == '__main__':
    app.run(debug=True)
