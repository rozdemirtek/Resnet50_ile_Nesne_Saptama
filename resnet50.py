# -*- coding: utf-8 -*-
"""RESNET50.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10WRSQ17vgUV_Zi_8DnHTzPWSTlqVOBsX
"""

from keras.applications import ResNet50
from keras.utils.image_utils import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
from io import BytesIO
import os
import requests

model=ResNet50(weights="imagenet")

def prepare_image(image,target):
  image=image.resize(target)
  image=img_to_array(image)
  image=np.expand_dims(image,axis=0)
  image=imagenet_utils.preprocess_input(image)

  return image

imageURL="https://i.ytimg.com/vi/0fEcYI4HeKA/maxresdefault.jpg"
response=requests.get(imageURL)
image=Image.open(BytesIO(response.content))
image

data = {"success":False}
pre_image=prepare_image(image,target=(224,224)) #224x224 boyutlu hale getirir
preds=model.predict(pre_image)

results=imagenet_utils.decode_predictions(preds)
data["predictions"]=[]
for(imagenetID,label,prob) in results[0]:
  r={"label":label,"probability":float(prob)}
  data["predictions"].append(r)

data["success"]=True
print(data)