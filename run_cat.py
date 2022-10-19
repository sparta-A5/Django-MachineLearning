import os
# '2' = I(Information), W(Warning), E(Error) 문구 중 I, W 를 제외하고 출력
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.models import load_model

# 학습된 모델 로드
model = load_model('model.h5')

print('Model loaded!')

# 업로드랑 연결하여 보여주는 코드 수정 필요
# test_imgs, test_labels = test_gen.__getitem__(5)
# y_pred = model.predict(test_imgs)
# classes = dict((v, k) for k, v in test_gen.class_indices.items())

# fig, axes = plt.subplots(2, 4, figsize=(20, 12))

# for img, test_label, pred_label, ax in zip(test_imgs, test_labels, y_pred, axes.flatten()):
#   test_label = classes[np.argmax(test_label)]
#   pred_label = classes[np.argmax(pred_label)]

#   ax.set_title('GT:%s\nPR:%s' % (test_label, pred_label))
#   ax.imshow(img)

# plt.show()