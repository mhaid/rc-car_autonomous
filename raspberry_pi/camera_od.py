# Import packages
import os
from picamera.array import PiRGBArray
from picamera import PiCamera
import tensorflow as tf
import sys

sys.path.append('..')


# Set up constants
IM_WIDTH = 640
IM_HEIGHT = 480

NUM_CLASSES = 5

CWD_PATH = os.getcwd()
MODEL_NAME = 'detector'
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')
PATH_TO_LABELS = os.path.join(CWD_PATH,'detector','label_map.pbtxt')


# Load the Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)


# Define input and output tensors (i.e. data) for the object detection classifier
image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

num_detections = detection_graph.get_tensor_by_name('num_detections:0')


# Initialize Picamera and grab reference to the raw capture
camera = PiCamera()
camera.resolution = (IM_WIDTH,IM_HEIGHT)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(IM_WIDTH,IM_HEIGHT))
rawCapture.truncate(0)

for frame1 in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):

    frame = frame1.array
    frame.setflags(write=1)
    frame_expanded = np.expand_dims(frame, axis=0)

    # Perform the actual detection
    (scores, classes, num) = sess.run(
        [detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: frame_expanded})

    print(classes)

    rawCapture.truncate(0)

camera.close()
