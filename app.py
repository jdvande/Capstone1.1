import io

from flask import Flask, render_template, request, jsonify, send_file
from GenerateImage import GenerateImage
from RateImage import rate_image
from PIL import Image
from ButtonTest import run_tests
import db_SQLA, NameEncoding


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

    nameTBExtended = NameEncoding.NameEncoding()
    userPhotoRenamed = nameTBExtended.nameExtension("static/photos_users/")  # name encode new file
    img.save(userPhotoRenamed)  # separate file for database path

    # SQLAlchemy image data to parameters database
    rating = (percent_mondrian // 10) * 10
    paramSession = db_SQLA.parameterSession()  # start database session

    parameters = db_SQLA.Parameter(userPhotoRenamed, create.h_line_get(), create.v_line_get(), create.cd_get(),
                                   create.lt_get(), create.ls_get(), create.hrsc_get(), create.vrsc_get(),
                                   create.ncc_get(), create.wrc_get(), rating)  # get parameters from image
    paramSession.add(parameters)  # submit image as one entry
    paramSession.commit()  # end database connection
    # End image data to database section

    # SQLAlchemy image data to averages database
    db_SQLA.AverageRating.update_averages(rating, int(create.h_line_get()), int(create.v_line_get()),
                                          int(create.cd_get()), int(create.lt_get()), int(create.ls_get()),
                                          int(create.hrsc_get()), int(create.vrsc_get()),
                                          int(create.ncc_get()), int(create.wrc_get()))
    # End SQLAlchemy image data to averages database

    return jsonify({'percent_mondrian': percent_mondrian})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
