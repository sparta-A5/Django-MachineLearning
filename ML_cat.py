import os
# '2' = I(Information), W(Warning), E(Error) 문구 중 I, W 를 제외하고 출력
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.callbacks import ModelCheckpoint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.preprocessing import OneHotEncoder

from pprint import pprint

# 이미지 epoch 에러 발생 시 아래 코드 적용
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

'''
이미지 증강 기법
flow_from_directory 메소드를 사용하여 데이터셋이 저장된 폴더에서 직접 데이터 읽어오기
'''
train_datagen = ImageDataGenerator(
  rescale=1./255, # 일반화
  rotation_range=10, # 랜덤하게 이미지를 회전 (단위: 도, 0-180)
  zoom_range=0.1, # 랜덤하게 이미지 확대 (%)
  width_shift_range=0.1,  # 랜덤하게 이미지를 수평으로 이동 (%)
  height_shift_range=0.1,  # 랜덤하게 이미지를 수직으로 이동 (%)
  horizontal_flip=True # 랜덤하게 이미지를 수평으로 뒤집기
)

test_datagen = ImageDataGenerator(
  rescale=1./255 # 일반화
)

train_gen = train_datagen.flow_from_directory(
  'train',
  target_size=(224, 224), # (height, width)
  batch_size=32,
  seed=2021,
  class_mode='categorical',
  shuffle=True
)

test_gen = test_datagen.flow_from_directory(
  'test',
  target_size=(224, 224), # (height, width)
  batch_size=32,
  seed=2021,
  class_mode='categorical',
  shuffle=False
)

# 클래스 이름, 번호 확인
pprint(train_gen.class_indices)

# 이미지 프리뷰
# preview_batch = train_gen.__getitem__(0)

# preview_imgs, preview_labels = preview_batch

# plt.title(str(preview_labels[0]))
# plt.imshow(preview_imgs[0])

'''
전이 학습

https://keras.io/api/applications/
'''
input = Input(shape=(224, 224, 3))

base_model = InceptionV3(weights='imagenet', include_top=False, input_tensor=input, pooling='max')

x = base_model.output
x = Dropout(rate=0.25)(x)
x = Dense(256, activation='relu')(x)
output = Dense(12, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=output)

model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.001), metrics=['acc'])

'''
학습
ModelCheckpoint('model.h5', monitor='val_acc', verbose=1, save_best_only=True)
val_acc가 높은 1개의 모델(save_best_only)을 model.h5 라는 파일로 저장

https://keras.io/api/callbacks/model_checkpoint/
'''
history = model.fit(
    train_gen,
    validation_data=test_gen,
    epochs=20,
    callbacks=[
      ModelCheckpoint('model.h5', monitor='val_acc', verbose=1, save_best_only=True)
    ]
)

# loss/val_loss, acc/val_acc 그래프 출력

# fig, axes = plt.subplots(1, 2, figsize=(20, 6))
# axes[0].plot(history.history['loss'])
# axes[0].plot(history.history['val_loss'])
# axes[1].plot(history.history['acc'])
# axes[1].plot(history.history['val_acc'])