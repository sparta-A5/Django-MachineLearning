import os

# '2' = I(Information), W(Warning), E(Error) 문구 중 I, W 를 제외하고 출력
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt

test_datagen = ImageDataGenerator(
  rescale=1./255 # 일반화
)

'''
directory 형태로 불러오기 때문에 upload 폴더 안의 폴더로 사진이 업로드 되어야 함. 업로드 순서 = 최신순
'''
test_gen = test_datagen.flow_from_directory(
  'upload',
  target_size=(224, 224), # (height, width)
  batch_size=32,
  seed=2021,
  class_mode='categorical',
  shuffle=False
)

model = load_model('model.h5')

test_imgs, test_labels = test_gen.__getitem__(0)

result = model.predict(test_imgs[0].reshape(1, test_imgs.shape[1], test_imgs.shape[2], test_imgs.shape[3]))

dict = {0:'abyssinian', 1:'bengal', 2:'birman', 3:'bombay', 4:'british_shorthair', 5:'egyptian_mau', 6:'maine_coon', 7:'persian', 8:'ragdoll', 9:'russian_blue', 10:'siamese', 11:'sphynx'}
for i in range(12):
    if i == np.argmax(result):
        plt.title('This cat is : %s' % (dict[i]))
        plt.imshow(test_imgs[0])
        plt.savefig('result.png')
        # plt.show() 