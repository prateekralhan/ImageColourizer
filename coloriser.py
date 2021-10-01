import numpy as np
import cv2
import os.path

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


def colorize_image(net,image_filename=None, cv2_frame=None):

    image = cv2.imread(image_filename) if image_filename else cv2_frame
    scaled = image.astype("float32")/255.0
    lab = cv2.cvtColor(scaled , cv2.COLOR_BGR2LAB)
    resized = cv2.resize(lab , (224,224))
    L = cv2.split(resized)[0]
    L -= 50 

    print("[info] colorising image ...")
    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0,:,:,:].transpose((1,2,0))

    ab = cv2.resize(ab, (image.shape[1],image.shape[0]))

    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:,:,np.newaxis],ab),axis=2)

    colorized = cv2.cvtColor(colorized,cv2.COLOR_LAB2BGR)
    colorized = np.clip(colorized,0,1)

    colorized = (255 * colorized).astype("uint8")
    return colorized


