# Computer

If you want to use my pretrained classifier, make sure to check out step 2, 8 and 9. Otherwise to train your own object classifier, start at step 1 or 2, depending on wether you want and can use your graphics card to train the classifier.

### 1. [optional] Install CUDA

.


### 3. Anaconda Virtual Environment

#### 3a. Setup Anaconda Environement

<b>Create</b> a new conda <b>environement</b> named 'rc_car'. As tensorflow does currently only support python version 3.5, create the environement with <b>python version 3.5</b>:
```
C:\rc_car> conda create -n rc_car pip python=3.5
```
Now <b>activate</b> the newly created <b>environement</b>:
```
C:\rc_car> activate rc_car
```

#### 3b. Install required packages

Inside the conda environement, install <b>'tensorflow'</b> via pip. If you installed CUDA, install <b>'tensorflow-gpu'</b>:
```
(rc_car) C:\rc_car> pip install --ignore-installed --upgrade tensorflow
```
or
```
(rc_car) C:\rc_car> pip install --ignore-installed --upgrade tensorflow-gpu
```
Finally you have to install the following required packages:
```
(rc_car) C:\rc_car> pip install Cython
(rc_car) C:\rc_car> pip install pillow
(rc_car) C:\rc_car> pip install lxml
(rc_car) C:\rc_car> pip install jupyter
(rc_car) C:\rc_car> pip install matplotlib
(rc_car) C:\rc_car> pip install pandas
(rc_car) C:\rc_car> pip install opencv-python
```
Install protobuf:
```
(rc_car) C:\rc_car> conda install -c anaconda protobuf
```

#### 3c. Compile Protobufs

Navigate into the 'research' folder located at 'C:\rc_car\computer\models\research'. Run the following script:
```
(rc_car) C:\rc_car\computer\models\research> for %f in (.\object_detection\protos\*.proto) do protoc --python_out=. %f
```
Now you should find a new '.py' file for every '.proto' file in the 'proto'-folder
Note: if you're getting errors while compiling, check out the official [Tensorflow manual](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md#protobuf-compilation).

#### 3d. Set the 'PYTHONPATH'

Now set the 'PYTHONPATH' of the anaconda environement:
```
(rc_car) C:\rc_car\computer\models\research> set PYTHONPATH=C:\rc_car\computer\models;C:\rc_car\computer\models\research;C:\rc_car\computer\models\research\slim
```
Note: You will have to set the 'PYTHONPATH' in every new instance of the CMD-Terminal. Closing the terminal will reset the 'PYTHONPATH'-Variable.

#### 3e. Run 'setup.py'

Run the following script:
```
(rc_car) C:\rc_car\computer\models\research> python setup.py build
(rc_car) C:\rc_car\computer\models\research> python setup.py install
```

#### 3f. Verify installation

To verify your installation, run the jupiter notebook inside the 'object_detection'-folder:
```
(rc_car) C:\rc_car\computer\models\research\object_detection> jupyter notebook object_detection_tutorial.ipynb
```


### 4. Import and label images

There are two options of gathering the images for your classifier:
4a. Download them from the internet (e.g. google images)
4b. Take your own images
In both cases, make sure there are not less than 200 images to train your classifier on.

#### 4a Download images

There are plenty of option to choose. You could eather install a add-on to download pictures directly from <b>google image search</b>, gather your images from a database like [Image Net](http://www.image-net.org/), etc.
<p align="center">
  <img src="documentation/image_net.png">
</p>
After you downloaded enough pictures, go to step 4c.

#### 4b Take own images

Take your own pictures with your mobile phone, camera or even the pi-cam from your raspberry pi. The images should be scaled down to max. 1080px x 720px (I will explain this step further down), otherwise the training time will increase. Therefore it's not important if you shoot them in 4K or just HD.
I for example took 219 pictures but will increase the count in the future.

#### 4c Resize images

Move all your pictures into the 'images'-directory located in in 'object_detection'. Now run the "resize.py".script:
```
(rc_car) C:\rc-car\computer\models\research\object_detection\images>python resize.py
```
After the script finished, you should see a change in width, heiht and size of the files.
Complete this step by moving 20% of the images into the test folder. It's best to choose those randomly, because the object classifier should learn to recognize the images across multiple backgrounds and positions of the sign.

#### 4d Label images

To label your test and train images, I suggest to use ['LabelImg'](https://github.com/tzutalin/labelImg) by [tzutalin](https://github.com/tzutalin). Click [here](https://tzutalin.github.io/labelImg/) to get directly to the download page.
After download and installation, open LabelImg, choose the right directory and start drawing the bounding boxes arount the objects.

Note: To fasten up the process, activate 'autosave' under the 'edit'-menu entry on the top left of the program. Also you can create a new rectangle by pressing 'w' and navigate by with 'a' and 'd'.

Finally check if all the bounding boxes meet the minimum size by running the 'checkSize.py' script:
```
(rc_car) C:\rc-car\computer\models\research\object_detection\images>python checkSize.py --move
```
All images and their corresponding xml-files which contain one or more bounding boxes smaller than 32px x 32px will be moved to the 'wrong_data'-folder inside 'test' or  'training'.


### 5. Generate training data

```
(rc_car) C:\rc-car\computer\models\research\object_detection> python xml_to_csv.py
```

Replace the label map section in 'generate_tfrecord.py' with your own classes.
Now issue the following commands:
```
(rc_car) C:\rc-car\computer\models\research\object_detection> python generate_tfrecord.py --csv_input=images\train_labels.csv --image_dir=images\train --output_path=train.record
(rc_car) C:\rc-car\computer\models\research\object_detection> python generate_tfrecord.py --csv_input=images\test_labels.csv --image_dir=images\test --output_path=test.record
```


### 6. Generate labelmap and configure training

#### 6a Generate labelmap

Edit 'labelmap.pbtxt' by editing the items. If you got more/less than 5 classes, add more/delete some.
Make sure the order of the classes in the 'labelmap.pbtxt' and 'generate_tfrecord.py' are the same.

#### 6b Configure training

Navigate to 'C:\rc-car\computer\models\research\object_detection\samples\configs' and copy 'ssd_mobilenet_v1_coco.config' into the training directory inside 'object_detection' ('C:\rc-car\computer\models\research\object_detection\training').
Open the config file with a text-editor of your choice and make the following changes:
```
L. 9   | num_classes: 5
L. 156 | fine_tune_checkpoint: "D:/rc-car/computer/models/research/object_detection/ssd_mobilenet_v1_coco_2018_01_28/model.ckpt"
L. 175 | input_path: "D:/rc-car/computer/models/research/object_detection/test.record"
L. 177 | label_map_path: "D:/rc-car/computer/models/research/object_detection/training/labelmap.pbtxt"
L. 189 | input_path: "D:/rc-car/computer/models/research/object_detection/train.record"
L. 191 | label_map_path: "D:/rc-car/computer/models/research/object_detection/training/labelmap.pbtxt"
```
Note: Change the 'num_classes'-variable to the number of different objects you want your classifier to detect.


### 7. Train model

```
python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2_pets.config
```


### 8. Export graph and move to 'Raspberry Pi'-folder
.
