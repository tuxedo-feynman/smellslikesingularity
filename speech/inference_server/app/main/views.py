import json

from flask import render_template, Blueprint

import app.audio.utils as audio
from app.inference.gender import GenderClassifier


main = Blueprint(
    'main',
    __name__,
    template_folder='templates/main',
    url_prefix='/'
)

gender_classifier = GenderClassifier(os.environ['GENDER_MODEL_PATH'])


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html')

@main.route('/infer_gender', methods=['POST'])
def infer_gender():
    # first convert audio to a image of the audio spectograph
    specto_path = save_to_specto(convert_format(request.data))
    prediction = gender_classifier.predict(specto_path)
    return {
        'gender': prediction
    }
