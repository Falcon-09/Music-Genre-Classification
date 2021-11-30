from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from Metadata import getmetadata
from predict import predict_gen
import os

app = Flask(__name__)
app.secret_key = '5%68*&)_)=+_^$3@!/'

genre=0

@app.route("/")
def home():
    return render_template('index.html')


app.config['ALLOWED_EXTENSIONS'] = ['wav']


def vaild_file(filename):
    if not '.' in filename:
        return False

    ext = filename.rsplit('.', 1)[1]

    if ext.lower() in app.config['ALLOWED_EXTENSIONS']:
        return True
    else:
        return False


@app.route("/result", methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        if request.files:
            f = request.files['file1']

            # if f.filename == "":
            #     # flash('Enter a valid file .wav file')
            #     return redirect(request.url_root)

            if not vaild_file(f.filename):
                flash('only .wav files are valid')
                return redirect(request.url_root)

            else:
                f = request.files['file1']
                # filename= secure_filename(f.filename)

                meta = getmetadata(f)
                genre = predict_gen(meta)
                print(genre)
                return render_template('result.html', gen=genre)



