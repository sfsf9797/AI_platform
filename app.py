#app.py
from flask import Flask, flash, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
from inference import inference 
from PIL import Image
from utils.utils import generate_filename
from config.config import * 

app = Flask(__name__)

app.secret_key = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/', methods=['POST'])
def upload_image():

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']

    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)

    if file and allowed_file(file.filename):

        #save the input image
        filename = secure_filename(file.filename)
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(output_path)

        #inference
        output_img = inference(output_path)
        output_img = Image.fromarray(output_img,'L')

        #save the inferenced image
        output_filename = generate_filename(filename)
        output_img_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
        output_img.save(output_img_path)

        flash('Ouput Image')
        return render_template('index.html', filename=output_filename)

    else:
        flash('Allowed image types are - png, jpg, jpeg')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    #display image output from model
    return redirect(url_for('static', filename='uploads/' + filename), code=301)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')
    