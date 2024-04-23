import io

from flask import Flask, render_template, request, jsonify, send_file
from GenerateImage import GenerateImage
from RateImage import rate_image
from PIL import Image
from ButtonTest import run_tests


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/generated_image')
def generated_image():
    # time.sleep(5)
    return render_template('generated_image.html')


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


@app.route('/execute-generate', methods=['POST'])
def execute_generate():
    data = request.json
    values = data['values']
    create = GenerateImage(values)

    img = create.generate_image()
    img.save("static/photos/image.png")

    percent_mondrian = rate_image(values)

    print(str(percent_mondrian))

    return jsonify({'percent_mondrian': percent_mondrian})


if __name__ == '__main__':
    app.run(debug=True)
