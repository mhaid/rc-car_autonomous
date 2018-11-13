### 1. [optional] Install CUDA

.


### 2. Download files

.


### 3. Anaconda Virtual Environment

#### 3a. Setup Anaconda Environement

<b>Create</b> a new conda <b>environement</b> named 'rc_car'. As tensorflow does currentyl only support python version 3.5, we create the environement with <b>python version 3.5</b>:
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
Install protobuf:
```
(rc_car) C:\rc_car> conda install -c anaconda protobuf
```
Finally you have to install the following required packages:
```
(rc_car) C:\rc_car> pip install pillow
(rc_car) C:\rc_car> pip install lxml
(rc_car) C:\rc_car> pip install Cython
(rc_car) C:\rc_car> pip install jupyter
(rc_car) C:\rc_car> pip install matplotlib
(rc_car) C:\rc_car> pip install pandas
(rc_car) C:\rc_car> pip install opencv-python
```

#### 3c. Set the Pythonpath

Now set the PYTHONPATH of the anaconda environement:
```
set PYTHONPATH=C:\rc_car\computer\models;C:\rc_car\computer\models\research;C:\rc_car\computer\models\research\slim
```

#### 3d. Compile Protobufs


#### 3e. Run 'setup.py'

Navigate into the 'object_detection' folder located at 'C:\rc_car\computer\models\research\object_detection'. Run the following script:
```
(rc_car) C:\rc_car\computer\models\research\object_detection> python setup.py build
(rc_car) C:\rc_car\computer\models\research\object_detection> python setup.py install
```



### 4. Import Images

.

### 5. Generate training data

.


### 6. Generate labelmap and configure training

.


### 7. Train model

.

### 8. Export graph and move to 'Raspberry Pi'-folder
.
