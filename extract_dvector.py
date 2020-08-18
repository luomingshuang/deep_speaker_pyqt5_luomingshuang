import os
import random
import time
import torch
import glob
import numpy as np
from torch.autograd import Variable

import torch
import random
import numpy as np

from deep_speaker.audio import read_mfcc
from deep_speaker.batcher import sample_from_mfcc
from deep_speaker.constants import SAMPLE_RATE, NUM_FRAMES
from deep_speaker.conv_models import DeepSpeakerModel
from deep_speaker.test import batch_cosine_similarity

# Reproducible results.
np.random.seed(123)
random.seed(123)

# Define the model here.
model = DeepSpeakerModel()

# Load the checkpoint.
model.m.load_weights('weights/ResCNN_triplet_training_checkpoint_265.h5', by_name=True)

data = 'media'

labels = ['cl', 'fuli', 'gongwenhua', 'liuyuguang', 
'lms', 'lsq', 'lxx', 'lzh', 'shanke', 'wry', 'zhangshuai163', 'zhuting', 'zlb', 'zq']
for speaker in labels:
    wavs = glob.glob(os.path.join(data, '{}_*.wav'.format(speaker)))
    print('{}: {} wavs'.format(speaker, len(wavs)))
    
if (__name__=='__main__'):
    print('Load model successfully.')
    
    inputs_wavs = glob.glob(os.path.join(data, '*.wav'))
    print(len(inputs_wavs))

    for wav in inputs_wavs:
        #print(wav)
        mfcc = sample_from_mfcc(read_mfcc(wav, SAMPLE_RATE), NUM_FRAMES)
        #print(mfcc.shape)
        predict_feat = model.m.predict(np.expand_dims(mfcc, axis=0))
        mel_db = predict_feat
        output_path = wav[:-4]+'.npy'
        np.save(output_path, mel_db)