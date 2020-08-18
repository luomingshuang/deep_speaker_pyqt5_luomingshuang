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

def get_centroid(embeddings, utterance_num):
    centroid = 0
    for utterance_id, utterance in enumerate(embeddings):
        if utterance_id <= (utterance_num-1):
            #print(utterance.shape)
            centroid = centroid + utterance 
        else: break
    centroid = centroid/utterance_num
    return centroid

speakers = ['cl', 'fuli', 'gongwenhua', 'liuyuguang', 
'lms', 'lsq', 'lxx', 'lzh', 'shanke', 'wry', 'zhangshuai163', 'zhuting', 'zlb', 'zq']
enroll_wav_path = 'media'
dict_spkid_embeddings = {}
enroll_nums = 8
total_wavs = glob.glob(os.path.join(data, '*.wav'))
print('total wavs: ', len(total_wavs))
for speaker in speakers:
    #print(speaker)
    speaker_wavs = glob.glob(os.path.join(enroll_wav_path, speaker+'_*.wav'))[:enroll_nums]
    #print(speaker, speaker_wavs)
    speaker_embeddings = []
    for wav in speaker_wavs:
        mfcc = sample_from_mfcc(read_mfcc(wav, SAMPLE_RATE), NUM_FRAMES)
        predict_feat = model.m.predict(np.expand_dims(mfcc, axis=0))
        speaker_embeddings.append(predict_feat)
    num_utterances = len(speaker_wavs)
    enroll_centroid_embeddings = get_centroid(speaker_embeddings, num_utterances)
    dict_spkid_embeddings[speaker] = enroll_centroid_embeddings

a = 0
total = 0
score = 0
name = 'Who?'

for speaker in speakers:
    test_wavs = glob.glob(os.path.join(enroll_wav_path, speaker+'_*.wav'))[enroll_nums:]
    x = 0
    y = 0
    for test_wav in test_wavs:
        scores= {}
        test_mel = []
        mfcc_feat = sample_from_mfcc(read_mfcc(test_wav, SAMPLE_RATE), NUM_FRAMES)
        output_feat = model.m.predict(np.expand_dims(mfcc_feat, axis=0))
        #  print(test_inputs.size())
        for speaker_name in dict_spkid_embeddings.keys():
            score_speaker = batch_cosine_similarity(dict_spkid_embeddings[speaker_name], output_feat)
            #print('speaker: ', speaker_name, 'score: ', score_speaker)
            scores[speaker_name] = score_speaker
            # if score_speaker > score :
            #     score = score_speaker
            #     name = speaker_name
                #print('speaker: ', name)
                #print('score: ', score)
        name = max(scores, key=scores.get)
        #print('test_wav: ', test_wav, 'predict speaker: ', name, 'predict score: ', scores)
        #print(speaker, name)
        if name == speaker:
            a += 1
            y += 1
        else:
            print('predict wrong {}:{} to {}:{}'.format(speaker, scores[speaker], name, scores[name]))
    total += len(test_wavs)
    print('speaker {}, {}/{}'.format(speaker, y, len(test_wavs)))

print('test_speaker_recognition is: ', a/total)