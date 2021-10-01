import os
from uuid import uuid4
from flask import Flask,render_template,request,url_for,redirect,send_from_directory
from werkzeug.utils import secure_filename
import numpy as np
import cv2
from coloriser import colorize_image

UPLOAD_FOLDER = 'static/uploads/'
DOWNLOAD_FOLDER = 'static/downloads/'
ALLOWED_EXTENSIONS = {'png','jpg','jpeg','bmp'}

app = Flask(__name__, static_url_path="/static")
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

# limit upload size upto 10mb
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

prototxt = r'models/colorization_deploy_v2.prototxt'
model = r'models/colorization_release_v2.caffemodel'
points = r'models/pts_in_hull.npy'
points = os.path.join(os.path.dirname(__file__),points)
prototxt = os.path.join(os.path.dirname(__file__),prototxt)
model = os.path.join(os.path.dirname(__file__),model)

if not os.path.isfile(model):
    print("model is missing from the model folder")
    exit()

net = cv2.dnn.readNetFromCaffe(prototxt,model)
pts = np.load(points)

class8 = net.getLayerId("class8_ab")
conv8 = net.getLayerId("conv8_313_rh")
pts = pts.transpose().reshape(2,313,1,1)
net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full([1,313],2.606,dtype="float32")]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='POST':
        if 'file' not in request.files:
            print('No file attached in the request')
            return redirect(request.url)
        file=request.files['file']
        if file.filename == '':
            print("no file selected..")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            basedir = os.path.abspath(os.path.dirname(__file__))
            file.save(os.path.join(basedir,app.config['UPLOAD_FOLDER'], filename))
            process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('index.html')

def process_file(path,filename):
    colorized_image_output(path,filename)

def colorized_image_output(path,filename):
    img=cv2.imread(path)
    colorized_img=colorize_image(image_filename=path,net=net)
    cv2.imwrite(os.path.join(app.config['DOWNLOAD_FOLDER'] + filename),colorized_img)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == "__main__":
    #app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
