import random

import numpy as np

from audio import read_mfcc
from batcher import sample_from_mfcc
from constants import SAMPLE_RATE, NUM_FRAMES
from conv_models import DeepSpeakerModel
from test import batch_cosine_similarity

# Reproducible results.
np.random.seed(123)
random.seed(123)

# Define the model here.
model = DeepSpeakerModel()

# Load the checkpoint.
model.m.load_weights('weights/ResCNN_triplet_training_checkpoint_265.h5', by_name=True)

# Sample some inputs for WAV/FLAC files for the same speaker.
mfcc_001 = sample_from_mfcc(read_mfcc('samples/PhilippeRemy/lms_20200811174251.wav', SAMPLE_RATE), NUM_FRAMES)
mfcc_002 = sample_from_mfcc(read_mfcc('samples/PhilippeRemy/lms_20200811174255.wav', SAMPLE_RATE), NUM_FRAMES)

# Call the model to get the embeddings of shape (1, 512) for each file.
predict_001 = model.m.predict(np.expand_dims(mfcc_001, axis=0))
predict_002 = model.m.predict(np.expand_dims(mfcc_002, axis=0))

# Do it again with a different speaker.
mfcc_003 = sample_from_mfcc(read_mfcc('samples/PhilippeRemy/lzh_20200812101503.wav', SAMPLE_RATE), NUM_FRAMES)
mfcc_004 = sample_from_mfcc(read_mfcc('samples/PhilippeRemy/wry_20200811195753.wav', SAMPLE_RATE), NUM_FRAMES)
mfcc_005 = sample_from_mfcc(read_mfcc('samples/PhilippeRemy/zq_20200811200033.wav', SAMPLE_RATE), NUM_FRAMES)
mfcc_006 = sample_from_mfcc(read_mfcc('samples/PhilippeRemy/fuli_20200812101411.wav', SAMPLE_RATE), NUM_FRAMES)

predict_003 = model.m.predict(np.expand_dims(mfcc_003, axis=0))
predict_004 = model.m.predict(np.expand_dims(mfcc_004, axis=0))
predict_005 = model.m.predict(np.expand_dims(mfcc_005, axis=0))
predict_006 = model.m.predict(np.expand_dims(mfcc_006, axis=0))
print(predict_001.shape)
# Compute the cosine similarity and check that it is higher for the same speaker.
print('SAME SPEAKER', batch_cosine_similarity(predict_001, predict_002)) # SAME SPEAKER [0.81564593]
print('DIFF SPEAKER1', batch_cosine_similarity(predict_001, predict_003)) # DIFF SPEAKER [0.1419204]
print('DIFF SPEAKER2', batch_cosine_similarity(predict_001, predict_004)) # DIFF SPEAKER [0.1419204]
print('DIFF SPEAKER3', batch_cosine_similarity(predict_001, predict_005)) # DIFF SPEAKER [0.1419204]
print('DIFF SPEAKER4', batch_cosine_similarity(predict_001, predict_006)) # DIFF SPEAKER [0.1419204]