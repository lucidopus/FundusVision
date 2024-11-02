from flask import Flask, flash, request, redirect, url_for, render_template
import os, cv2
import numpy as np
from werkzeug.utils import secure_filename
import warnings
warnings.filterwarnings('ignore')

from keras.models import load_model
model = load_model("models/cataract_detection.h5")

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

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
		filename = secure_filename(file.filename)
        
        # Changed here
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], "image.jpg"))
		return render_template('index.html', filename="image.jpg")
	else:
		flash('Allowed image types are - png, jpg, jpeg')
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/getPrediction')
def getPrediction():
    res = cv2.imread("static/uploads/image.jpg")
    resized = cv2.resize(res, (224,224))
    mat224224 = np.array([resized])

    probability = model.predict(mat224224)

    prediction = "Normal Fundus" if probability < 0.5 else "Cataract Detected!"
    
    return str(prediction)

@app.route("/refresh")
def refresh():

	directory = "."

	for file in os.listdir(directory):
		if os.path.isfile(os.path.join(directory, file)):
			extension = os.path.splitext(file)[1]
			break

	file_path = "../static/uploads/image"+extension
	
	print(file_path)

	if os.path.exists(file_path):
		os.remove(file_path)
		return("File successfully deleted")
	else:
		return("File not found")
		
if __name__ == "__main__":
    app.run()