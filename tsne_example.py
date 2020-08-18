import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold, datasets

path = 'media'

import numpy as np
import glob
import options as opt
import os

labels = [] 

ivectors = glob.glob(os.path.join(path, '*.npy'))

length = len(ivectors)
dim = 512
ivector_np = np.zeros((length, dim))
print(ivector_np.shape)

targets = []
labels = ['cl', 'fuli', 'gongwenhua', 'liuyuguang', 
'lms', 'lsq', 'lxx', 'lzh', 'shanke', 'wry', 'zhangshuai163', 'zhuting', 'zlb', 'zq']

for i in range(length):

    ivector_np[i] = np.load(ivectors[i])
    #print(ivectors[i])
    print(ivectors[i])
    speaker_name = ivectors[i].split('\\')[-1].split('_')[0]
    
    #print(labels, speaker_name)
    if speaker_name not in labels:
        print('bad')
    #print(speaker_name)
    speaker_name = labels.index(speaker_name)
    targets.append(speaker_name)

'''t-SNE'''
tsne = manifold.TSNE(n_components=2, init='pca', random_state=501)
X_tsne = tsne.fit_transform(ivector_np.data)


print("Org data dimension is {}, Embedded data dimension is {}".format(ivector_np.shape[-1], X_tsne.shape[-1]))

'''嵌入空间可视化'''
x_min, x_max = X_tsne.min(0), X_tsne.max(0)
X_norm = (X_tsne - x_min) / (x_max - x_min)  # 归一化
plt.title('{}'.format('-'.join(labels)))
#plt.figure(num='{}'.format('-'.join(labels)), figsize=(6, 6))
for i in range(X_norm.shape[0]):
    plt.text(X_norm[i, 0], X_norm[i, 1], str(targets[i]), color=plt.cm.Set1(targets[i]), 
             fontdict={'weight': 'bold', 'size': 9})

plt.xticks([])
plt.yticks([])
plt.show()